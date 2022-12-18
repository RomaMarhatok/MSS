import axios from "axios";

const getBaseApi = axios.create({
    baseURL:"http://127.0.0.1:8000",
    timeout:2000
})
getBaseApi.interceptors.request.use(function(config){
    console.log("authorization interceptors")
    const token = localStorage.getItem("auth_token")
    console.log(`auth token ${token}`)
    config.headers.Authorization = `Token ${token}`
    return config
})
export default getBaseApi