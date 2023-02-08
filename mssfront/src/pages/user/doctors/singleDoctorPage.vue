<script setup>
import doctorsPageHeader from '@/components/layout//Headers/PageHeader.vue';
import doctorImageSection from '@/components/ui/Sections/UserPages/DoctorsPage/ImageSection.vue'
import doctorDataSection from '@/components/ui/Sections/UserPages/DoctorsPage/DataSection.vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
const route = useRoute()
const store = useStore()
const doctorSlug = route.params.doctorSlug
const doctor = computed(() => store.getters["doctors/getDoctorBySlug"](doctorSlug))
</script>
<template>
    <div>
        <doctorsPageHeader />
        <main class="main-data-section">
            <div>
                <doctorImageSection :fullName="doctor.personal_info.full_name" :image="doctor.personal_info.image" />
            </div>
            <doctorDataSection :sectionTitle="'Resume'" :sectionText="doctor.doctor_summary.summary" />
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