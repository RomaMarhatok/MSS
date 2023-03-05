<script setup>
import { ref, computed } from 'vue'
import { useStore } from 'vuex';
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import DataView from 'primevue/dataview';
import AccordionTab from 'primevue/accordiontab';
import Accordion from 'primevue/accordion';
import Panel from 'primevue/panel'

const store = useStore()
const appointments = computed(() => store.getters["doctorAppointments/getAppointments"])
// const getTreatmentsHistory = (appointment) => {
//     store.dispatch("treatments/fetchTreatments", appointment.patient.user.slug, appointment.doctor_specialization.slug)
//     return store.getters["treatments/getTreatmentsHistories"]
// }
const layout = ref('list')
</script>
<template>
    <main class="w-full">
        <DataView :value="appointments" :paginator="true" :rows="10" :layout="layout">
            <template #list="slotProps">
                <Accordion>
                    <AccordionTab>
                        <div class="flex flex-col">
                            <p>Patient {{ slotProps.data.patient.user.full_name }}</p>
                            <div class="p-2">
                                <Panel header="Persnal info" :toggleable="true" :collapsed="true">
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                                        incididunt ut labore et dolore magna aliqua.
                                        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
                                        ex ea commodo consequat.
                                        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
                                        fugiat nulla pariatur. Excepteur sint occaecat
                                        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
                                        laborum.</p>
                                </Panel>
                            </div>
                        </div>
                    </AccordionTab>
                </Accordion>
            </template>
        </DataView>
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
