import axios from "axios";

const getBaseApi = axios.create({
    baseURL:"http://127.0.0.1:8000/mss",
    timeout:2000
})
getBaseApi.interceptors.request.use(function(config){
    const token = localStorage.getItem("auth_token")
    config.headers.Authorization = `Token ${token}`
    return config
})
export default getBaseApi