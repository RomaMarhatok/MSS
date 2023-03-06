<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import AccordionTab from 'primevue/accordiontab';
import Accordion from 'primevue/accordion';
import Timeline from 'primevue/timeline'
import Card from 'primevue/card';
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
const store = useStore()
const getTreatmentsHistory = computed(() => {
    return store.getters["treatments/getTreatmentsHistories"]
})
console.log(getTreatmentsHistory.value)
const currentAppointment = computed(() => store.state.treatments.selectedAppointment)
</script>
<template>
    <main class="flex w-full p-6 flex-col">
        <div>
            Patient {{ currentAppointment.patient.user.full_name }}
        </div>
        <div v-for="(treatment, index) in getTreatmentsHistory" :key="index">
            <Accordion>
                <AccordionTab>
                    <template #header>
                        <div>
                            {{ treatment.created_at }}
                        </div>
                    </template>
                    <Timeline :value="getTreatmentsHistory" :align="'alternate'">
                        <template #content="slotProps">
                            <Card>
                                {{ slotProps }}
                            </Card>
                        </template>

                    </Timeline>
                </AccordionTab>
            </Accordion>
        </div>
    </main>
</template>
<style lang="css">
.p-scrollpanel-bar {
    background-color: #3B82F6;
    opacity: 1;
    transition: background-color .2s;


}

.p-scrollpanel-bar:hover {
    background-color: #007ad9;
}

.scroll-panel {
    height: 300px;
}
</style>