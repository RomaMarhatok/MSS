import RequestService from "./base/RequestService"
class DoctorService extends RequestService {
    async getAllDoctors(){
        return await this.get(`/mss/doctors/`)
    }

    async getDoctorBySlug(slug){
        return await this.get(`/mss/doctor/${slug}/`)
    }
}
export default DoctorService