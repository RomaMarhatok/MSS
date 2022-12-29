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
    async getUserDocument(userSlug,documentSlug){
        return await this.get(`/mss/user/${userSlug}/document/${documentSlug}/`)
    }
}
export default UserService