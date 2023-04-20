const state = {
    selectedAppointment:{}
}

const getters = {
    getSelectedAppointment:(state)=>{
        return state.selectedAppointment
    }
}
const actions = {

}
const mutations = {
    setSelectedAppointment:(state,appointment)=>{
        console.log("mutations setSelectedAppointment",appointment)
        state.selectedAppointment = appointment
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}