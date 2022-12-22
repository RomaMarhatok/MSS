import RequestService from "./base/RequestService"
class DoctorService extends RequestService {
    async getAllDoctors(){
        return await this.get(`/mss/doctors/`)
    }
}
export default DoctorService