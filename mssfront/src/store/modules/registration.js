import RegistrationService from "@/../services/RegistrationService"

const state = {
    status:0,
    message:"",
}

const getters = {
    getMessage:(state)=>state.message
}

const actions = {
    async registrateUser({ commit,state }, dataFromForm){
        commit("setMessage","")
        const registrationService = new RegistrationService()
        await registrationService.registerUser(
            dataFromForm,
            (status,message)=>{
                commit("setStatus",status)
                commit("setMessage",message)
            },
            error=>commit("response/setErrors", error,{ root:true })
        )

        return new Promise((resolve,reject)=>{
            resolve(state.status)
            reject(null)
        })      
    },
    async resetMessage({commit}){
        commit("setMessage","")
    }
}

const mutations = {
    setMessage:(state,message)=>{
        console.log("mutation registration message",message)
        state.message=message
    },
    setStatus:(state,status)=>{
        console.log("mutation registration status",status)
        state.status = status
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}