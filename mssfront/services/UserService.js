import RequestService from "./base/RequestService"
class UserService extends RequestService {
    async getUserPersonalInfo(slug){
        return await this.post(`/mss/user/${slug}/profile/`)
    }
    async getUserDocuments(slug){
        return await this.get(`/mss/user/${slug}/documents/`)
    }
}
export default UserService