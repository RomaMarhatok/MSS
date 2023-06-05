<script setup>
import { ref } from 'vue'
import Dialog from 'primevue/dialog';
import { defineProps } from 'vue'
import AddTreatmentHistoryDocumentForm from '@/components/ui/Forms/treatmentHistoryForms/AddDocumentForm.vue';
const props = defineProps({
    treatmentHistorySlug: String
})
const dialog = ref(false)
const openDialog = () => {
    dialog.value = true
}
const closeDialog = () => {
    dialog.value = false
}

</script>
<template>
    <button class="add-document-button" @click="openDialog">Добавить документ</button>
    <Dialog v-model:visible="dialog" header="Добавить документ" :style="{ width: '50vw' }">
        <AddTreatmentHistoryDocumentForm @onAddDocument="closeDialog" :treatmentHistorySlug="props.treatmentHistorySlug" />
    </Dialog>
</template>
<style lang="css" scoped>
.add-document-button {
    appearance: none;
    background-color: #38cf63;
    border: 1px solid rgba(27, 31, 35, .15);
    border-radius: 6px;
    box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 14px;
    font-weight: 600;
    line-height: 20px;
    padding: 6px 16px;
    position: relative;
    text-align: center;
    text-decoration: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
    white-space: nowrap;
}

.add-document-button:focus:not(:focus-visible):not(.focus-visible) {
    box-shadow: none;
    outline: none;
}

.add-document-button:hover {
    background-color: #2c974b;
}

.add-document-button:focus {
    box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
    outline: none;
}

.add-document-button:disabled {
    background-color: #94d3a2;
    border-color: rgba(27, 31, 35, .1);
    color: rgba(255, 255, 255, .8);
    cursor: default;
}

.add-document-button:active {
    background-color: #298e46;
    box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;
}
</style>