<script setup>
import documentListPageCard from '@/components/cards/documentListPageCard.vue';
import { defineProps } from 'vue';
const props = defineProps({
    documents: Object
})
</script>
<template>
    <div
        class="grid-cols-5 grid-flow-row-dense gap-3 justify-center w-4/5 max-[600px]:grid-cols-1 max-[900px]:grid-cols-2 max-[1300px]:grid-cols-3">
        <div v-if="props.documents">
            <documentListPageCard v-for="(document, index) in props.documents" :key="index" :document="document" />
        </div>
    </div>
</template>