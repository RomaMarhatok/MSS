import {createRouter,createWebHashHistory} from "vue-router";
import IndexView from "./src/view/IndexView"
import SignupView from "./src/view/SignupView"
import LoginView from "./src/view/LoginView"
import LogoutView from "./src/view/LogoutView"
import NoPermissionView from './src/view/NoPermissionView'

import PatinetPersonalInfoVIew from "./src/view/user/PersonalInfoView"
import DocumentsListView from './src/view/user/documents/DocumentsListView'
import DocumentView from "./src/view/user/documents/DocumentView"
import DoctorListView from "./src/view/user/doctors/DoctorListView" 
import DoctorView from "./src/view/user/doctors/DoctorView"
import DoctorHomeView from './src/view/doctor/DoctorHomeView'
import DoctorAppointmentView from './src/view/doctor/appointments/AppointmentView'
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
        ]
    },
    {
        path:"/doctor/",
        meta:{authorize:[ROLES.Doctor]},
        children:[
            {
                path:"",
                meta:{authorize:[ROLES.Doctor]},
                component:DoctorHomeView,
            },
            {
                path:"appointment/",
                meta:{authorize:[ROLES.Doctor]},
                component:DoctorAppointmentView,
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
