import RequestService from "./base/RequestService";

class DocumentService extends RequestService{
    async getPatientDocuments(slug,cb,errorCb){
        return await this.get(`/document/documents/${slug}/`)
        .then(response=>cb(response.data.user_documents))
        .catch(error=>errorCb(error))
    }
    async getPatientDocument(slug,document_slug){
        return await this.get(`/document/document/${slug}/${document_slug}/`)
    }
    async getPatientNewestDocument(slug,cb,errorCb){
        return await this.get(`/document/new/${slug}/`)
        .then(response=>cb(response.data.user_documents))
        .catch(error=>errorCb(error))
    }
    async getDoctorDocuments(cb,errorCb,slug){
        return await this.get(`/document/doctor/documents/${slug}/`)
        .then(response=>cb(response.data.doctor_documents))
        .catch(error=>errorCb(error))

    }
    async getDoctorDocument(slug,documentSlug){
        return await this.get(`/document/doctor/document/${slug}/${documentSlug}/`)
    }
    async getDocumentTypes(cb,errorCb){
        return await this.get(`/document/documents/types/`)
        .then(response=>cb(response.data.document_types))
        .catch(error=>errorCb(error))
    }
    async createDocument(data){
        return await this.post(`/document/create/`,data)
    }
    async updateDocument(data){
        return await this.post(`/document/update/`,data)
    }
    async deleteDocument(data){
        return await this.post(`/document/delete/`,data)
    }
}

export default DocumentService