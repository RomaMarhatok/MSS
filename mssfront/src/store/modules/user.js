import UserService from "@/../services/UserService"
import getBaseApi from "@/apis/baseApi"
const state = {
    slug:"",
    role:"",
    personalInfo:{},
    documents:[],
    documentTypes:[],
    appoitnments:[],
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
    getAllAppointmentsForCalendar:(state)=>{
        console.log("getters",state.appointments)
        let calendarAppointments = state.appointments.map((appointment,index)=>{
            // date example "23/8/2006 10:28"
            let [days,months,years] = appointment.date.split(" ")[0].split("/")
            let [hours,minutes] = appointment.date.split(" ")[1].split(":")
            let date = new Date(years,months,days,hours,minutes)
            return {
                key:index,
                customData:{
                    title:`appointments to ${appointment.doctor_specialization.name}`,
                    class:'bg-pink-500 text-white',
                },
                dates:date
            }
        })
        return calendarAppointments
    },
    getRecentAppointments:(state)=>{
        console.log("getters",state.appointments)
        let recentAppointments = state.appointments.map(appointment=>{
            // date example "23/8/2006 10:28"
            let [days,months,years] = appointment.date.split(" ")[0].split("/")
            let [hours,minutes] = appointment.date.split(" ")[1].split(":")
            let date = new Date(years,months,days,hours,minutes)
            let currentDate = new Date()
            let dateDifference = Math.abs(date - currentDate)
            let diffDays = Math.ceil(dateDifference / (1000 * 60 * 60 * 24)); 
            if(diffDays <= 10000000) {
                return {
                    label:`date: ${appointment.date.split(" ")[0]} time: ${appointment.date.split(" ")[1]}`,
                    text:`appointments to ${appointment.doctor_specialization.name}`,
                }
            }
        })
        return recentAppointments
    }
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
        console.log("action without request",state.personalInfo)
    },
    async fetchUserDocuments({commit,state},slug){
        if(state.documents.length == 0){
            const userService = new UserService()
            await userService.getUserDocuments(
                    slug,
                    documents=>commit("setDocuments",documents),
                    error=>console.log(error)
                )
            console.log("action documents",state.documents)
        }
        console.log("action without request",state.documents)
    },
    async fetchDocumentTypes({commit,state}){
        if(state.documentTypes.length == 0){
            const userService = new UserService()
            await userService.getAllDocumentTypes(
                    documentTypes=>commit("setDocumentTypes",documentTypes),
                    error=>console.log(error)
                )
            console.log("action document types",state.documentTypes)
        }
        console.log("action without request",state.documentTypes)
    },
    async fetchAppointments({commit,state},slug){
        if(state.appointments.length == 0){
            const userService = new UserService()
            await userService.getAllAppointments(
                slug,
                appointments=>commit("setAppointments",appointments),
                error=>console.log(error)
            )
            console.log("action appointments",state.appointments)
        }
        console.log("action without request appointments",state.appointments)
       
    },
    async fetchDestroyAppointemtns(data){
        const userService = new UserService()
        await userService.destroyAppointments(
            appointments=>console.log(appointments),
            error=>console.log(error),
            data
        )
        console.log("action destroy appointments",state.appoitnments)
    },
    async fetchCreateAppointemtns({commit},data){
        const userService = new UserService()
        await userService.createAppointments( 
            appointment=>commit("addAppointment",appointment),
            error=>console.log(error),
            data
        )
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
    },
    setAppointments:(state,appointments)=>{
        console.log("mutation appointments",appointments)
        state.appointments = appointments
    },
    addAppointment:(state,appointment)=>{
        console.log("add appointments")
        state.appointments.push(appointment)
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}