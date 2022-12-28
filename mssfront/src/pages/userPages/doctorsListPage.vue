<script setup>
import doctorsPageHeader from '@/components/headers/pageHeader.vue';
import doctorsPageNavBar from '@/components/navbars/pageNavBar.vue';
import doctorListSection from '@/components/sections/userPages/doctorsPage/doctorListSection.vue';
import DoctorService from '@/../services/DoctorService';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router'
const doctors = ref([])
const activeLinks = ref([false, false, true])
const route = useRoute()
onMounted(() => {
    const doctorService = ref(new DoctorService());
    doctorService.value.getAllDoctors().then(response => {
        doctors.value = response.data.doctors
    }).catch(error => console.log(error))
})
</script>
<template>
    <div class="flex flex-col gap-4">
        <doctorsPageHeader />
        <doctorsPageNavBar :activeLinks="activeLinks" :userSlug="route.params.userSlug" />
        <doctorListSection :doctors="doctors" />
    </div>
</template>