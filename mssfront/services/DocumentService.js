import RequestService from "./base/RequestService";

class DocumentService extends RequestService{
    async getDocuments(slug,cb,errorCb){
        return await this.get(`/document/documents/${slug}/`).then(response=>{
            console.log(response.data.user_documents)
            cb(response.data.user_documents)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getDocument(slug,document_slug){
        return await this.get(`/document/document/${slug}/${document_slug}/`)
    }
    async getDocumentTypes(cb,errorCb){
        return await this.get(`/document/documents/types/`).then(response=>{
            cb(response.data.document_types)
        }).catch(error=>{
            errorCb(error)
        })
    }
    async getNewestDocument(slug,cb,errorCb){
        return await this.get(`/document/new/${slug}/`).then(response=>
            cb(response.data.user_documents)
            ).catch(error=>errorCb(error))
    }
}

export default DocumentService