import AppointmentService from "@/../services/AppointmentService"
const appointmentService = new AppointmentService()
const state = {
    appointments:[],
    errors:[]
}

const getters = {
    getAllAppointmentsForCalendar:(state)=>{
            console.log("getters getAllAppointmentsForCalendar",state.appointments)
            let calendarAppointments = state.appointments.map((appointment)=>{
                    return {
                        highlight: true,  // Boolean, String, Object
                        dates:new Date(appointment.date),
                        popover:{
                            label:`appointments to ${appointment.doctor_specialization.name}`
                        }
                    }            
            })
            console.log(calendarAppointments)
            return calendarAppointments
        },
        getAppointments:(state)=>{
            console.log(state.appointments)
            return state.appointments
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