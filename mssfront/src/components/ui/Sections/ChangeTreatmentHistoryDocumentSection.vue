<script setup>
import { defineProps, computed } from 'vue'
import { useStore } from 'vuex'
import TreatmentHistoryService from '@/../services/TreatmentHistoryService'
import { useToast } from 'primevue/usetoast';
const store = useStore()
const toast = useToast()
const treatmentHistoryService = new TreatmentHistoryService()
const props = defineProps({
    treatmentHistorySlug: String,
})
const documents = computed(() => store.getters["treatments/getTreatmentHistoryDocuments"](props.treatmentHistorySlug))
const deleteDocument = (documentSlug) => {
    const data = {
        treatment_history_slug: props.treatmentHistorySlug,
        document_slug: documentSlug,
    }
    treatmentHistoryService.deleteTreatmentHistoryDocument(data).then(
        response => {
            if (response.status == 200) {
                store.commit("treatments/deleteDocument", {
                    documentSlug: response.data.deleted_document_slug,
                    treatmentHistorySlug: props.treatmentHistorySlug
                })
                toast.add({ severity: 'success', summary: 'Успех', detail: 'Запись удалена', life: 3000 });
            }
        }
    )
}
</script>

<template>
    <main class="p-2">
        <p>Прилогающиеся документы</p>
        <div v-if="!documents.length">
            <p>Нет прилогающихся документов</p>
        </div>
        <div v-else>
            <div v-for="(document, index) in  documents" :key="document.slug" class="flex justify-between">
                <p>{{ index + 1 }}. {{ document.name }}</p>
                <button @click="deleteDocument(document.slug)"><i class="pi pi-times"></i></button>
            </div>
        </div>
    </main>
</template>