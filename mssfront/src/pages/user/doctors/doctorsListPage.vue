<script setup>
import PageHeader from '@/components/layout/Headers/PageHeader.vue';
import PageNavBar from '@/components/layout/Navbars/PageNavBar.vue';
import ListSection from '@/components/ui/Sections/UserPages/DoctorsPage/DoctorListSection.vue';
import { ref, onBeforeMount } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const activeLinks = ref([false, false, true])
onBeforeMount(() => {
    store.dispatch("doctors/fetchAllDoctors")
    store.dispatch("doctors/fetchAllDoctorTypes")
})
</script>
<template>
    <div class="flex flex-col gap-4">
        <PageHeader />
        <PageNavBar :activeLinks="activeLinks" />
        <ListSection />
    </div>
</template>