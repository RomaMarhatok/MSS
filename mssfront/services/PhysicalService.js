import RequestService from "./base/RequestService"
class PhysicalService extends RequestService {
    async getPhysicalParametersForPatient(cb,errorCb,patientSlug){
        return await this.get(`/physical/list/${patientSlug}/`)
        .then(response=>cb(response.data.physical_parameters))
        .catch(error=>errorCb(error))
    }
    async createPhysicalParameters(data){
        return await this.post(`/physical/create/`,data)
    }
}
export default PhysicalService