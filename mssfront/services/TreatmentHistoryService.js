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
    async createTreatmentHistoryImageForAnalyze(data){
        return await this.post(`/treatment_histories/create/image/`,data)
    }
    async deleteTreatmentHistoryImageForAnalyze(data){
        return await this.post(`/treatment_histories/delete/image/`,data)
    }
    async updateTreatmentHistory(data){
        return await this.post(`/treatment_histories/update/`,data)
    }
}

export default TreatmentHistoryService