import RequestService from "./base/RequestService";

class AppointmentService extends RequestService{
    async getAppointmentsForUser(userSlug,cb,errorCb){
        return await this.get(`/mss/appointments/${userSlug}/`).then(response=>{
            console.log("get appointemnts",response.data.user_appointments)
            console.log(response)
            cb(response.data.user_appointments)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getAppointmentsForDoctor(userSlug,cb,errorCb){
        return await this.get(`/mss/doctor/appointments/${userSlug}/`).then(response=>{
            console.log(response)
            cb(response.data.doctor_appointments)
        }).catch(errors=>errorCb(errors))
    }
    async createAppointments(cb,errorCb,data){
        return await this.post(`/mss/appointments/create/`,data).then(response=>{
            cb(response.status,response.data.appointment)
        }).catch(error=>{
            errorCb(error.response.status,error.response.data.errors??{})
        })
    }
    async destroyAppointments(cb,errorCb,data){
        return await this.post(`mss/appointments/desctroy/`,data).then(response=>{
            cb(response.data)
        }).catch(error=>{
            errorCb(error)
        })
    }
}

export default AppointmentService