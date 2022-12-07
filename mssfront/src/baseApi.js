import axios from "axios";

const getBaseApi = axios.create({
    baseURL:"http://127.0.0.1:8000/mss",
    timeout:2000
})
export default getBaseApi