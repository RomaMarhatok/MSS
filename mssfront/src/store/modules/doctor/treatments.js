import TreatmentHistoryService from "@/../services/TreatmentHistoryService";
const treatmentHistoryService = new TreatmentHistoryService()
const state = {
    patientInfo:{},
    treatmentHistories:[]
}
const getters = {
    getTreatmentsHistories:(state)=>{
        return state.treatmentHistories
    },
    getPatientInfo:(state)=>{
        console.log(state.patientInfo)
        return state.patientInfo
    }
}
const actions = {
    async fetchTreatments({commit},{patientSlug,doctorSpecializationSlug}){
        console.log(patientSlug,doctorSpecializationSlug)
        await treatmentHistoryService.getTreatmentHistoriesForDoctor(
            (treatmentHistory,patientInfo) =>{
                commit("setTreatmentHistory",treatmentHistory)
                commit("setPatientInfo",patientInfo)
            }
                ,
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
    },
    setPatientInfo:(state,patientInfo)=>{
        console.log("mutations setPatient",patientInfo)
        state.patientInfo = patientInfo
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}