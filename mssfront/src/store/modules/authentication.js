import AuthenticationService from "@/../services/AuthenticationService"

const state = {
    status:0,
}

const getters = {
}

const actions = {
    async authenticateUser({ commit,state }, dataFromForm){   
        const authenticationService = new AuthenticationService()
        await authenticationService.authenticateUser(
            dataFromForm,
            (slug, role, status)=>{
                commit("user/setSlug", slug, {root:true})
                commit("user/setRole", role, {root:true})
                commit("setStatus", status)
            },
            error=>commit("responseErrors/setErrors", error, { root:true })
        )
        console.log("action",state.status)
        return new Promise((resolve,reject)=>{
            resolve(state.status)
            reject(null)
        })
   }
}

const mutations = {
    setStatus:(state,status)=>(state.status = status)
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}