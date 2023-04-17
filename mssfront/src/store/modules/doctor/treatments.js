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
        return state.patientInfo
    },
    getTreatmentHistoryBySlug:(state)=>(slug)=>{
        state.treatmentHistories.filter(ts=>ts.slug===slug)[0]
        return state.treatmentHistories.filter(ts=>{
            return ts.treatment_history.slug==slug
        })[0]
    }
}
const actions = {
    async fetchTreatmentsHistories({commit},{patientSlug,doctorSpecializationSlug}){
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
    },
}
const mutations = {
    setTreatmentHistory:(state,treatmentHistories)=>{
        console.log("mutations setTreatmentHistory",treatmentHistories)
        state.treatmentHistories = treatmentHistories
    },
    addTreatmentHistory:(state,treatmentHistory)=>{
        console.log("mutations addTreatmentHistory",treatmentHistory)
        state.treatmentHistories.push(treatmentHistory)
    },
    setPatientInfo:(state,patientInfo)=>{
        console.log("mutations setPatient",patientInfo)
        state.patientInfo = patientInfo
    },
    updateTreatmentHistory:(state,treatmentHistory)=>{
        console.log("mutations updateTreatmentHistory",treatmentHistory)
        console.log(state.treatmentHistories)
        
        for(let tsIndex in state.treatmentHistories){
            if(state.treatmentHistories[tsIndex].treatment_history.slug == treatmentHistory.slug){
                state.treatmentHistories[tsIndex].treatment_history = treatmentHistory
            }
        }
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}