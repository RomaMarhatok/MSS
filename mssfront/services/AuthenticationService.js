import RequestService from "./base/RequestService"

class AuthenticationService extends RequestService{
    async authenticateUser(userData){
        return await this.post("/auth/authentication/",userData)
    }
}   
export default AuthenticationService