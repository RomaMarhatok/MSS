<script setup>
import documentsPageHeader from '@/components/headers/pageHeader.vue';
import documentPageNavBar from '@/components/navbars/pageNavBar.vue';
import documentDisplaySection from '@/components/sections/userPages/documentPage/documentDisplaySection.vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { ref, onMounted, computed } from 'vue';
const store = useStore()
const route = useRoute()
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)
const activeLinks = ref([true, false, false])

onMounted(() => {
    store.dispatch("user/fetchUserDocuments", slug.value)
})
</script>
<template>
    <div>
        <documentsPageHeader />
        <documentPageNavBar :activeLinks="activeLinks" />
        <documentDisplaySection />
    </div>
</template>