<script setup>
import { reactive, onMounted, ref } from 'vue';
import UserService from '@/../services/UserService';
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
onMounted(() => {
    const userService = ref(new UserService())
    const userSlug = route.params.userSlug
    const documentSlug = route.params.documentSlug
    console.log(route.params.user_slug)
    console.log(route.params.doc_slug)
    console.log(userService)
    userService.value.getUserDocument(userSlug, documentSlug).then(response => {
        console.log(response)

        const userDocument = response.data.user_document
        const doctorCreator = response.data.doctor_creator
        document.document_name = userDocument.name
        document.document_type = userDocument.document_type.name
        document.doctor_name = doctorCreator.first_name + " " + doctorCreator.second_name + " " + (doctorCreator.patronymic ?? "")
        document.content = userDocument.content
        document.created_at = userDocument.created_at
        document.updated_at = userDocument.updated_at
    }).then(error => {
        console.log(error)
    })
})
</script>
<template>
    <div class="main">
        <div class="main-container">
            <div class="document-header">
                <div class="content-container">
                    <p>{{ document.document_name }}</p>
                    <p>{{ document.doctor_name }}</p>
                    <p>{{ document.document_type }}</p>
                    <p>{{ document.updated_at }}</p>
                    <p>{{ document.created_at }}</p>
                </div>
            </div>
            <div class="main">
                <p>{{ document.content }}</p>
            </div>
            <div class="button-container">

            </div>
        </div>

    </div>
</template>
<style scoped>
.main {
    display: flex;
    justify-content: center;
}

.main-container {
    display: flex;
    flex-direction: column;
    box-shadow: 2px 4px 10px -4px rgba(34, 60, 80, 0.2);
    background-color: white;
    font-size: 1.2em;
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
}

.content-container {
    padding-left: 20px;
}

.content {
    border-radius: 10px;
    padding: 20px;
    margin-top: 10px;
    text-align: justify;
}

.button-container {
    width: 100%;
    display: flex;
    justify-content: center;
}
</style>