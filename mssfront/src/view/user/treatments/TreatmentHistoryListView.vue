<script setup>
import { onBeforeMount, computed } from 'vue';
import { useStore } from 'vuex'
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue';
import TreatmentHistoryImageListSection from "@/components/ui/Sections/TreatmentHistoryImageListSection.vue"
import TreatmentHistoryDocumentListSection from '@/components/ui/Sections/TreatmentHistoryDocumentListSection.vue';
import Panel from 'primevue/panel';
const store = useStore()
const slug = computed(() => store.state.user.slug)
const treatmentHistories = computed(() => store.getters["patientTreatments/getTreatmentsHistories"])
const panelHeader = (ts) => {
    return "Было создано в " + ts.treatment_history.parsed_date.day + " "
        + ts.treatment_history.parsed_date.mounth + " в "
        + ts.treatment_history.parsed_date.hours + ":"
        + ts.treatment_history.parsed_date.minutes + " "
        + ts.treatment_history.parsed_date.year
}
onBeforeMount(async () => {
    store.dispatch('patientTreatments/fetchTreatmentsHistories', slug.value)
})
</script>
<template>
    <HeaderLayout>
        <TabMenu />
    </HeaderLayout>
    <main v-if="!treatmentHistories.length" class="flex justify-center p-4">
        <p class="text-3xl text-slate-400">Лечебных записей пока нет</p>
    </main>
    <main v-else class="bg__section m-2 p-2 rounded-lg">
        <div v-for="ts in treatmentHistories" :key="ts.treatment_history.slug" class="p-2">
            <Panel :header="ts.treatment_history.title + ' ' + panelHeader(ts)" toggleable collapsed>
                <div class="flex flex-col gap-4">
                    <div class="flex flex-col">
                        <p>Описание</p>
                        <p>
                            {{ ts.treatment_history.description }}
                        </p>
                    </div>
                    <div class="flex flex-col">
                        <p>Заключение</p>
                        <p>
                            {{ ts.treatment_history.conclusion }}
                        </p>
                    </div>
                </div>
                <TreatmentHistoryImageListSection :images="ts.images_for_analyzes" />
                <TreatmentHistoryDocumentListSection :documents="ts.documents" />
            </Panel>
        </div>
    </main>
</template>
<style lang="css" scoped>
.bg__section {
    background-color: rgba(110, 131, 165, 0.103);
}
</style>