import RequestService from "./base/RequestService"
class UserService extends RequestService {
    async getUserPersonalInfo(slug,cb,errorCb){
        return await this.get(`/user/profile/${slug}/`)
        .then(response=>cb(response.data))
        .catch(error=>errorCb(error))
    }
    async updateUserPersonalInfo(data){
        return await this.post(`/user/profile/update/`,data)
    }
    async getPatients(cb,errorCb){
        return await this.get("/user/patients/")
        .then(response=>cb(response.data.patients))
        .catch(error=>errorCb(error))
    }
    async verifyUser(uid,token){
        return await this.get(`user/verify/${uid}/${token}/`)
    }
    async resetPassword(data){
        return await this.post(`user/reset/`,data)
    }

}
export default UserService