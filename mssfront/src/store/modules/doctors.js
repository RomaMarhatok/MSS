import DoctorService from "@/../services/DoctorService"
const state = {
    doctors:[],
    doctorTypes:[],
}

const getters = {
    getDoctorBySlug:(state)=>(slug)=>{
        return state.doctors.filter(doctor=>doctor.doctor_slug === slug)[0]
    },
    getDoctorsByString:(state)=>(searchString)=>{
        console.log("getters searchString",searchString)
        return state.doctors.filter(doctor => doctor.personal_info.full_name.toLowerCase().includes(searchString.toLowerCase()))
    },
    getDoctorByDoctorTypes:(state)=>(doctorType)=>{
        return state.doctors.filter(doctor=>doctor.doctor_types.some(dt=>dt.slug==doctorType.slug))
    }
}

const actions = {
    async fetchAllDoctors({commit, state}){
        const doctorService = new DoctorService()
        await doctorService.getAllDoctors(
            doctors=>{
                console.log("cb",doctors)
                commit("setDoctors",doctors)
            },
            error=>console.log(error)
            )
        console.log("action doctors",state.doctors)
    },
    async fetchAllDoctorTypes({commit,state}){
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