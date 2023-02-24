import AuthenticationService from "@/../services/AuthenticationService"

const state = {}
const getters = {}

const actions = {
    async authenticate({ commit,state,rootState }, dataFromForm){   
        const authenticationService = new AuthenticationService()
        await authenticationService.authenticateUser(
            dataFromForm,
            (slug, role, status)=>{
                console.log("cb",slug,role,state)
                commit("user/setSlug", slug, {root:true})
                commit("user/setRole", role, {root:true})
                commit("response/setStatus", status,{root:true})
            },
            error=>commit("response/setErrors", error, { root:true })
        )
        return new Promise((resolve,reject)=>{
            resolve(rootState.response.status)
            reject(null)
        })
    },
}

const mutations = {
    setStatus:(state,status)=>{
        console.log("mutation authentication",status)
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