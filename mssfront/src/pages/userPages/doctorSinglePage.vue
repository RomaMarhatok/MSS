<script setup>
import doctorsPageHeader from '@/components/headers/pageHeader.vue';
import doctorImageSection from '@/components/sections/userPages/doctorsPage/doctorImageSection.vue';
// import doctorDataSection from '@/components/sections/userPages/doctorsPage/doctorDataSection.vue';
import DoctorService from '@/../services/DoctorService';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()
const doctorService = ref(new DoctorService())
const fullName = ref("")
const image = ref("")
onMounted(() => {
    const doctorSlug = route.params.doctorSlug
    doctorService.value.getDoctorBySlug(doctorSlug).then((response) => {
        console.log(response)
        fullName.value = response.data.personal_info.full_name
        image.value = response.data.personal_info.image
    }).catch((error) => console.log(error))

})
</script>
<template>
    <div>
        <doctorsPageHeader />
        <doctorImageSection :fullName="fullName" :image="image" />
        <!-- <doctorDataSection /> -->
    </div>
</template>