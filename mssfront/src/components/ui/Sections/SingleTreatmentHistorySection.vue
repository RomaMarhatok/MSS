<script setup>
import { useStore } from 'vuex';
import { defineProps, computed } from 'vue'
import ChangeTreatmentHistoryForm from '../Forms/treatmentHistoryForms/ChangeTreatmentHistoryForm.vue';
import TreatmentHistoryImageListSection from "@/components/ui/Sections/TreatmentHistoryImageListSection.vue"
import TreatmentHistoryDocumentListSection from './TreatmentHistoryDocumentListSection.vue';
import ChangeTreatmentHistoryImageSection from './ChangeTreatmentHistoryImageSection.vue';
import ChangeTreatmentHistoryDocumentSection from './ChangeTreatmentHistoryDocumentSection.vue';
import addImageDialog from '@/components/ui/Dialogs/addImageDialog.vue';
import addDocumentDialog from '@/components/ui/Dialogs/addDocumentDialog.vue';
const props = defineProps({
    swapOnChangeForm: {
        type: Boolean,
        default: () => false,
    },
    treatmentHistorySlug: String
})
const store = useStore()
const selectedTreatmentHistoryData = computed(() => store.getters["treatments/getTreatmentHistoryBySlug"](props.treatmentHistorySlug))
</script>
<template>
    <div>
        <div v-if="!props.swapOnChangeForm">
            <div>
                <div class="flex-col p-2">
                    <p>Название</p>
                    <p>{{ selectedTreatmentHistoryData.treatment_history.title }}</p>
                </div>
                <div class="flex-col p-2">
                    <p>Описание</p>
                    <p>{{ selectedTreatmentHistoryData.treatment_history.description }}</p>
                </div>
                <div class="flex-col p-2">
                    <p>Заключение</p>
                    <p>{{ selectedTreatmentHistoryData.treatment_history.conclusion }}</p>
                </div>
            </div>
            <div class="flex gap-4 justify-between">
                <TreatmentHistoryImageListSection :images="selectedTreatmentHistoryData.images_for_analyzes" />
                <TreatmentHistoryDocumentListSection :documents="selectedTreatmentHistoryData.documents" />
            </div>

        </div>
        <div v-else class="flex flex-col w-full">
            <ChangeTreatmentHistoryForm :treatment-history="selectedTreatmentHistoryData.treatment_history"
                @change-success="$emit('onChangeTreatmentHistory')" />
            <div class="bordered__section w-full mt-4 bg-white p-2">
                <div class="flex gap-2 p-2">
                    <addImageDialog :treatment-history-slug="selectedTreatmentHistoryData.treatment_history.slug" />
                    <addDocumentDialog :treatment-history-slug="selectedTreatmentHistoryData.treatment_history.slug" />
                </div>
                <div class="flex gap-4 justify-between">
                    <ChangeTreatmentHistoryImageSection
                        :treatment-history-slug="selectedTreatmentHistoryData.treatment_history.slug" />
                    <ChangeTreatmentHistoryDocumentSection
                        :treatment-history-slug="selectedTreatmentHistoryData.treatment_history.slug" />
                </div>

            </div>
        </div>
    </div>
</template>
<style lang="css" scoped>
.bordered__section {
    border: 1px solid rgb(218, 218, 218);
    border-radius: 5px;
}
</style>