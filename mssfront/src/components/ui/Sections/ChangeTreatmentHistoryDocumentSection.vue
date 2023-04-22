<script setup>
import { defineProps, computed, ref } from 'vue'
import Dialog from 'primevue/dialog'
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
const dialog = ref(false)
const selectedDocumentSlug = ref("")
const selectedDocument = computed(() => documents.value.find(d => d.slug = selectedDocumentSlug.value))
const onClick = (documentSlug) => {
    console.log(documentSlug)
    selectedDocumentSlug.value = documentSlug
    dialog.value = true
}
</script>

<template>
    <main class="p-2 w-full">
        <p>Прилогающиеся документы</p>
        <div v-if="!documents.length">
            <p>Нет прилогающихся документов</p>
        </div>
        <div v-else>
            <div v-for="(document, index) in  documents" :key="document.slug" class="flex justify-between">
                <p @click="onClick(document.slug)">{{ index + 1 }}. {{ document.name }}</p>
                <button @click="deleteDocument(document.slug)"><i class="pi pi-times"></i></button>
            </div>
        </div>
        <Dialog v-model:visible="dialog" modal :header="'Документ'" :style="{ width: '70vw' }">
            <div class="document-header">
                <div class="content-container">
                    <div class="header-container">
                        <div class="flex gap-4">
                            <p>{{ selectedDocument.document_type.name }}</p>
                            <p>{{ selectedDocument.name }}</p>
                        </div>
                        <div>
                            <p>Создано
                                {{ selectedDocument.parsed_date.day +
                                    " " + selectedDocument.parsed_date.mounth +
                                    " " + selectedDocument.parsed_date.year
                                }} в {{ selectedDocument.parsed_date.hours + ":" + selectedDocument.parsed_date.minutes }}
                            </p>
                        </div>

                    </div>

                </div>
            </div>
            <div class="main">
                <p>{{ selectedDocument.content }}</p>
            </div>
        </Dialog>
    </main>
</template>