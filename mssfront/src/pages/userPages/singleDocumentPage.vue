<script setup>
import { reactive, onMounted, ref } from 'vue';
import UserService from '@/../services/UserService';
import baseLink from '@/components/links/Base/baseLink.vue';
import { useRoute } from 'vue-router';
const document = reactive({
    document_name: "",
    document_type: "",
    doctor_name: "",
    content: "",
    created_at: "",
    updated_at: "",
})
const route = useRoute()
const redirectHref = ref(`#/user/${route.params.userSlug}/documents/`)
onMounted(() => {
    const userService = ref(new UserService())
    const userSlug = route.params.userSlug
    const documentSlug = route.params.documentSlug
    userService.value.getUserDocument(userSlug, documentSlug).then(response => {
        console.log(response)

        const userDocument = response.data.user_document
        const doctorCreator = response.data.doctor_creator
        document.document_name = userDocument.name
        document.document_type = userDocument.document_type.name
        document.doctor_name = getFullName(doctorCreator)
        document.content = userDocument.content
        document.created_at = "created at " + getFullDate(userDocument.created_at)
        document.updated_at = "updated at " + getFullDate(userDocument.updated_at)
    }).then(error => {
        console.log(error)
    })
})
function getFullDate(dateString) {
    const date = new Date(dateString)
    const dd = date.getDate()
    const mm = date.getMonth()
    const yyyy = date.getFullYear()
    return dd + "/" + mm + "/" + yyyy
}
function getFullName(doctorData) {
    return "creator " + doctorData.first_name + " " + doctorData.second_name + " " + (doctorData.patronymic ?? "")
}
</script>
<template>
    <div class="main">
        <div class="main-container">
            <div class="document-header">
                <div class="content-container">
                    <div class="header-container">
                        <p>{{ document.document_type }}</p>
                        <p>{{ document.document_name }}</p>
                    </div>
                    <p>{{ document.doctor_name }}</p>
                    <p>{{ document.updated_at }}</p>
                    <p>{{ document.created_at }}</p>
                </div>
            </div>
            <div class="main">
                <p>{{ document.content }}</p>
            </div>
            <baseLink :text="'Back'" :href="redirectHref" />
        </div>

    </div>
</template>
<style scoped>
.main {
    display: flex;
    justify-content: center;
    padding: 2rem;
}

.main-container {
    display: flex;
    flex-direction: column;
    box-shadow: 0px 0px 8px 0px rgba(34, 60, 80, 0.2);
    background-color: white;
    margin-top: 10px;
    margin-bottom: 10px;
    width: 80%;
}

.document-header {
    border-radius: 10px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    word-break: break-all;
    padding-top: 1rem;
}

.content-container {
    display: flex;
    flex-direction: column;
    padding-left: 20px;
    width: 100%;

}

.header-container {
    display: flex;
    width: 100%;
    justify-content: center;
    gap: 1rem;
}

.content {
    border-radius: 10px;
    padding: 20px;
    margin-top: 10px;
    text-align: justify;
}
</style>