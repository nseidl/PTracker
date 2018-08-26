import * as React from 'react'
import * as types from '../types'

// const styles = require('./SimpleTestItem.css')
// const classNames = require('classnames')

interface Props {
    testItemInformation: types.ITestItem
}

export default class SimpleTestItem extends React.Component<Props, {}> {
    render() {
        const testItem = this.props.testItemInformation

        return (
            <p key={testItem.id}>
                {testItem.listing_name}: ${testItem.price} (
                <a href={testItem.post_link} target="_blank">
                    link
                </a>
                )
            </p>
        )
    }
}
