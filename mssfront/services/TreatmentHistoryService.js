import RequestService from "./base/RequestService";

class TreatmentHistoryService extends RequestService{
    async getTreatmentHistoriesForPatient(cb,errorCb,patientSlug){
        return await this.get(`/mss/patient/treatment/${patientSlug}/`).then(response=>{
            cb(response.data.treatment_histories)
        }).catch(error=>errorCb(error))
    }
}

export default TreatmentHistoryService