<script setup>
import { onBeforeMount, computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
// import AppointmentForm from '@/components/ui/Forms/AppointmentForm.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue'
import BodyLayout from '@/components/layout/BodyLayout.vue'
import PageHeader from '@/components/ui/Headers/PageHeader.vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
import Button from 'primevue/button';
const store = useStore()
const route = useRoute()
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)
const appointments = computed(() => store.getters["appointments/getAppointments"])
onBeforeMount(() => {
    store.dispatch("appointments/fetchAppointments", slug.value)
    store.dispatch("doctors/fetchAllDoctors")
    store.dispatch("doctors/fetchAllDoctorTypes")

})
</script>
<template>
    <HeaderLayout>
        <PageHeader />
        <TabMenu />
    </HeaderLayout>
    <BodyLayout>
        <section class="appointment-list">
            <div v-for="(appointment, index) in appointments" :key="index" class="appointment-item">
                <p>
                    {{ appointment.text }}
                </p>
                <p>
                    {{ appointment.label }}
                </p>
                <div v-if="appointment.is_cancelable">
                    <Button :label="'Cancel'"></Button>
                </div>
            </div>
        </section>
    </BodyLayout>
    <!-- <AppointmentForm></AppointmentForm> -->
</template>
<style scoped>
.appointment-list {
    padding: 1rem;
    background-color: #f8f9fa;
}

.appointment-item {
    display: flex;
    flex-direction: row;
}
</style>