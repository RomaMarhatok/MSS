import AppointmentService from "@/../services/AppointmentService"
const appointmentService = new AppointmentService()
const state = {
    appointments:[]
}

const getters = {
    getAppointments:(state)=>{
        return state.appointments
    },
    getRecentAppointments:(state)=>{
        console.log("getters getRecentAppointments",state.appointments)
        let recentAppointments = state.appointments.map(appointment=>{
            // date example "23/8/2006 10:28"
            console.log(appointment)

            let [days,months,years] = appointment.date.split(" ")[0].split("/")
            let [hours,minutes] = appointment.date.split(" ")[1].split(":")
            let date = new Date(years,months-1,days,hours,minutes)
            console.log(date)
            // let currentDate = new Date()
            // let dateDifference = Math.abs(date - currentDate)
            // let diffDays = Math.ceil(dateDifference / (1000 * 60 * 60 * 24)); 
            // if(diffDays <= 10000000) {
            return {
                label:`date: ${appointment.date.split(" ")[0]} time: ${appointment.date.split(" ")[1]}`,
                text:`appointments to ${appointment.doctor_specialization.name}`,
            }
            // }
        })
        return recentAppointments
    }
}

const actions = {
    async fetchAppointments({commit,state},slug){
        await appointmentService.getAppointmentsForDoctor(
            slug,
            appointments=>commit("setAppointments",appointments),
            error=>console.log(error)
        )
        console.log(state.appointments)
    },
    async fetchDestroyAppointemtns(data){
        await appointmentService.destroyAppointments(
            appointments=>console.log(appointments),
            error=>console.log(error),
            data
        )
        console.log("action destroy appointments",state.appointments)
    },
}

const mutations = {
    setAppointments:(state,appointments)=>{
        console.log("mutation appointments",appointments)
        state.appointments = appointments
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}