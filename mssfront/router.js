import {createRouter,createWebHashHistory} from "vue-router";
import frontPage from "./src/pages/frontPage"
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"Home",component:frontPage}
    ]
})
export default router