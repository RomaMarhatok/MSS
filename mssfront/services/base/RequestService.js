import getBaseApi from "@/apis/baseApi";
class RequestService {
    get(url,config){
        return getBaseApi.get(url,config)
    }
    post(url,data,config){
        return getBaseApi.post(url,data,config)
    }
}
export default RequestService