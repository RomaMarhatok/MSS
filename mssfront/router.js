import {createRouter,createWebHashHistory} from "vue-router";
import IndexView from "./src/view/IndexView"
import SignupView from "./src/view/SignupView"
import LoginView from "./src/view/LoginView"
import LogoutView from "./src/view/LogoutView"
import NoPermissionView from './src/view/NoPermissionView'
import VerifyAccountView from './src/view/VerifyAccountView'

import PatinetPersonalInfoVIew from "./src/view/user/PersonalInfoView"
import DocumentsListView from './src/view/user/documents/DocumentsListView'
import DocumentView from "./src/view/user/documents/DocumentView"
import DoctorListView from "./src/view/user/doctors/DoctorListView" 
import DoctorView from "./src/view/user/doctors/DoctorView"
import TreatmentHistoryList from './src/view/user/treatments/TreatmentHistoryListView'

import DoctorHomeView from './src/view/doctor/DoctorHomeView'
import DoctorAppointmentView from './src/view/doctor/appointments/AppointmentView'
import DoctorDocumentListView from './src/view/doctor/documents/DoctorDocumentListView'
import AddDocumentView from './src/view/doctor/documents/AddDocumentView'
import ChangeDocumentView from './src/view/doctor/documents/ChangeDocumentView'
import DoctorDocumentView from './src/view/doctor/documents/DocumentView'
import ROLES from "./roles/roles"
const routes = [
    {
        path:"/logout/",
        name:"logut page",
        component:LogoutView,
        meta:{authorize:[]}
    },
    {
        path:"/",
        name:"site-home-page",
        component:IndexView
    },
    {
        path:"/registration/",
        name:"registration-page",
        component:SignupView
    },
    {
        path:"/authentication/",
        name:"authentication-page",
        component:LoginView
    },
    {
        path:"/verification/:uid/:token/",
        name:"verify-page",
        component:VerifyAccountView,
    },
    {
        path:"/home/",
        meta:{authorize:[]},
        children:[
            {
                path:"",
                name:"profile-page",
                component:PatinetPersonalInfoVIew,
            },
            {
                path:"documents/",
                name:"patuent-documents-page",
                component:DocumentsListView,
                meta:{authorize:[ROLES.Patient]},
            },
            {
                path:"document/:documentSlug/",
                name:"single-patuent-document-page",
                component:DocumentView,
                meta:{authorize:[ROLES.Patient]},
            },
            {
                path:"doctors/",
                name:"doctors-list-page",
                component:DoctorListView,
                meta:{authorize:[ROLES.Patient]}
            },
            {
                path:"doctor/:doctorSlug",
                name:"doctor-sing-display-section",
                component:DoctorView,
                meta:{authorize:[ROLES.Patient]}
            },
            {
                path:'treatments/',
                name:"treatment-history-list",
                component:TreatmentHistoryList,
                meta:{authorize:[ROLES.Patient]}
            }
        ]
    },
    {
        path:"/doctor/",
        meta:{authorize:[ROLES.Doctor]},
        children:[
            {
                path:"",
                name:"doctor-home-page",
                meta:{authorize:[ROLES.Doctor]},
                component:DoctorHomeView,
            },
            {
                path:"appointment/",
                name:"doctor-appointment-page",
                component:DoctorAppointmentView,
                meta:{authorize:[ROLES.Doctor]},
            },
            {
                path:"documents/",
                name:"doctor-documents-page",
                component:DoctorDocumentListView,
                meta:{authorize:[ROLES.Doctor]},
                
            },
            {
                path:"document/",
                name:"doctor-document-page",
                component:DoctorDocumentView,
                meta:{authorize:[ROLES.Doctor]},
            },
            {
                path:"add/document/",
                name:"add-doctor-document",
                component:AddDocumentView,
                meta:{authorize:[ROLES.Doctor]},
            },
            {
                path:"change/document/",
                name:"change-doctor-document",
                component:ChangeDocumentView,
                meta:{authorize:[ROLES.Doctor]},
            }
            
        ]
    },
    {
        path:"/nopermission/",
        name:"no-permission-page",
        component:NoPermissionView
    },
]
const router = createRouter({
    history:createWebHashHistory(),
    routes:routes
})
//need much fixes
// TODO fix error with logout page
// router.beforeEach((to,from,next)=>{
//     const { authorize } = to.meta
//     if(authorize){
//         if(authorize.length && authorize.includes(store.state.user.role)){
//             next()
//         }
//         else{
//             console.log(authorize.length,authorize.includes(store.state.user.role))
//             next("/nopermission/")
//         }
//     }
//     else{
//         next()
//     }
// })
export default router
