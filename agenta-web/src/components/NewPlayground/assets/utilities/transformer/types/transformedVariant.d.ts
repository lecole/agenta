import type {Enhanced} from "../../genericTransformer/types"
import type {InputType} from "./input"
import type {Message} from "./message"
import type {AgentaConfigPrompt, BaseVariant} from "./variant"

/** Enhanced Variant with embedded metadata */
export interface EnhancedVariant<
    T extends Enhanced<AgentaConfigPrompt> = Enhanced<AgentaConfigPrompt>,
> extends BaseVariant {
    isChat: boolean
    prompts: T[]
    __isMutating?: boolean
}
