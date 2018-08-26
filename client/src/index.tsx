import * as React from 'react'
import * as ReactDOM from 'react-dom'
import App from './containers/App/App'
import { Provider } from 'react-redux'
import { applyMiddleware, compose, createStore } from 'redux'
import thunk from 'redux-thunk'
import rootReducer from './redux/reducers/index'
import './index.css'
// import registerServiceWorker from './registerServiceWorker';

const composeEnhancers =
    (window as any).__REDUX_DEVTOLS_EXTENSION_COMPOSE__ || compose

const store = createStore(rootReducer, composeEnhancers(applyMiddleware(thunk)))

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root') as HTMLElement
)
// registerServiceWorker();
