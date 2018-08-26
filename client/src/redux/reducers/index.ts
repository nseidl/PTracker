import { combineReducers } from 'redux'

import date from './date'
import testItems from './testItems'

const rootReducer = combineReducers({
    date,
    testItems
})

export default rootReducer
