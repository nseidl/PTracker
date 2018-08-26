import { GET_DATE, GET_DATE_SUCCESS, GET_DATE_FAILURE } from '../constants'
import * as types from '../../types'

const initialState = {
    asString: '',
    date: ''
}

export default function date(
    state: types.IDate = initialState,
    action: types.DateAction
): types.IDate {
    switch (action.type) {
        case GET_DATE:
            return { ...state }
        case GET_DATE_SUCCESS:
            return {
                ...state,
                asString: action.data.date
            }
        case GET_DATE_FAILURE:
            return {
                ...state
            }
    }
    return state
}
