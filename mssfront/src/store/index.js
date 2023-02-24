import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import authentication from './modules/authentication'
import registration from './modules/registration'
import user from './modules/user'
import doctors from './modules/doctors'
import response from './modules/response'
import documents from './modules/documents'
import appointments from './modules/appointments'
const store = createStore({
    modules:{
        registration,
        authentication,
        user,
        doctors,
        response,
        documents,
        appointments,
    },
     plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
})
export default store