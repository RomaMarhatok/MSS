import RequestService from "./base/RequestService"
class CountryService extends RequestService {
    async getCities(){
        return await this.get(`/user/cities/`)
    }
}
export default CountryService