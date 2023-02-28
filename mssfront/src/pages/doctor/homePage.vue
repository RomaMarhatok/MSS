<script setup>
import PageHeader from '@/components/layout/Headers/PageHeader.vue';
import AppointmentsListSection from '@/components/ui/Sections/DoctorPage/AppointmentsListSection.vue';
import TreatmentHistoryListSection from '@/components/ui/Sections/DoctorPage/TreatmentHistoryListSection.vue';
import { onBeforeMount } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
onBeforeMount(() => {
    store.dispatch("doctorAppointments/fetchAppointments", store.state.user.slug)
})
</script>
<template>
    <div class="flex flex-col">
        <PageHeader></PageHeader>
        <div class="flex flex-row m-2 gap-5">
            <AppointmentsListSection></AppointmentsListSection>
            <TreatmentHistoryListSection></TreatmentHistoryListSection>
        </div>
    </div>
</template>
<style lang="css"></style>