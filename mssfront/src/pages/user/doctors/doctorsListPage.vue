<script setup>
import doctorsPageHeader from '@/components/headers/pageHeader.vue';
import doctorsPageNavBar from '@/components/navbars/pageNavBar.vue';
import doctorListSection from '@/components/sections/userPages/doctorsPage/doctorListSection.vue';
import { ref, onBeforeMount } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const activeLinks = ref([false, false, true])
onBeforeMount(() => {
    store.dispatch("doctors/fetchAllDoctors")
})
</script>
<template>
    <div class="flex flex-col gap-4">
        <doctorsPageHeader />
        <doctorsPageNavBar :activeLinks="activeLinks" />
        <doctorListSection />
    </div>
</template>