import DoctorService from "@/../services/DoctorService"
const state = {
    doctors:[],
}

const getters = {
    getDoctorBySlug:(state)=>(slug)=>{
        return state.doctors.filter(doctor=>doctor.doctor_slug === slug)[0]
    },
    getDoctorsByString:(state)=>(searchString)=>{
        console.log("getters searchString",searchString)
        return state.doctors.filter(doctor => doctor.personal_info.full_name.toLowerCase().includes(searchString.toLowerCase()))
    }
}

const actions = {
    async fetchAllDoctors({commit,state}){
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
}

const mutations = {
    setDoctors:(state,doctors)=>{
        state.doctors = doctors
        console.log("mutation",state.doctors)
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}