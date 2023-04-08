import UserService from "@/../services/UserService"
const userService = new UserService()

const state = {
    slug:"",
    role:"",
    personalInfo:{},
}

const getters = {
    getPersonalInfo:(state)=>{
        return state.personalInfo
    },
    getRole:(state)=>{
        return state.role
    }

}

const actions = {
    async fetchUserPersonalInfo({commit,state},slug){
        if(Object.keys(state.personalInfo).length == 0){
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