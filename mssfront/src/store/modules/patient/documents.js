import DocumentService from "@/../services/DocumentService"
const documentService = new DocumentService()
const state = {
    documents:[],
    documentsTypes:[]
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
}
const actions = {
    async fetchDocuments({commit,state},slug){
        await documentService.getDocuments(
            slug,
            (status,documents)=>{
                commit("response/setStatus",status,{root:true})
                commit("setDocuments",documents)
            },
            
        )
        console.log("actions documents",state.documents)
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
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}