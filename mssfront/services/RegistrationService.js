import RequestService from "./base/RequestService"
class RegistrationService extends RequestService {
    async registerUser(userData,cb,errorCb){
        return await this.post("/mss/auth/registration/",userData).then(response=>{
            cb(response.status,response.data.message)
        }).catch(error=>{
            console.log("Registration error",error)
            errorCb(error.response.data.errors)
        })
    }
}
export default RegistrationService