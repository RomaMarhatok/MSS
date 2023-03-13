import {createRouter,createWebHashHistory} from "vue-router";
import store from "./src/store/index"
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
import ROLES from "./roles/roles"
const routes = [
    {
        path:"/logout/",
        name:"logut page",
        component:LogOutPage,
        meta:{authorize:[]}
    },
    {
        path:"/",
        name:"site-home-page",
        component:homePage
    },
    {
        path:"/registration/",
        name:"registration-page",
        component:registrationPage
    },
    {
        path:"/authentication/",
        name:"authentication-page",
        component:authenticationPage
    },
    {
        path:"/doctors/",
        name:"doctors-list-page",
        component:doctorsListPage,
        meta:{authorize:[ROLES.Patient]}
    },
    {
        path:"/doctor/:doctorSlug",
        name:"doctor-sing-display-section",
        component:doctorSinglePage,
        meta:{authorize:[ROLES.Patient]}
    },
    {
        path:"/home/",
        meta:{authorize:[ROLES.Patient]},
        children:[
            {
                path:"",
                name:"profile-page",
                component:()=>store.state.user.role == ROLES.Patient?personalInfoPage:doctorHomePage,
                meta:{authorize:[ROLES.Patient]},
            },
            {
                path:"documents/",
                name:"patuent-documents-page",
                component:documentsPage,
                meta:{authorize:[ROLES.Patient]},
            },
            {
                path:"document/:documentSlug/",
                name:"single-patuent-document-page",
                component:singleDocumentPage,
                meta:{authorize:[ROLES.Patient]},
            },
            
            {
                path:"appointments/",
                name:"patient-appointments",
                component:appointmentsPage,
                meta:{authorize:[ROLES.Patient]},
            }
        ]
    },
    {
        path:"/appointment/",
        meta:{authorize:[ROLES.Doctor]},
        name:"single-appointment",
        component:singleAppointmentPage
    },
    {
        path:"/editor/",
        meta:{authorize:[ROLES.Doctor]},
        name:"editor",component:EditorPage
    },
    {
        path:"/nopermission/",
        name:"no-permission-page",
        component:noPermissionPage
    },
]
const router = createRouter({
    history:createWebHashHistory(),
    routes:routes
})
router.beforeEach((to,from,next)=>{
    const { authorize } = to.meta
    if(authorize){
        if(authorize.length && authorize.includes(store.state.user.role)){
            next()
        }
        else{
            next("/nopermission/")
        }
    }
    else{
        next()
    }
})
export default router
