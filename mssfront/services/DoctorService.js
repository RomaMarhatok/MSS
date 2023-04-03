import RequestService from "./base/RequestService"
class DoctorService extends RequestService {
    async getAllDoctors(cb,errorCb){
        return await this.get(`/doctor/list/`).then(response=>{
            cb(response.data.doctors)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getAllDoctorTypes(cb,errorCb){
        return await this.get(`/doctor/doctors/specializations/`).then(response=>{
            console.log("doctor types",response)
            cb(response.data.doctor_types)
        }).catch((error)=>{
            errorCb(error)
        })
    }
    async getAppointmentsForDoctor(cb,errorCb,doctor_slug){
        return await this.get(`/appointments/doctor/appointments/${doctor_slug}/`).then(response=>{
                console.log(response)
                cb(response.data.doctor_appointments)
            }
        ).error(error=>errorCb(error))
    }
}
export default DoctorService