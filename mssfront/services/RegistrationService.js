import RequestService from "./base/RequestService"
class RegistrationService extends RequestService {
    async registrate(data){
        return this.post("/user/registration/",data)
    }
    async validateUser(userData){
        return await this.post("/user/validate/user/",userData)
    }
    async validateUserPersonalInfo(userPersonalInfo){
        return await this.post("/user/validate/info/",userPersonalInfo)
    }
}
export default RegistrationService