import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import authentication from './modules/authentication'
import registration from './modules/registration'
import responseErrors from './modules/responseErrors'
import user from './modules/user'
import doctors from './modules/doctors'
const store = createStore({
    modules:{
        registration,
        authentication,
        responseErrors,
        user,
        doctors,
    },
     plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
})
export default store