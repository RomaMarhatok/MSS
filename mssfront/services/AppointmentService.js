import RequestService from "./base/RequestService";

class AppointmentService extends RequestService{
    async getPatientAppointments(userSlug,cb,errorCb){
        return await this.get(`/appointments/patient/${userSlug}/`).then(response=>{
            console.log("get appointemnts",response.data.user_appointments)
            cb(response.data.user_appointments)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getAppointmentsForDoctor(userSlug,cb,errorCb){
        return await this.get(`/appointments/doctor/appointments/${userSlug}/`).then(response=>{
            console.log(response)
            cb(response.data.doctor_appointments)
        }).catch(errors=>errorCb(errors))
    }
    async createPatientAppointments(data){
        return await this.post(`/appointments/patient/create/`,data)
    }
    async destroyPatientAppointments(cb,errorCb,data){
        return await this.post(`/appointments/patient/destroy/`,data).then(response=>{
            cb(response.data)
        }).catch(error=>{
            errorCb(error)
        })
    }
}

export default AppointmentService