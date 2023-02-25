import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import authentication from './modules/authentication'
import registration from './modules/registration'
import user from './modules/user'
import doctors from './modules/patient/doctors'
import response from './modules/response'
import documents from './modules/patient/documents'
import appointments from './modules/patient/appointments'
import doctorAppointments from './modules/doctor/doctorAppointments'
import treatments from './modules/doctor/treatments'
const store = createStore({
    modules:{
        registration,
        authentication,
        user,
        doctors,
        response,
        documents,
        appointments,
        doctorAppointments,
        treatments,
    },
     plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
})
export default store