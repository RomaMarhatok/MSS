<script setup>
import { useStore } from 'vuex'
import { computed } from 'vue'
import Button from 'primevue/button';
const store = useStore()
const appointments = computed(() => store.getters["appointments/getRecentAppointments"])
const cancelAppointment = (appointment) => {
    const data = {
        patient_slug: store.state.user.slug,
        doctor_slug: appointment.doctor_slug,
        date: appointment.date,
    }
    console.log(data)
    store.dispatch("appointments/fetchDestroyAppointments", data)
}
</script>
<template>
    <main class="flex flex-col">
        <div v-for="(appointment, index) in appointments" :key="index">
            <p>{{ appointment.label }}</p>
            <p>{{ appointment.text }}</p>
            <Button v-if="appointment.is_cancelable" class="p-button-info"
                @click="cancelAppointment(appointment)">Cancel</Button>
        </div>
    </main>
</template>