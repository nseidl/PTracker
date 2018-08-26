import {
    GET_DATE,
    GET_DATE_SUCCESS,
    GET_DATE_FAILURE,
    GET_TEST_ITEMS,
    GET_TEST_ITEMS_SUCCESS,
    GET_TEST_ITEMS_FAILURE
} from './constants'
import { Dispatch } from 'redux'

function handleAsync({
    url,
    actions,
    actionParams = {},
    fetchParams = {}
}: {
    url: string
    actions: { action: string; successAction: string; failureAction: string }
    actionParams: object
    fetchParams: RequestInit | undefined
}) {
    return (dispatch: Dispatch) => {
        dispatch({ type: actions.action })
        console.log(url)
        return fetch(url, { credentials: 'include', ...fetchParams })
            .then(response => {
                console.log(response)
                return response.json()
            })
            .then(
                data =>
                    dispatch({
                        type: actions.successAction,
                        data,
                        ...actionParams
                    }),
                error =>
                    dispatch({
                        type: actions.failureAction,
                        data: error,
                        ...actionParams
                    })
            )
    }
}

export function getDate() {
    return handleAsync({
        url: `${process.env.REACT_APP_API_URL}/api/date`,
        actions: {
            action: GET_DATE,
            successAction: GET_DATE_SUCCESS,
            failureAction: GET_DATE_FAILURE
        },
        fetchParams: {},
        actionParams: {}
    })
}

export function getAllTestItems() {
    return handleAsync({
        url: `${process.env.REACT_APP_API_URL}/api/test_items`,
        actions: {
            action: GET_TEST_ITEMS,
            successAction: GET_TEST_ITEMS_SUCCESS,
            failureAction: GET_TEST_ITEMS_FAILURE
        },
        fetchParams: {},
        actionParams: {}
    })
}
