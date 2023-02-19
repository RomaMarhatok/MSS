import DoctorService from "@/../services/DoctorService"
const state = {
    doctors:[],
    doctorTypes:[],
}

const getters = {
    getDoctorBySlug:(state)=>(slug)=>{
        return state.doctors.find(doctor=>doctor.doctor_slug === slug)
    },
    getDoctorsByString:(state)=>(searchString)=>{
        return state.doctors.filter(doctor => doctor.personal_info.full_name.toLowerCase().includes(searchString.toLowerCase()))
    },
    getDoctorByDoctorTypes:(state)=>(doctorType)=>{
        return state.doctors.filter(doctor=>doctor.doctor_types.some(dt=>dt.slug==doctorType.slug))
    },
    getDoctorByDoctorTypeSlug:(state)=>(doctorTypeSlug)=>{
        return state.doctors.filter(doctor=>doctor.doctor_types.some(dt=>dt.slug==doctorTypeSlug))
    },
}

const actions = {
    async fetchAllDoctors({commit, state}){
        if(state.doctors.length == 0){
            const doctorService = new DoctorService()
            await doctorService.getAllDoctors(
                doctors=>{
                    console.log("cb",doctors)
                    commit("setDoctors",doctors)
                },
                error=>console.log(error)
                )
            console.log("action doctors",state.doctors)
        }
        else{
            console.log("action without request",state.doctorTypes)
        }
    },
    async fetchAllDoctorTypes({commit,state}){
        if(state.doctorTypes.length == 0){
            const doctorService = new DoctorService()
            await doctorService.getAllDoctorTypes(
                doctorTypes=>{
                    console.log("cb",doctorTypes)
                    commit("setDoctorType",doctorTypes)
                },
                error=>console.log(error)
            )
            console.log("action doctor types",state.doctorTypes)
        }
        else{
            console.log("action without request",state.doctorTypes)
        }
    }
}

const mutations = {
    setDoctors:(state, doctors)=>{
        state.doctors = doctors
        console.log("mutation",state.doctors)
    },
    setDoctorType:(state, doctorTypes)=>{
        state.doctorTypes = doctorTypes
        console.log("mutation",state.doctorTypes)
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}