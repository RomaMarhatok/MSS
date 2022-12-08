import {createRouter,createWebHashHistory} from "vue-router";
import homePage from "./src/pages/homePage"
import registrationPage from "./src/pages/registrationPage"
import authenticationPage from "./src/pages/authenticationPage"
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"Home",component:homePage},
        {path:"/registration/",name:"Registration",component:registrationPage},
        {path:"/authentication/",name:"Authentication",component:authenticationPage}
    ]
})
export default router