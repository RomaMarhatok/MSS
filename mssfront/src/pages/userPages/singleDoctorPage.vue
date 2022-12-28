<script setup>
import doctorsPageHeader from '@/components/headers/pageHeader.vue';
import doctorImageSection from '@/components/sections/userPages/doctorsPage/doctorImageSection.vue';
import doctorDataSection from '@/components/sections/userPages/doctorsPage/doctorDataSection.vue';
import DoctorService from '@/../services/DoctorService';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()
const doctorService = ref(new DoctorService())
const fullName = ref("")
const image = ref("")
const summary = ref("")
onMounted(() => {
    const doctorSlug = route.params.doctorSlug
    doctorService.value.getDoctorBySlug(doctorSlug).then((response) => {
        console.log(response)
        fullName.value = response.data.personal_info.full_name
        image.value = response.data.personal_info.image
        summary.value = response.data.doctor_summary.summary
    }).catch((error) => console.log(error))

})
</script>
<template>
    <div>
        <doctorsPageHeader />
        <main class="main-data-section">
            <doctorImageSection :fullName="fullName" :image="image" />
            <doctorDataSection :sectionTitle="'Resume'" :sectionText="summary" />
        </main>

    </div>
</template>
<style scoped>
.main-data-section {
    display: flex;
    flex-direction: row;
    margin-top: 10px;
    justify-content: space-evenly;
}

@media screen and (max-width: 1100px) {
    .main-data-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin-top: 10px;
    }
}
</style>