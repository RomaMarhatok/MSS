import RequestService from "./base/RequestService"

class AuthenticationService extends RequestService{
    async authenticate(data){
        return await this.post("/user/authentication/",data).then(response=>{
            console.log("Authentication response",response)
            const token = response.data.token
            localStorage.setItem("auth_token", token)
            return Promise.resolve(response)
        }).catch(error=>{
            return Promise.reject(error)
        })
    }
}   
export default AuthenticationService