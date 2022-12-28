const state = {
    errors:{},
}

const getters = {
    generalErrors:(state)=>state.errors.general ?? [],
    loginErrors:(state)=>state.errors.login ?? [],
    passwordErrors:(state)=>state.errors.password ?? [],
    firstNameErrors:(state)=>state.errors.first_name ?? [],
    secondNameErrors:(state)=>state.errors.second_name ?? [],
}

const actions = {
    async clearErrors({commit}){
        commit("setErrors",{})
    }
}

const mutations = {
    setErrors:(state, errors)=>{
        state.errors = errors
        console.log("mutation",state.errors)
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}