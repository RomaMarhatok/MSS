import RequestService from "./base/RequestService"
class UserService extends RequestService {
    async getUserPersonalInfo(slug,cb,errorCb){
        return await this.get(`/user/profile/${slug}/`).then(response=>{
            cb(response.data)
        }).catch(error=>{
            errorCb(error)
        })
    }
}
export default UserService