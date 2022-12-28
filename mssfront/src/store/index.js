import {createStore} from 'vuex'
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
})
export default store