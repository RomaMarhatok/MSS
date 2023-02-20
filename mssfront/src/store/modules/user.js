import UserService from "@/../services/UserService"
import getBaseApi from "@/apis/baseApi"
const state = {
    slug:"",
    role:"",
    personalInfo:{},
}

const getters = {
    getHealthInfo:(state)=>{
        return  [
            {
                label: "Email",
                text: state.personalInfo.email
            },
            {
                label: "Age",
                text: state.personalInfo.age
            },
            {
                label: "Gender",
                text: state.personalInfo.gender
            },
            {
                label: "Health status",
                text: state.personalInfo.health_status
            }
        ]
    },
    getPersonalInfo:(state,getters)=>{
        return {
            image:getters.getImage,
            full_name:state.personalInfo.full_name,
            location:state.personalInfo.location,
            address:state.personalInfo.address,
        }
    },
    getImage:(state)=>{
        return state.personalInfo.image ? getBaseApi.getUri()+state.personalInfo.image:undefined
    },
}

const actions = {
    async fetchUserPersonalInfo({commit,state},slug){
        if(Object.keys(state.personalInfo).length == 0){
            const userService = new UserService()
            await userService.getUserPersonalInfo(
                    slug,
                    personalInfo=>commit("setPersonalInfo",personalInfo),
                    error=>console.log(error)
                )
            console.log("action personal info",state.personalInfo)
        }
        else{
            console.log("action without request",state.personalInfo)
        }
    },
}

const mutations = {
    setSlug:( state, slug )=>{
        console.log("mutation user slug",slug)
        state.slug = slug
    },
    setRole:( state, role )=>{
        console.log("mutation user role",role)
        state.role = role
    },
    setPersonalInfo:(state, personalInfo)=>{
        console.log("mutation user personal info",personalInfo)
        state.personalInfo = personalInfo
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}