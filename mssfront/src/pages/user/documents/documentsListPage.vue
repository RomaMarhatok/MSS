<script setup>
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { onMounted, computed } from 'vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue';
import DocumentList from '@/components/ui/Sections/UserPages/DocumentPage/ListSection.vue'


const store = useStore()
const route = useRoute()
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)

onMounted(() => {
    store.dispatch("documents/fetchDocuments", slug.value)
    store.dispatch("documents/fetchDocumentsTypes")
})
</script>
<template>
    <TabMenu />

    <DocumentList />
</template>