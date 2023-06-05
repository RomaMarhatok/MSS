
const state = {
    errors:[]
}

const getters = {
    getErrors:(state)=>state.errors
}

const actions = {
}

const mutations = {
    setErrors:(state,errors)=>{
        console.log("mutation registration message",errors)
        state.errors=errors
    },
    addError:(state,error)=>{
        if(state.errors.indexOf(error)==-1){
            state.errors.push(error)
        }
    },
    clearErrors:(state)=>{
        state.errors = []
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}