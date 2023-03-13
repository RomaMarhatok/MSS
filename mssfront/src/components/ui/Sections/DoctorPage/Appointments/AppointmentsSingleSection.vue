<script setup>
import { computed, ref } from 'vue';
import { useStore } from 'vuex';
import AccordionTab from 'primevue/accordiontab';
import Accordion from 'primevue/accordion';
import Timeline from 'primevue/timeline'
import Card from 'primevue/card';
import DataTable from 'primevue/datatable'
import Column from 'primevue/column';
import SelectButton from 'primevue/selectbutton'
import ScrollPanel from 'primevue/scrollpanel';
import ScrollTop from 'primevue/scrolltop';
import Button from 'primevue/button';
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import { useRouter } from 'vue-router';
const store = useStore()
const router = useRouter()
const getTreatmentsHistory = computed(() => {
    return store.getters["treatments/getTreatmentsHistories"]
})
const selectButtonOptions = ref(["list", "timeline"])
const selectButtonValue = ref("list")
const currentAppointment = computed(() => store.state.appointment.selectedAppointment)
const redirect = () => router.push("/editor/")
</script>
<template>
    <main class="flex w-full p-6 flex-col">
        <div class="flex flex-row justify-between">
            <p>
                Patient {{ currentAppointment.patient.user.full_name }}
            </p>
            <Button label="create" class="p-button-info" @click="redirect"></Button>
            <SelectButton v-model="selectButtonValue" :options="selectButtonOptions" />

        </div>
        <ScrollPanel v-if="selectButtonValue == 'timeline'" class="w-full m-3 border-y-3 pt-2 scroll-panel">
            <Timeline v-if="selectButtonValue == 'timeline'" :value="getTreatmentsHistory" :align="'alternate'">
                <template #opposite="slotProps">
                    <small class="p-text-secondary">{{ slotProps.item.created_at }}</small>
                </template>
                <template #content="slotProps">
                    <Card>
                        <template #title>
                            <p class="font-bold text-base text-left">
                                {{ slotProps.item.title }}
                            </p>
                        </template>
                        <template #content>
                            <p class="text-left">
                                {{ slotProps.item.short_description }}
                            </p>
                        </template>
                    </Card>
                </template>
            </Timeline>
            <ScrollTop target="parent" :threshold="100" class="custom-scroll-top" icon="pi pi-arrow-up" />
        </ScrollPanel>

        <DataTable v-if="selectButtonValue == 'list'" :value="getTreatmentsHistory" :rows="10" :paginator="true">
            <template #empty>
                No treatment histories found found.
            </template>
            <template #loading>
                Loading patient data. Please wait.
            </template>
            <Column>
                <template #header></template>
                <template #body="{ data }">
                    <Accordion>
                        <AccordionTab>
                            <template #header>
                                <div>
                                    {{ data.created_at }}
                                </div>
                            </template>
                            <Card>
                                <template #title>
                                    <p class="font-bold text-base text-left">
                                        {{ data.title }}
                                    </p>
                                </template>
                                <template #content>
                                    <p class="text-left">
                                        {{ data.short_description }}
                                    </p>
                                </template>
                            </Card>
                        </AccordionTab>
                    </Accordion>
                </template>
            </Column>
        </DataTable>
    </main>
</template>
<style lang="css">
.p-scrollpanel .p-scrollpanel-bar {
    background-color: #3B82F6;
    opacity: 1;
    transition: background-color .2s;


}

.p-scrollpanel-bar:hover {
    background-color: #007ad9;
}

.scroll-panel {
    height: 550px;
    max-height: 550px;
}

.p-scrolltop.p-link {
    background-color: #3B82F6;

}

.p-scrolltop.p-link:hover {
    background-color: #007ad9;

}
</style>