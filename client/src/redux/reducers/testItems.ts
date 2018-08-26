import {
    GET_TEST_ITEMS,
    GET_TEST_ITEMS_SUCCESS,
    GET_TEST_ITEMS_FAILURE
} from '../constants'
import * as types from '../../types'

const initialState = {}

export default function testItems(
    state: {} = initialState,
    action: types.TestItemsAction
) {
    switch (action.type) {
        case GET_TEST_ITEMS:
            return { ...state }
        case GET_TEST_ITEMS_SUCCESS:
            return {
                ...state,
                ...action.data
            }
        case GET_TEST_ITEMS_FAILURE:
            return {
                ...state
            }
    }
    return state
}
