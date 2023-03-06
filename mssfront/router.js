import {createRouter,createWebHashHistory} from "vue-router";
// import patientRoutes from './src/routes/patientRoutes'
import doctorRoutes from './src/routes/doctorRoutes'
const router = createRouter({
    history:createWebHashHistory(),
    routes:doctorRoutes
})
export default router