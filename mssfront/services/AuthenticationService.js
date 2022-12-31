import RequestService from "./base/RequestService"

class AuthenticationService extends RequestService{
    async authenticateUser(userData,cb,errorCb){
        return await this.post("/mss/auth/authentication/",userData).then((response) => {
            console.log(response)
            const token = response.data.token
            localStorage.setItem("auth_token", token)
            const slug = response.data.user_slug
            const role = response.data.user_role
            const status = response.status
            cb(slug,role,status)
        }).catch(error => {
            errorCb(error.response.data.errors??{})
        })
    }
}   
export default AuthenticationService