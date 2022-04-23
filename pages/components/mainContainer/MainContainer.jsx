import React from 'react'
import { useState } from 'react'

import { NavBar, Map, SideMenu } from '../'

const MainContainer = ({}) => {
  const [sideMenuVisible, setSideMenuVisible] = useState();

  return (
    <div>
      <NavBar />
      <Map />
      <SideMenu visible={sideMenuVisible} />
    </div>
  )
}

export default MainContainer