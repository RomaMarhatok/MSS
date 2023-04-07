import AppointmentService from "@/../services/AppointmentService"
const appointmentService = new AppointmentService()
const state = {
    appointments:[],
    errors:[]
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
        getErrors:(state)=>{
            return state.errors
        }
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
            (appointment)=>{
                commit("addAppointment",appointment)
            },
            (error)=>console.log(error),
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
    },
    addError:(state,error)=>{
        console.log("mutation appointemnts add error")
        if(state.errors.indexOf(error)==-1){
            state.errors.push()
        }
    },
    clearError:(state)=>{
        console.log("mutation appointemnts clear error")
        state.error = []
    },
    setErrors:(state,errors)=>{
        console.log("mutation appointemnts set error")
        state.errors = errors
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}