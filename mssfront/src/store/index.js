import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import authentication from './modules/authentication'
import registration from './modules/registration'
import responseErrors from './modules/responseErrors'
import user from './modules/user'
const store = createStore({
    modules:{
        registration,
        authentication,
        responseErrors,
        user,
    },
    plugins:[
        createPersistedState()
    ]
})
export default store