import {memo, useMemo} from "react"

import {Typography} from "antd"

import usePlayground from "../../hooks/usePlayground"
import {componentLogger} from "../../assets/utilities/componentLogger"
import {findPropertyById} from "../../hooks/usePlayground/middlewares/playgroundVariantMiddleware"
import {findPropertyInObject} from "../../hooks/usePlayground/assets/helpers"
import {getMetadataLazy} from "../../state"

import {renderMap} from "./assets/helpers"

import type {PlaygroundVariantPropertyControlProps} from "./types"
import type {Enhanced, EnhancedObjectConfig} from "../../assets/utilities/genericTransformer/types"
import type {EnhancedVariant} from "../../assets/utilities/transformer/types"

// TODO: RENAME TO PlaygroundPropertyControl
const PlaygroundVariantPropertyControl = ({
    propertyId,
    variantId,
    className,
    as,
    view,
    rowId,
    withTooltip,
    value: propsValue,
    onChange,
    placeholder,
}: PlaygroundVariantPropertyControlProps): React.ReactElement | null => {
    componentLogger("PlaygroundVariantPropertyControl", variantId, propertyId)

    const {
        mutate,
        handleParamUpdate: updateVariantProperty,
        baseProperty,
    } = usePlayground({
        hookId: "PlaygroundVariantPropertyControl",
        stateSelector: (state) => {
            const object = !!rowId
                ? state.generationData.inputs.value.find((v) => v.__id === rowId) ||
                  (state.generationData.messages.value || []).find((v) => v.__id === rowId)
                : variantId
                  ? state.variants.find((v) => v.id === variantId)
                  : null

            if (!object) {
                return {}
            } else {
                const property = !!rowId
                    ? (findPropertyInObject(object, propertyId) as EnhancedObjectConfig<any>)
                    : (findPropertyById(
                          object as EnhancedVariant,
                          propertyId,
                      ) as EnhancedObjectConfig<any>)
                return {baseProperty: property}
            }
        },
    })

    const property = useMemo(() => {
        if (!baseProperty) return null

        const {__metadata, value: _value} = baseProperty
        const value = propsValue ?? _value

        const handler = rowId
            ? (e: any) => {
                  if (onChange) {
                      const val =
                          e !== null && e !== undefined
                              ? typeof e === "object" && "target" in e
                                  ? e.target.value
                                  : e
                              : null

                      onChange(val)
                  } else {
                      mutate(
                          (clonedState) => {
                              if (!clonedState) return clonedState
                              const val =
                                  e !== null && e !== undefined
                                      ? typeof e === "object" && "target" in e
                                          ? e.target.value
                                          : e
                                      : null

                              const object =
                                  clonedState.generationData.inputs.value.find(
                                      (v) => v.__id === rowId,
                                  ) ||
                                  clonedState.generationData.messages.value.find(
                                      (v) => v.__id === rowId,
                                  )

                              if (!object) return clonedState

                              const property = findPropertyInObject(
                                  object,
                                  propertyId,
                              ) as Enhanced<any>
                              if (!property) return clonedState

                              if (property.value === val) return clonedState

                              property.value = val

                              return clonedState
                          },
                          {
                              revalidate: false,
                          },
                      )
                  }
              }
            : (newValue: any) => {
                  if (onChange) {
                      onChange({
                          value: newValue,
                          id: baseProperty.__id,
                      })
                  } else {
                      updateVariantProperty?.(newValue, baseProperty.__id, variantId)
                  }
              }

        return {
            __metadata: getMetadataLazy(__metadata),
            value,
            handleChange: handler,
        }
    }, [
        baseProperty,
        propsValue,
        rowId,
        onChange,
        mutate,
        propertyId,
        updateVariantProperty,
        variantId,
    ])

    if (!property) {
        return null
    }

    const {__metadata: metadata, value: _value, handleChange} = property
    const value = propsValue ?? _value

    if (!metadata) {
        return <Typography.Text>unable to find metadata for property</Typography.Text>
    }

    const renderer = renderMap[metadata.type]
    if (renderer) {
        return renderer({
            withTooltip,
            metadata: metadata as any,
            value,
            handleChange,
            as,
            className,
            view,
            placeholder,
        })
    }

    return <Typography.Text>Unknown type: {metadata.type}</Typography.Text>
}

export default memo(PlaygroundVariantPropertyControl)
