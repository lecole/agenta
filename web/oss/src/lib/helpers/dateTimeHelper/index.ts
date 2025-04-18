import dayjs from "./dayjs"

export const formatDate = (date: dayjs.ConfigType): string => {
    return dayjs(date).format("DD MMM YYYY | h:mm a")
}

export const formatDate24 = (date: dayjs.ConfigType, includeSeconds = false): string => {
    return dayjs(date).format("DD MMM YY, HH:mm" + (includeSeconds ? ":ss" : ""))
}

export const formatDay = (date: dayjs.ConfigType): string => {
    return dayjs(date, "YYYY/MM/DD H:mm:ssAZ").format("DD MMM YYYY")
}
