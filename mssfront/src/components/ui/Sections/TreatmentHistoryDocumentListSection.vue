<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    documents: {
        type: Array,
        default: () => []
    }
})
</script>
<template>
    <main class="p-2">
        <p>Прилогающиеся документы</p>
        <div v-if="!props.documents.length">
            <p>Нет прилогающихся документов</p>
        </div>
        <div v-else>
            <div v-for="(document, index) in  documents" :key="document.slug">
                <p>{{ index + 1 }}. {{ document.name }}</p>
            </div>
        </div>
    </main>
</template>