<script setup>
import { useStore } from 'vuex';
import { ref, defineProps, computed } from 'vue'
import ChangeTreatmentHistoryForm from '../Forms/treatmentHistoryForms/ChangeTreatmentHistoryForm.vue';
import TreatmentHistoryImageListSection from "@/components/ui/Sections/TreatmentHistoryImageListSection.vue"
const props = defineProps({
    swapOnChangeForm: {
        type: Boolean,
        default: () => false,
    },
    treatmentHistorySlug: String
})
const store = useStore()
const selectedTreatmentHistoryAndImages = computed(() => store.getters["treatments/getTreatmentHistoryBySlug"](props.treatmentHistorySlug))
const swapOnChangeForm = ref(false)

const toggleForms = () => {
    swapOnChangeForm.value = false
}
</script>
<template>
    <div>
        <div v-if="!props.swapOnChangeForm">
            <div>
                <div class="flex-col p-2">
                    <p>Название</p>
                    <p>{{ selectedTreatmentHistoryAndImages.treatment_history.title }}</p>
                </div>
                <div class="flex-col p-2">
                    <p>Описание</p>
                    <p>{{ selectedTreatmentHistoryAndImages.treatment_history.description }}</p>
                </div>
                <div class="flex-col p-2">
                    <p>Заключение</p>
                    <p>{{ selectedTreatmentHistoryAndImages.treatment_history.conclusion }}</p>
                </div>
            </div>
            <TreatmentHistoryImageListSection :images="selectedTreatmentHistoryAndImages.images_for_analyzes" />
        </div>
        <div v-else class="flex flex-col w-full">
            <ChangeTreatmentHistoryForm :treatment-history="selectedTreatmentHistoryAndImages.treatment_history"
                @changeSuccess="toggleForms" />
            <div class="bordered__section w-full">
                <TreatmentHistoryImageListSection :images="selectedTreatmentHistoryAndImages.images_for_analyzes" />
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