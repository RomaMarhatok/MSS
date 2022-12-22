<script setup>
import documentsPageHeader from '@/components/headers/documentsPageHeader.vue';
import documentPageNavBar from '@/components/navbars/documentPageNavBar.vue';
import documentDisplaySection from '@/components/sections/userPages/documentPage/documentDisplaySection.vue';
import UserService from '@/../services/UserService';
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
const route = useRoute()
const documents = ref([])
onMounted(() => {
    const userService = ref(new UserService())
    userService.value.getUserDocuments(route.params.userSlug).then(response => {
        documents.value = response.data.user_documents
    }).catch(error => {
        console.log(error)
    })
})
</script>
<template>
    <div>
        <documentsPageHeader />
        <documentPageNavBar />
        <documentDisplaySection :documents="documents" />
    </div>
</template>