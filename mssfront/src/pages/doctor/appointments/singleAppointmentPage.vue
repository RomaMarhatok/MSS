<script setup>
import AppointmentsSingleSection from '@/components/ui/Sections/DoctorPage/Appointments/AppointmentsSingleSection.vue';
import { onBeforeMount } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
onBeforeMount(() => {
    store.dispatch("treatments/fetchTreatments",
        {
            patientSlug: store.state.treatments.selectedAppointment.patient.user.slug,
            doctorSpecializationSlug: store.state.treatments.selectedAppointment.doctor_specialization.slug
        }
    )
})
</script>
<template>
    <AppointmentsSingleSection></AppointmentsSingleSection>
</template>