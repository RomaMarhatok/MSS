<script setup>
import doctorsPageHeader from '@/components/headers/pageHeader.vue';
import doctorsPageNavBar from '@/components/navbars/pageNavBar.vue';
import doctorListSection from '@/components/sections/userPages/doctorsPage/doctorListSection.vue';
import { ref } from 'vue';
const activeLinks = ref([false, false, true])
</script>
<template>
    <div class="flex flex-col gap-4">
        <doctorsPageHeader />
        <doctorsPageNavBar :activeLinks="activeLinks" />
        <doctorListSection />
    </div>
</template>