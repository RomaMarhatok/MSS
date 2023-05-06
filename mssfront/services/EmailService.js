import RequestService from "./base/RequestService";

class EmailService extends RequestService{
    async sendEmail(data){
        this.post(`/user/send/email/`,data)
    }
}
export default EmailService