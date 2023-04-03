import RequestService from "./base/RequestService";

class DocumentService extends RequestService{
    async getDocuments(slug,cb,errorCb){
        return await this.get(`/document/documents/${slug}/`).then(response=>{
            console.log(response.data.user_documents)
            cb(response.status,response.data.user_documents)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getDocumentTypes(cb,errorCb){
        return await this.get(`/document/documents/types/`).then(response=>{
            cb(response.data.document_types)
        }).catch(error=>{
            errorCb(error)
        })
    }
}

export default DocumentService