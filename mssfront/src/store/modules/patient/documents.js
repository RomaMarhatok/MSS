import DocumentService from "@/../services/DocumentService"
const documentService = new DocumentService()
const state = {
    documents:[],
    documentsTypes:[],
    activeDocument:{},
}
const getters = {
    getDocumentBySlug:(state)=>(slug)=>{
        return state.documents.filter(document=>document.slug===slug)[0]
    },
    getDocumentByString:(state)=>(searchString)=>{
        return state.documents.filter(document=>document.name.toLowerCase().includes(searchString.toLowerCase()))
    },
    getDocumentsByDocumentType:(state)=>(documentType)=>{
        return state.documents.filter(d=>d.document_type.name === documentType.name)
    },
    getActiveDocument:(state)=>{
        return state.activeDocument
    }
}
const actions = {
    async fetchDocuments({commit,state},slug){
        await documentService.getDocuments(
            slug,
            (documents)=>{
                commit("setDocuments",documents)
            },   
        )
        console.log("actions documents",state.documents)
    },
    async fetchDocument({commit,state},{slug,document_slug}){
        await documentService.getDocument(slug,document_slug).then(
            response=>{
                commit("setActiveDocument",response.data.document)
            }
        )

        console.log("actions documents",state.activeDocument)

    },
    async fetchDocumentsTypes({commit,state}){
        await documentService.getDocumentTypes(
            documentsTypes=>commit("setDocumentsTypes",documentsTypes)
        )
        console.log("actions documents types",state.documentsTypes)
    }
}
const mutations = {
    setDocuments:( state, documents )=>{
        console.log("mutation documents",documents)
        state.documents = documents
    },
    setDocumentsTypes:(state,documentsTypes)=>{
        console.log("mutation document types",documentsTypes)
        state.documentsTypes = documentsTypes
    },
    setActiveDocument:(state,document)=>{
        console.log("set active document")
        state.activeDocument = document
    },
    clearActiveDocument:(state)=>{
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