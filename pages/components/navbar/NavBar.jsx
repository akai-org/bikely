import react, {useState} from "react";
import styles from "./NavBar.module.css"
import Input from "./../input/Input"
import { AiOutlineMenu } from "react-icons/ai";

const NavBar = ({}) => {
    const [destinationValue, setDestinationValue] = useState()

    return <div className={styles.navbarContainer}>
        <div className={styles.icon}>
            <AiOutlineMenu />
        </div>
        <div>
            <Input placeholder={"Skąd?"}/>
        </div>
    </div>
}

export default NavBar