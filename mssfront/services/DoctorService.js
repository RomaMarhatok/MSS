import RequestService from "./base/RequestService"
class DoctorService extends RequestService {
    async getAllDoctors(cb,errorCb){
        return await this.get(`/mss/doctors/`).then(response=>{
            cb(response.data.doctors)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getAllDoctorTypes(cb,errorCb){
        return await this.get(`/mss/doctors/specializations/`).then(response=>{
            console.log("doctor types",response)
            cb(response.data.doctor_types)
        }).catch((error)=>{
            errorCb(error)
        })
    }
}
export default DoctorService