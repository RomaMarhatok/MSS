<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import PageHeader from '@/components/layout//Headers/PageHeader.vue';
import DataSection from '@/components/ui/Sections/UserPages/DoctorsPage/DataSection.vue';
import ImageSection from '@/components/ui/Sections/UserPages/DoctorsPage/ImageSection.vue'

const route = useRoute()
const store = useStore()
const doctorSlug = route.params.doctorSlug
const doctor = computed(() => store.getters["doctors/getDoctorBySlug"](doctorSlug))
</script>
<template>
    <div>
        <PageHeader />
        <main class="main-data-section">
            <div class="w-72">
                <ImageSection :fullName="doctor.personal_info.full_name" :image="doctor.personal_info.image" />
            </div>
            <DataSection :sectionTitle="'Resume'" :sectionText="doctor.doctor_summary.summary" />
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