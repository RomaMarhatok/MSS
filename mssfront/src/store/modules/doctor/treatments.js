import TreatmentHistoryService from "@/../services/TreatmentHistoryService";
const treatmentHistoryService = new TreatmentHistoryService()
const state ={
    selectedAppointment:null,
    treatmentHistory:[]
}
const getters = {
    getTreatmentsHistories:(state)=>{
        //TODO sort by date
        return state.treatmentHistory??[]
    }
}
const actions = {
    async fetchTreatments({commit},{patientSlug,doctorSpecializationSlug}){
        console.log(patientSlug,doctorSpecializationSlug)
        await treatmentHistoryService.getTreatmentHistoriesForDoctor(
            treatmentHistory =>commit("setTreatmentHistory",treatmentHistory),
            error=>console.log(error),
            patientSlug,
            doctorSpecializationSlug
        )
        console.log("action fetchTreatments",state.treatmentHistory)
    }
}
const mutations = {
    setTreatmentHistory:(state,treatmentHistory)=>{
        console.log("mutations setTreatmentHistory",treatmentHistory)
        state.treatmentHistory = treatmentHistory
    },
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
    mutations,
}