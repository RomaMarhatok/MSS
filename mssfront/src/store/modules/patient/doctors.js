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
    getDoctorTypes:(state)=>{
        return state.doctorTypes
    },
    getAllDoctors:(state)=>{
        return state.doctors
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
            doctorTypes=>commit("setDoctorType",doctorTypes),
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