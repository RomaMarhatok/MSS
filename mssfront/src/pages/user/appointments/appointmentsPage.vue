<script setup>
import { onBeforeMount, computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import AppointmentForm from '@/components/ui/Forms/AppointmentForm.vue';
const store = useStore()
const route = useRoute()
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)

console.log(store)
onBeforeMount(() => {
    store.dispatch("appointments/fetchAppointments", slug.value)
    store.dispatch("doctors/fetchAllDoctors")
    store.dispatch("doctors/fetchAllDoctorTypes")

})
</script>
<template>
    <AppointmentForm></AppointmentForm>
</template>