import TreatmentHistoryService from "@/../services/TreatmentHistoryService";
const treatmentHistoryService = new TreatmentHistoryService()
const state = {
    treatmentHistories:[],
}
const getters = {
    getTreatmentsHistories:(state)=>{
        return state.treatmentHistories
    },
}
const actions = {
    async fetchTreatmentsHistories({commit},patientSlug){
        console.log(patientSlug)
        await treatmentHistoryService.getTreatmentHistoriesForPatient(
            (treatmentHistories) =>{
                commit("setTreatmentHistories",treatmentHistories)
            },
            error=>console.log(error),
            patientSlug,
        )
    },
}
const mutations = {
    setTreatmentHistories:(state,treatmentHistories)=>{
        console.log("mutations setTreatmentHistory",treatmentHistories)
        state.treatmentHistories = treatmentHistories
    },
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}