import RequestService from "./base/RequestService";

class EmailService extends RequestService{
    async sendEmail(data){
        return await this.post(`/user/send/email/`,data)
    }
}
export default EmailService