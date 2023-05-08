import axios from "axios";

const getBaseApi = axios.create({
    baseURL:"http://127.0.0.1:8000",
    timeout:5000
})
getBaseApi.interceptors.request.use(function(config){
    console.log("authorization interceptors")
    const token = localStorage.getItem("auth_token")
    config.headers.Authorization = `Token ${token}`
    return config
})
export default getBaseApi