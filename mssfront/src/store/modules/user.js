import UserService from "@/../services/UserService"
import getBaseApi from "@/apis/baseApi"
const state = {
    slug:"",
    role:"",
    personalInfo:{},
    documents:[],
    documentTypes:[],
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
    getDocumentBySlug:(state)=>(slug)=>{
        return state.documents.filter(document=>document.slug===slug)[0]
    },
    getDocumentByString:(state)=>(searchString)=>{
        return state.documents.filter(document=>document.name.toLowerCase().includes(searchString.toLowerCase()))
    },
    getDocumentsByDocumentType:(state)=>(documentType)=>{
        return state.documents.filter(d=>d.document_type.name === documentType.name)
    },
    getImage:(state)=>{
        return state.personalInfo.image ? getBaseApi.getUri()+state.personalInfo.image:undefined
    },
}

const actions = {
    async fetchUserPersonalInfo({commit,state},slug){
        const userService = new UserService()
        await userService.getUserPersonalInfo(
                slug,
                personalInfo=>commit("setPersonalInfo",personalInfo),
                error=>console.log(error)
            )
        console.log("action personal info",state.personalInfo)
    },
    async fetchUserDocuments({commit,state},slug){
        const userService = new UserService()
        await userService.getUserDocuments(
                slug,
                documents=>commit("setDocuments",documents),
                error=>console.log(error)
            )
        console.log("action documents",state.documents)
    },
    async fetchDocumentTypes({commit,state}){
        const userService = new UserService()
        await userService.getAllDocumentTypes(
                documentTypes=>commit("setDocumentTypes",documentTypes),
                error=>console.log(error)
            )
        console.log("action document types",state.documentTypes)
    }
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
    setDocuments:( state, documents )=>{
        console.log("mutation user documents",documents)
        state.documents = documents
    },
    setDocumentTypes:(state,documentTypes)=>{
        console.log("mutation document types",documentTypes)
        state.documentTypes = documentTypes
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}