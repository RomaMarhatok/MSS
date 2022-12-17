<script setup>
import Dropdown from 'primevue/dropdown';
import "primevue/resources/themes/saga-blue/theme.css";
import { ref, reactive, defineProps } from 'vue'
const selectedDocumentType = ref("")
const documentTypes = reactive([
    { name: "medical directions", code: 1 },
    { name: "medical certifications", code: 2 },
    { name: "medical tests", code: 3 },
    { name: "medical tests", code: 4 },
    { name: "medical directions", code: 5 },
    { name: "medical certifications", code: 6 },
    { name: "medical tests", code: 7 },
    { name: "medical tests", code: 8 },
    { name: "medical tests", code: 9 },
    { name: "medical tests", code: 10 },
    { name: "medical tests", code: 11 },

])
const props = defineProps({
    documents: Object
})
</script>
<template>
    <main class="flex flex-col w-full boredr-3 border-solid border-gray-400">
        <section>
            <div class="flex flex-row justify-start bg-custom-menu-color border rounded-xl p-3">
                <Dropdown v-model="selectedDocumentType" :options="documentTypes" optionLabel="name" :editable="true"
                    :placeholder="'document type'" :virtualScrollerOptions="{ itemSize: 38 }" />
            </div>
        </section>
        <section class="flex flex-col justify-start pl-1 mt-3" v-if="props.documents">
            <div class="text-left border-3 border-solid border-black mb-5 hover:border-custom-deep-purple"
                v-for="(document, index) in props.docuemnts" :key="index">
                Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            </div>
        </section>
    </main>
</template>