export function objectToArray(obj: any) {
    return Object.keys(obj).map((key: any) => {
        return obj[key]
    })
}
