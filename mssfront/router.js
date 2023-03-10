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
import doctorHomePage from "./src/pages/doctor/homePage"
import noPermissionPage from './src/pages/noPermissionPage'
import singleAppointmentPage from "./src/pages/doctor/appointments/singleAppointmentPage"
import EditorPage from "./src/pages/doctor/editorPage"
import LogOutPage from "./src/pages/logOutPage"
import isPatient from "./permissions/IsPatient"
import isDoctor from "./permissions/IsDcotor"

const routes = [
    {path:"/logout/",name:"logut page",component:LogOutPage},
    {path:"/",name:"site-home-page",component:homePage},
    {path:"/registration/",name:"registration-page",component:registrationPage},
    {path:"/authentication/",name:"authentication-page",component:authenticationPage},
    {
        path:"/doctors/",
        name:"doctors-list-page",
        beforeEnter: (to, from, next) => {
            if(isPatient()){
                next()
            }
            next("/home/")
        },
        component:doctorsListPage
    },
    {path:"/doctor/:doctorSlug",name:"doctor-sing-display-section",component:doctorSinglePage},
    {path:"/home/",children:[
        {
            path:"",
            name:"profile-page",
            component:()=>{
                if(isDoctor()) {
                    return doctorHomePage
                }
                else {
                    return personalInfoPage
                }
            }
        },
        {
            path:"documents/",
            name:"patuent-documents-page",
            beforeEnter: (to, from, next) => {
                if(isPatient()){
                    next()
                }
                next("/home/")
            },
            component:documentsPage,
        },
        {
            path:"document/:documentSlug/",
            name:"single-patuent-document-page",
            beforeEnter: (to, from, next) => {
                if(isPatient()){
                    next()
                }
                next("/home/")
            },
            component:singleDocumentPage
        },
        
        {
            path:"appointments/",
            name:"patient-appointments",
            beforeEnter: (to, from, next) => {
                if(isPatient()){
                    next()
                }
                else{
                    next("/home/")
                }
            },
            component:appointmentsPage
        }
    ]},
    {
        path:"/appointment/",
        beforeEnter: (to, from, next) => {
            if(isDoctor()){
                next()
            }
            else{
                next("/nopermission/")
            }
        },
        name:"single-appointment",
        component:singleAppointmentPage
    },
    {
        path:"/editor/",
        beforeEnter: (to, from, next) => {
            if(isDoctor()){
                next()
            }
            else{
                next("/nopermission/")
            }
        },
        name:"editor",component:EditorPage},
    {path:"/nopermission/",name:"no-permission-page",component:noPermissionPage},
    
]
const router = createRouter({
    history:createWebHashHistory(),
    routes:routes
})
export default router
