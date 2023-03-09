import homePage from "../pages/homePage"
import registrationPage from "../pages/registrationPage"
import authenticationPage from "../pages/authenticationPage"
import documentsPage from '../pages/user/documents/documentsListPage'
import personalInfoPage from "../pages/user/personalInfoPage"  
import singleDocumentPage from "../pages/user/documents/singleDocumentPage"
import doctorsListPage from "../pages/user/doctors/doctorsListPage" 
import doctorSinglePage from "../pages/user/doctors/singleDoctorPage"
import appointmentsPage from "../pages/user/appointments/appointmentsPage"
import LogOutPage from "../pages/logOutPage"

const routes = [
    {path:"/logout/",name:"logut page",component:LogOutPage},
    {path:"/",name:"site-home-page",component:homePage},
    {path:"/registration/",name:"registration-page",component:registrationPage},
    {path:"/authentication/",name:"authentication-page",component:authenticationPage},
    {path:"/doctors/",name:"doctors-list-page",component:doctorsListPage},
    {path:"/doctor/:doctorSlug",name:"doctor-sing-display-section",component:doctorSinglePage},
    {path:"/home/",children:[
        {
            path:"",
            name:"patient-profile-page",
            component:personalInfoPage
        },
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
            path:"appointments/",
            name:"patient-appointments",
            component:appointmentsPage
        }
    ]},
]
export default routes

