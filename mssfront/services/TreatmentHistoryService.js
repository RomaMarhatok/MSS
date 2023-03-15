import RequestService from "./base/RequestService";

class TreatmentHistoryService extends RequestService{
    async getTreatmentHistoriesForDoctor(cb,errorCb,patientSlug,doctorSpecializationSlug){
        return await this.get(`/mss/patient/treatment/treatments/${patientSlug}/${doctorSpecializationSlug}/`).then(response=>{
            cb(response.data.treatment_histories,response.data.patient_info)
        }).catch(error=>errorCb(error))
    }
}

export default TreatmentHistoryService