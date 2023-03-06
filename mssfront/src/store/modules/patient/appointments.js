import AppointmentService from "@/../services/AppointmentService"
const appointmentService = new AppointmentService()
const state = {
    appointments:[]
}

const getters = {
    getAllAppointmentsForCalendar:(state)=>{
            console.log("getters getAllAppointmentsForCalendar",state.appointments)
            console.log(state.appointemnts)
            let calendarAppointments = state.appointments.map((appointment,index)=>{
                    console.log(appointment)
                    let [days,months,years] = appointment.date.split(" ")[0].split("/")
                    let [hours,minutes] = appointment.date.split(" ")[1].split(":")
                    let date = new Date(years,months-1,days,hours,minutes)
                    return {
                        key:index,
                        customData:{
                            title:`appointments to ${appointment.doctor_specialization.name}`,
                            class:'bg-pink-500 text-white',
                        },
                        dates:date
                    }
                // date example "23/8/2006 10:28"
                
            })
            console.log(calendarAppointments)
            return calendarAppointments
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
                let currentDate = new Date()
                let dateDifference = Math.abs(date - currentDate)
                let diffDays = Math.ceil(dateDifference / (1000 * 60 * 60 * 24)); 
                if(diffDays <= 10000000) {
                    return {
                        label:`date: ${appointment.date.split(" ")[0]} time: ${appointment.date.split(" ")[1]}`,
                        text:`appointments to ${appointment.doctor_specialization.name}`,
                    }
                }
            })
            return recentAppointments
        }
}

const actions = {
    async fetchAppointments({commit,state},slug){
        await appointmentService.getAppointmentsForUser(
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
    async fetchCreateAppointemtns({commit,rootState },data){
        await appointmentService.createAppointments( 
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
    }
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