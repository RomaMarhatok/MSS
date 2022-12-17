import {createRouter,createWebHashHistory} from "vue-router";
import homePage from "./src/pages/homePage"
import registrationPage from "./src/pages/registrationPage"
import authenticationPage from "./src/pages/authenticationPage"
import documentsPage from './src/pages/userPages/documentsPage'
import personalInfoPage from "./src/pages/userPages/personalInfoPage"  
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"Home",component:homePage},
        {path:"/registration/",name:"Registration",component:registrationPage},
        {path:"/authentication/",name:"Authentication",component:authenticationPage},
        {path:"/user/documents/",name:"UserDocuments",component:documentsPage},
        {path:"/user/home/",name:"UserHomePage",component:personalInfoPage}
    ]
})
export default router