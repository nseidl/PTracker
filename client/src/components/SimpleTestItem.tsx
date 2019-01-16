import * as React from 'react'
import * as types from '../types'

// const styles = require('./SimpleTestItem.css')
// const classNames = require('classnames')

interface Props {
    testItemInformation: types.ITestItem
}

const styles = require('./SimpleTestItem.css')
export default class SimpleTestItem extends React.Component<Props, {}> {
    render() {
        const testItem = this.props.testItemInformation

        return (
            <a
                className={styles.container}
                href={testItem.post_link}
                target="_blank"
            >
                <div>
                    <div className={styles.picture}>(picture)</div>
                </div>
                <div className={styles.text}>
                    <div className={styles.name}>
                        {testItem.listing_name}
                    </div>

                    <div className={styles.price}>{testItem.price}</div>
                </div>
            </a>
        )
    }
}
