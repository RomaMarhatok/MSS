<script setup>
import documentsPageHeader from '@/components/headers/pageHeader.vue';
import documentPageNavBar from '@/components/navbars/pageNavBar.vue';
import documentListSection from '@/components/sections/userPages/documentPage/documentListSection.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { ref, onMounted, computed } from 'vue';
const store = useStore()
const route = useRoute()
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)
const activeLinks = ref([true, false, false])

onMounted(() => {
    store.dispatch("user/fetchUserDocuments", slug.value)
    store.dispatch("user/fetchDocumentTypes")

})
</script>
<template>
    <div>
        <documentsPageHeader />
        <documentPageNavBar :activeLinks="activeLinks" />
        <documentListSection />
    </div>
</template>