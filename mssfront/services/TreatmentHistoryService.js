import RequestService from "./base/RequestService";

class TreatmentHistoryService extends RequestService{
    async getTreatmentHistoriesForDoctor(cb,errorCb,patientSlug,doctorSpecializationSlug){
        return await this.get(`/treatment_histories/treatments/${patientSlug}/${doctorSpecializationSlug}/`).then(response=>{
            cb(response.data.treatment_histories,response.data.patient_info)
        }).catch(error=>errorCb(error))
    }
    async createTreatmentHistory(cb,errorCb){
        return await this.post(`/treatment_histories/create/`).then(response=>{
            cb(response.data.treatment_history)
        }).catch(error=>errorCb(error))
    }
}

export default TreatmentHistoryService