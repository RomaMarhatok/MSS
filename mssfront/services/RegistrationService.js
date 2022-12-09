import RequestService from "./base/RequestService"
class RegistrationService extends RequestService {
    async registerUser(userData){
        return await this.post("/auth/registration/",userData)
    }
}
export default RegistrationService