
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
        console.log("set mutation authentication",errors)
        state.errors = errors
    },
    addError:(state,error)=>{
        console.log("add mutation authentication",error)
        if(state.errors.indexOf(error)==-1){
            state.errors.push(error)
        }
    },
    clearErrors:(state)=>{
        console.log("clear mutation authentication")
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