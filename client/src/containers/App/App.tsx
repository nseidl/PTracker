import * as React from 'react'
import { getDate, getAllTestItems } from '../../redux/actions'
import { connect } from 'react-redux'

import { bindActionCreators, Dispatch } from '../../../node_modules/redux'
import * as Spinner from 'react-spinkit'
import * as types from '../../types'
import * as utils from '../../utils'

import SimpleTestItem from '../../components/SimpleTestItem'

const styles = require('./App.css')
// const classNames = require('classnames')

interface Props {
    getDate: any
    date?: types.IDate
    getAllTestItems: any
    testItems?: any
}

interface State {
    itemsLoading: boolean
}

export class App extends React.Component<Props, State> {
    readonly state: State = {
        itemsLoading: true
    }
    async componentDidMount() {
        await this.props.getDate()
        await this.props.getAllTestItems()

        this.setState({ itemsLoading: false })
    }

    render() {
        const { date, testItems } = this.props

        const testItemsList = utils.objectToArray(testItems)

        const loader = <Spinner name="circle" />

        return (
            <div className={styles.app}>
                <header className={styles.appHeader}>
                    <h1 className={styles.appTitle}>PTracker</h1>
                </header>
                {date && !this.state.itemsLoading ? (
                    <div className={styles.content}>
                        <p>{date.asString}</p>
                        {testItemsList
                            .sort(
                                (a: types.ITestItem, b: types.ITestItem) =>
                                    b.price - a.price
                            )
                            .map((aTestItem: types.ITestItem) => (
                                <SimpleTestItem
                                    testItemInformation={aTestItem}
                                />
                            ))}
                        <div className={styles.container}>
                            <div className={styles.picture}>(picture) </div>
                            <div className={styles.text}>
                                <div className={styles.name}>
                                    H 6D-400c MS Medium Format DSLR Camera
                                </div>
                                <div className={styles.price}>$1999</div>
                                <div>link</div>
                            </div>
                        </div>
                        <div className={styles.container}>
                            <div className={styles.picture}>(picture) </div>
                            <div className={styles.text}>
                                <div className={styles.name}>
                                    H 6D-400c MS Medium Format DSLR Camera
                                </div>
                                <div className={styles.price}>$1999</div>
                                <div>link</div>
                            </div>
                        </div>
                        <div className={styles.container}>
                            <div className={styles.picture}>(picture) </div>
                            <div className={styles.text}>
                                <div className={styles.name}>
                                    H 6D-400c MS Medium Format DSLR Camera
                                </div>
                                <div className={styles.price}>$1999</div>
                                <div>link</div>
                            </div>
                        </div>
                        
                    </div>
                ) : (
                    loader
                )}
            </div>
        )
    }
}

export default connect(
    (state: any) => ({
        date: state.date,
        testItems: state.testItems
    }),
    (dispatch: Dispatch) =>
        bindActionCreators({ getDate, getAllTestItems }, dispatch)
)(App)
