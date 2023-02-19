import RequestService from "./base/RequestService"
class UserService extends RequestService {
    async getUserPersonalInfo(slug,cb,errorCb){
        return await this.post(`/mss/user/${slug}/profile/`).then(response=>{
            cb(response.data)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getUserDocuments(slug,cb,errorCb){
        return await this.get(`/mss/user/${slug}/documents/`).then(response=>{
            cb(response.data.user_documents)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getAllDocumentTypes(cb,errorCb){
        return await this.get(`/mss/documents/types/`).then(response=>{
            cb(response.data.document_types)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getAllAppointments(userSlug,cb,errorCb){
        return await this.get(`/mss/appointments/${userSlug}/`).then(response=>{
            cb(response.data.user_appointments)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async createAppointments(cb,errorCb,data){
        return await this.post(`/mss/appointments/create/`,data).then(response=>{
            console.log(response.status)
            cb(response.status,response.data.appointments)
        }).catch(error=>{
            errorCb(error.response.status,error.response.data.errors??{})
        })
    }
    async destroyAppointments(cb,errorCb,data){
        return await this.post(`mss/appointments/desctroy/`,data).then(response=>{
            cb(response.data)
        }).catch(error=>{
            errorCb(error)
        })
    }
}
export default UserService