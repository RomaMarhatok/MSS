import RequestService from "./base/RequestService"
class UserService extends RequestService {
    async getUserPersonalInfo(slug){
        return await this.post(`/mss/user/${slug}/profile/`)
    }
}
export default UserService