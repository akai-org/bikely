import React, {useState} from "react"
import styles from "./Input.module.css"
import classNames from "classnames"

const Input = ({className, placeholder, onChange, value}) => {
    return <input type="text" placeholder={placeholder} className={classNames(className, styles.input)} value={value} onChange={onChange}/>
}

export default Input;