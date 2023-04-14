import RequestService from "./base/RequestService";

class TreatmentHistoryService extends RequestService{
    async getTreatmentHistoriesForDoctor(cb,errorCb,patientSlug,doctorSpecializationSlug){
        return await this.get(`/treatment_histories/treatments/${patientSlug}/${doctorSpecializationSlug}/`).then(response=>{
            cb(response.data.treatment_histories,response.data.patient_info)
        }).catch(error=>errorCb(error))
    }
    async createTreatmentHistory(data){
        return await this.post(`/treatment_histories/create/`,data)
    }
    async createTreatmentHistoryImageForAnalyze(cb,errorCb,data){
        return await this.post(`create/image/`,data).then(response=>cb(response)).catch(error=>errorCb(error))
    }
}

export default TreatmentHistoryService