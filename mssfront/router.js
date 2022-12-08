import {createRouter,createWebHashHistory} from "vue-router";
import homePage from "./src/pages/homePage"
import registrationPage from "./src/pages/registrationPage"
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"Home",component:homePage},
        {path:"/registration/",name:"Registration",component:registrationPage}
    ]
})
export default router