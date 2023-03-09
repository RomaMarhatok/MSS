import TreatmentHistoryService from "@/../services/TreatmentHistoryService";
const treatmentHistoryService = new TreatmentHistoryService()
const state = {
    treatmentHistories:[]
}
const getters = {
    getTreatmentsHistories:(state)=>{
        //TODO sort by date
        return state.treatmentHistories??[]
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
        console.log("action fetchTreatments",state.treatmentHistories)
    }
}
const mutations = {
    setTreatmentHistory:(state,treatmentHistories)=>{
        console.log("mutations setTreatmentHistory",treatmentHistories)
        state.treatmentHistories = treatmentHistories
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}