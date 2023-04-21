import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import authentication from './modules/authentication'
import registration from './modules/registration'
import user from './modules/user'
import doctors from './modules/patient/doctors'
import documents from './modules/patient/documents'
import appointments from './modules/patient/appointments'
import patientTreatments from './modules/patient/patientTreatments'
import physicalParameters from './modules/patient/physicalParameters'
import doctorAppointments from './modules/doctor/doctorAppointments'
import treatments from './modules/doctor/treatments'
import appointment from './modules/doctor/appointment'
import doctorDocuments from './modules/doctor/documents'
import patients from './modules/doctor/patients'
const store = createStore({
    modules:{
        registration,
        authentication,
        user,
        doctors,
        documents,
        appointments,
        doctorAppointments,
        appointment,
        treatments,
        patientTreatments,
        doctorDocuments,
        patients,
        physicalParameters,
    },
     plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
})
export default store