import DocumentService from "@/../services/DocumentService"
const documentService = new DocumentService()
const state = {
    documents:[],
    documentsTypes:[],
    activeDocument:{},
    activeDocumentSlug:"",
}
const getters = {
    getDocumentBySlug:(state)=>(slug)=>{
        return state.documents.find(document=>document.slug===slug)
    },
    getDocumentByString:(state)=>(searchString)=>{
        return state.documents.filter(document=>document.name.toLowerCase().includes(searchString.toLowerCase()))
    },
    getDocumentsByDocumentType:(state)=>(documentType)=>{
        return state.documents.filter(d=>d.document_type.name === documentType.name)
    },
    getDocumentsByDocumentTypes:(state)=>(documentTypes)=>{
        return state.documents.filter(d=>documentTypes.indexOf(d.document_type.name))
    },
    getActiveDocument:(state)=>{
        return state.activeDocument
    },
    getDocuments:(state)=>{
        return state.documents
    },
    getDocumentTypes:(state)=>{
        return state.documentsTypes
    },
    getActiveDocumentSlug:(state)=>{
        return state.activeDocumentSlug
    }
}

const actions = {
    async fetchDocumentsTypes({commit,state}){
        await documentService.getDocumentTypes(
            documentsTypes=>commit("setDocumentsTypes",documentsTypes),
            error=>console.log(error)
        )
        console.log("actions documents types",state.documentsTypes)
    },
    async fetchDocuments({commit,state},slug){
        await documentService.getDoctorDocuments(
            doctor_documents=>commit("setDocuments",doctor_documents),
            error=>console.log(error),
            slug,
        )
        console.log("actions doctor documents",state.documents)
    },
    async fetchActiveDocument({commit,state},{slug,documentSlug}){
        await documentService.getDoctorDocument(slug,documentSlug).then(
            response=>{
                commit("setActiveDocument",response.data.doctor_document)
            }
        )
        console.log("actions documents",state.activeDocument)
    },
}
const mutations = {
    setActiveDocumentSlug:(state,documentSlug)=>{
        console.log("setActiveDocumentSlug",documentSlug)
        state.activeDocumentSlug = documentSlug
    },
    setDocuments:( state, documents )=>{
        console.log("mutation documents",documents)
        state.documents = documents
    },
    setDocumentsTypes:(state,documentsTypes)=>{
        console.log("mutation document types",documentsTypes)
        state.documentsTypes = documentsTypes
    },
    addDocument:(state,document)=>{
        console.log("add document",document)
        state.documents.push(document)
    },
    changeDocument:(state,document)=>{
        for (let i = 0; i < state.documents.length; i++) {
            if(state.documents[i].slug==document.slug){
                state.documents[i]=document
                break
            }
        }
    },
    deleteDocument:(state,documentSlug)=>{
        state.documents = state.documents.filter(d=>d.slug!=documentSlug)
    },
    setActiveDocument:(state,document)=>{
        console.log("set active document",document)
        state.activeDocument = document
    },
    clearActiveDocument:(state)=>{
        console.log("clear active document")
        state.activeDocument = {}
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}