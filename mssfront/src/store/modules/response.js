const state = {
    status:200,
    errors:{},
}

const getters = {
    responseStatus:(state)=>state.status,
    generalErrors:(state)=>state.errors.general ?? [],
    loginErrors:(state)=>state.errors.login ?? [],
    passwordErrors:(state)=>state.errors.password ?? [],
    firstNameErrors:(state)=>state.errors.first_name ?? [],
    secondNameErrors:(state)=>state.errors.second_name ?? [],
}

const actions = {
    async resetStatus({commit}){
        commit("setStatus",200)
    },
    async resetErrors({commit}){
        commit("setErrors",{})
    }
}

const mutations = {
    setStatus:(state,status)=>{
        state.status =status
    },
    setErrors:(state, errors)=>{
        state.errors = errors
        console.log("mutation response errors",state.errors)
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}