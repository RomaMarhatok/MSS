import RequestService from "./base/RequestService"
class UserService extends RequestService {
    async getUserPersonalInfo(slug,cb,errorCb){
        return await this.post(`/mss/user/${slug}/profile/`).then(response=>{
            cb(response.data)
        }).catch(error=>{
            errorCb(error)
        })
    }
}
export default UserService