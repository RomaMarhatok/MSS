import UserService from "@/../services/UserService"
const userService = new UserService()
const state = {
    patients:[],
}
const getters = {
    getPatients:(state)=>{
        return state.patients
    }
}

const actions = {
    async fetchPatients({commit,state}){
        await userService.getPatients(
            patients=>commit("setPatients",patients),
            error=>console.log(error)
        )
        console.log("actions patients",state.patients)
    },
}
const mutations = {
    setPatients:( state, patients )=>{
        console.log("mutation patients",patients)
        state.patients = patients
    },
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}