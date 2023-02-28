<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex';
const store = useStore()
const appointments = computed(() => store.getters["doctorAppointments/getAppointments"])
const getTreatmentsHistory = (appointment) => store.dispatch("treatments/fetchTreatments", appointment.patient.user.slug)
</script>
<template>
    <main class="appointments-container">
        <p>Appointments</p>
        <div class="appointments-item" v-for="appointment  in appointments" :key="appointment.patient.user.slug"
            @click="getTreatmentsHistory(appointment)">
            <div>
                <div class="patient">
                    {{ appointment.patient.user.full_name }}
                </div>
                <div class="date">
                    {{ appointment.date }}
                </div>
            </div>
        </div>
    </main>
</template>
<style lang="css">
.appointments-container {
    display: flex;
    flex-direction: column;
    width: 30%;
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
    padding: 1rem;
}

.appointments-item {
    padding: 1rem;
}

.appointments-container:hover {
    cursor: pointer;
}
</style>
