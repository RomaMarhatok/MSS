import {createRouter,createWebHashHistory} from "vue-router";
import homePage from "./src/pages/homePage"
import registrationPage from "./src/pages/registrationPage"
import authenticationPage from "./src/pages/authenticationPage"
import documentsPage from './src/pages/userPages/documentsPage'
import personalInfoPage from "./src/pages/userPages/personalInfoPage"  
import singleDocumentPage from "./src/pages/userPages/singleDocumentPage"
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"site-home-page",component:homePage},
        {path:"/registration/",name:"registration-page",component:registrationPage},
        {path:"/authentication/",name:"authentication-page",component:authenticationPage},
        {path:"/user/:userSlug/",children:[
            {
                path:"documents/",
                name:"patuent-documents-page",
                component:documentsPage,
            },
            {
                path:"document/:documentSlug/",
                name:"single-patuent-document-page",
                component:singleDocumentPage
            },
            {
                path:"home/",
                name:"patient-profile-page",
                component:personalInfoPage
            },
        ]},
        

    ]
})
export default router