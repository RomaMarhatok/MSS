<script setup>
import documentListPageCard from '@/components/cards/documentListPageCard.vue';
import { defineProps } from 'vue';
const props = defineProps({
    documents: Object
})
</script>
<template>
    <main>
        <div>
            <div class="flex flex-row">
                <font-awesome-icon icon="fa-solid fa-magnifying-glass" class="relative" />
                <input class="m-0 p-3 pr-8 font-extrabold w-full rounded-2xl outline-none">
            </div>
        </div>
        <div
            class="grid-cols-5 grid-flow-row-dense gap-3 justify-center w-4/5 max-[600px]:grid-cols-1 max-[900px]:grid-cols-2 max-[1300px]:grid-cols-3">
            <div v-if="props.documents">
                <documentListPageCard v-for="(document, index) in props.documents" :key="index" :document="document" />
            </div>
        </div>
    </main>

</template>