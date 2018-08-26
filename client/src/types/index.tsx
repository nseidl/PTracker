import {
    GET_DATE,
    GET_DATE_SUCCESS,
    GET_DATE_FAILURE,
    GET_TEST_ITEMS,
    GET_TEST_ITEMS_SUCCESS,
    GET_TEST_ITEMS_FAILURE
} from '../redux/constants'

export interface IDate {
    readonly date: string
    readonly asString: string
}

export interface IGetDate {
    type: GET_DATE | GET_DATE_SUCCESS | GET_DATE_FAILURE
    data: IDate
}

export type DateAction = IGetDate

export interface ITestItem {
    readonly id: string
    readonly listing_name: string
    readonly condition: string
    readonly post_link: string
    readonly price: number
    readonly website: string
    readonly date_scrabed: Date
    readonly images: string[]
    readonly listing_dates: {
        date_listed: string
        date_sold: string
    }
    readonly misc: any
    readonly post_description: string
}

export interface IGetTestItems {
    type: GET_TEST_ITEMS | GET_TEST_ITEMS_SUCCESS | GET_TEST_ITEMS_FAILURE
    data: any
}

export type TestItemsAction = IGetTestItems
