import AppointmentService from "@/../services/AppointmentService"
const appointmentService = new AppointmentService()
const state = {
    appointments:[]
}

const getters = {
    getAllAppointmentsForCalendar:(state)=>{
            console.log("getters getAllAppointmentsForCalendar",state.appointments)
            console.log(state.appointments)
            let calendarAppointments = state.appointments.map((appointment,index)=>{
                    console.log(appointment)
                    let date = new Date(appointment.date)
                    return {
                        key:index,
                        customData:{
                            title:`appointments to ${appointment.doctor_specialization.name}`,
                            class:'bg-pink-500 text-white',
                        },
                        dates:date
                    }                
            })
            console.log(calendarAppointments)
            return calendarAppointments
        },
        getAppointments:(state)=>{
            console.log("getters getAppointments",state.appointments)
            return state.appointments.map(appointment=>{
                return {
                        label:`date: ${appointment.date}`,
                        date:appointment.date,
                        text:`appointments to ${appointment.doctor_specialization.name}`,
                        doctor_slug:appointment.doctor.user.slug,
                        is_cancelable: appointment.is_cancelable,
                    }
            })
            // .filter(appointment=>{
            //     //date example "23/8/2006 10:28"
            //     console.log(appointment)

            //     let date = new Date(appointment.date)
            //     let currentDate = new Date()
            //     let dateDifference = Math.abs(date - currentDate)
            //     let diffDays = Math.ceil(dateDifference / (1000 * 60 * 60 * 24));

            //     if(diffDays <= 1000) {
            //         console.log("if statement")
            //         return appointment
            //     }
            // })
            // console.log("recentAppointments",recentAppointments)
            // return recentAppointments
        },
}

const actions = {
    async fetchAppointments({commit,state},slug){
        await appointmentService.getPatientAppointments(
            slug,
            appointments=>commit("setAppointments",appointments),
            error=>console.log(error)
        )
        console.log(state.appointments)
    },
    async fetchDestroyAppointments({state},data){
        console.log(data)
        await appointmentService.destroyPatientAppointments(
            appointments=>console.log(appointments),
            error=>console.log(error),
            data
        )
        console.log("action destroy appointments",state.appointments)
    },
    async fetchCreateAppointemtns({commit,rootState },data){
        await appointmentService.createPatientAppointments( 
            (status,appointment)=>{
                commit("response/setStatus", status, { root:true })
                commit("addAppointment",appointment)
            },
            (status,error)=>{
                commit("response/setStatus", status, { root:true })
                commit("response/setErrors", error, { root:true })
            },
            data
        )
        return new Promise((resolve,reject)=>{
            resolve(rootState.response.status)
            reject(null)
        })
    },
}

const mutations = {
    setAppointments:(state,appointments)=>{
        console.log("mutation appointments",appointments)
        state.appointments = appointments
    },
    addAppointment:(state,appointment)=>{
        console.log("add appointments")
        state.appointments.push(appointment)
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}