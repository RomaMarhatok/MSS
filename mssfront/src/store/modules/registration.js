import RegistrationService from "@/../services/RegistrationService"

const state = {
    message:"",
}

const getters = {
}

const actions = {
    async registrateUser({ commit,state }, dataFromForm){
        commit("setMessage","")
        const registrationService = new RegistrationService()
        await registrationService.registerUser(
            dataFromForm,
            message=>{
                commit("setMessage",message)
            },
            error=>commit("responseErrors/setErrors", error,{ root:true })
        )
        return new Promise((resolve,reject)=>{
            resolve(state.message)
            reject("")
        })      
    },
    async clearAll({commit}){
        commit("setMessage","")
    }
}

const mutations = {
    setMessage:(state,message)=>{
        console.log("mutation registration",message)
        state.message=message
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}