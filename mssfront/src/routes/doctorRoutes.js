import homePage from "../pages/homePage"
import registrationPage from "../pages/registrationPage"
import authenticationPage from "../pages/authenticationPage"
import doctorHomePage from "../pages/doctor/homePage"

const routes = [
    {path:"/",name:"site-home-page",component:homePage},
    {path:"/registration/",name:"registration-page",component:registrationPage},
    {path:"/authentication/",name:"authentication-page",component:authenticationPage},
    {path:"/home/",name:"doctors-home-page",component:doctorHomePage},
]

export default routes