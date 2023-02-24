<script setup>
import PageHeader from '@/components/layout/Headers/PageHeader.vue';
import PageNavBar from '@/components/layout/Navbars/PageNavBar.vue';
import DocumentList from '@/components/ui/Sections/UserPages/DocumentPage/ListSection.vue'
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { ref, onMounted, computed } from 'vue';
const store = useStore()
const route = useRoute()
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)
const activeLinks = ref([true, false, false])

onMounted(() => {
    store.dispatch("documents/fetchDocuments", slug.value)
    store.dispatch("documents/fetchDocumentsTypes")
})
</script>
<template>
    <div>
        <PageHeader />
        <PageNavBar :activeLinks="activeLinks" />
        <DocumentList />
    </div>
</template>