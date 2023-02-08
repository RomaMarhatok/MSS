import {createRouter,createWebHashHistory} from "vue-router";
import homePage from "./src/pages/homePage"
import registrationPage from "./src/pages/registrationPage"
import authenticationPage from "./src/pages/authenticationPage"
import documentsPage from './src/pages/user/documents/documentsListPage'
import personalInfoPage from "./src/pages/user/personalInfoPage"  
import singleDocumentPage from "./src/pages/user/documents/singleDocumentPage"
import doctorsListPage from "./src/pages/user/doctors/doctorsListPage" 
import doctorSinglePage from "./src/pages/user/doctors/singleDoctorPage"
import appointmentsPage from "./src/pages/user/appointments/appointmentsPage"
const router = createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:"/",name:"site-home-page",component:homePage},
        {path:"/registration/",name:"registration-page",component:registrationPage},
        {path:"/authentication/",name:"authentication-page",component:authenticationPage},
        {path:"/doctors/",name:"doctors-list-page",component:doctorsListPage},
        {path:"/doctor/:doctorSlug",name:"doctor-sing-display-section",component:doctorSinglePage},
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
            {
                path:"appointments/",
                name:"patient-appointments",
                component:appointmentsPage
            }
        ]},
        

    ]
})
export default router