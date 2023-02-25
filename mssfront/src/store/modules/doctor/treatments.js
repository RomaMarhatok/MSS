import TreatmentHistoryService from "services/TreatmentHistoryService";
const treatmentHistoryService = new TreatmentHistoryService()
const state ={
    treatmentHistory:[]
}
const getters = {
    getTreatmentsHistories:(state)=>{
        console.log("getTreatmentsHistories",state.treatmentHistory)
        return state.treatmentHistory??[]
    }
}
const actions = {
    async fetchAppointments({commit},patientSlug){
        await treatmentHistoryService.getTreatmentHistoriesForPatient(
            treatmentHistory =>commit("setTreatmentHistory",treatmentHistory),
            error=>console.log(error),
            patientSlug
        )
        console.log("action fetchAppointments",state.treatmentHistory)
    }
}
const mutations = {
    setTreatmentHistory:(state,appointments)=>{
        console.log("mutations setTreatmentHistory",appointments)
        state.appointments = appointments
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}