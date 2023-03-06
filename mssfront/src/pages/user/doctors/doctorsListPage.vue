<script setup>
import { useStore } from 'vuex';
import { onBeforeMount } from 'vue';
import TabMenu from '@/components/ui/Menu/TabMenu'
import ListSection from '@/components/ui/Sections/UserPages/DoctorsPage/DoctorListSection.vue';

const store = useStore()
onBeforeMount(() => {
    store.dispatch("doctors/fetchAllDoctors")
    store.dispatch("doctors/fetchAllDoctorTypes")
})
</script>
<template>
    <TabMenu />
    <div class="flex flex-col gap-4">
        <ListSection />
    </div>
</template>