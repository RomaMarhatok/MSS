import RequestService from "./base/RequestService"

class AuthenticationService extends RequestService{
    async authenticate(userData,cb,errorCb){
        return await this.post("/user/authentication/",userData).then((response) => {
            console.log(response)
            const token = response.data.token
            localStorage.setItem("auth_token", token)
            const slug = response.data.slug
            const role = response.data.role
            const status = response.status
            cb(slug,role,status)
        }).catch(error => {
            errorCb(error.response.data.errors??{})
        })
    }
}   
export default AuthenticationService