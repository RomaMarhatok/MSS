<script setup>
import { defineProps, ref, computed } from 'vue'
import Dialog from "primevue/dialog";
const props = defineProps({
    documents: {
        type: Array,
        default: () => []
    }
})
const dialog = ref(false)
const selectedDocumentSlug = ref("")
const selectedDocument = computed(() => props.documents.find(d => d.slug = selectedDocumentSlug.value))
const onClick = (documentSlug) => {
    console.log(documentSlug)
    selectedDocumentSlug.value = documentSlug
    dialog.value = true
}
</script>
<template>
    <main class="p-2 bg-white rounded-md w-full">
        <p>Прилогающиеся документы</p>
        <div v-if="!props.documents.length">
            <p>Нет прилогающихся документов</p>
        </div>
        <div v-else>
            <div v-for="(document, index) in  documents" :key="document.slug" @click="onClick(document.slug)">
                <p>{{ index + 1 }}. {{ document.name }}</p>
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
<style lang="css" scoped>
.main {
    display: flex;
    justify-content: center;
}

.document-header {
    border-radius: 10px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    word-break: break-all;
    padding-top: 1rem;
}

.content-container {
    display: flex;
    flex-direction: column;
    padding-left: 20px;
    width: 100%;

}

.header-container {
    display: flex;
    width: 100%;
    justify-content: center;
    gap: 1rem;
}
</style>