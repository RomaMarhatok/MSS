import {createRouter,createWebHashHistory} from "vue-router";
import frontPage from "./src/pages/frontPage"
import registrationPage from "./src/pages/registrationPage"
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"Home",component:frontPage},
        {path:"/registration/",name:"Registration",component:registrationPage}
    ]
})
export default router