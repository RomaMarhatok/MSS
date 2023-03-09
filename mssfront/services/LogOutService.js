import RequestService from "./base/RequestService";

class LogOutService extends RequestService{
    async LogOut(userSlug){
        this.get(`/logout/${userSlug}/`)
    }
}
export default LogOutService