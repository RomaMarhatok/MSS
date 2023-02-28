import TreatmentHistoryService from "@/../services/TreatmentHistoryService";
const treatmentHistoryService = new TreatmentHistoryService()
const state ={
    treatmentHistory:[]
}
const getters = {
    getTreatmentsHistories:(state)=>{
        return state.treatmentHistory??[]
    }
}
const actions = {
    async fetchTreatments({commit},patientSlug){
        console.log(patientSlug)
        await treatmentHistoryService.getTreatmentHistoriesForPatient(
            treatmentHistory =>commit("setTreatmentHistory",treatmentHistory),
            error=>console.log(error),
            patientSlug
        )
        console.log("action fetchTreatments",state.treatmentHistory)
    }
}
const mutations = {
    setTreatmentHistory:(state,treatmentHistory)=>{
        console.log("mutations setTreatmentHistory",treatmentHistory)
        state.treatmentHistory = treatmentHistory
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}