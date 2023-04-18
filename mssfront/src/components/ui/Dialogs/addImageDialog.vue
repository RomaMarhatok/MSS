<script setup>
import { ref, defineProps } from 'vue'
import Dialog from "primevue/dialog";
import AddImageForm from "@/components/ui/Forms/treatmentHistoryForms/AddImageForm.vue";
const props = defineProps({
    treatmentHistorySlug: String,
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
    <main>
        <button class="add-image-button" @click="openDialog">Добавить изображение</button>
        <Dialog v-model:visible="dialog" header="Добавить изображение" :style="{ width: '50vw' }">
            <AddImageForm :treatment-history-slug="props.treatmentHistorySlug" @on-add-image="closeDialog" />
        </Dialog>
    </main>
</template>
<style lang="css" scoped>
.add-image-button {
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

.add-image-button:focus:not(:focus-visible):not(.focus-visible) {
    box-shadow: none;
    outline: none;
}

.add-image-button:hover {
    background-color: #2c974b;
}

.add-image-button:focus {
    box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
    outline: none;
}

.add-image-button:disabled {
    background-color: #94d3a2;
    border-color: rgba(27, 31, 35, .1);
    color: rgba(255, 255, 255, .8);
    cursor: default;
}

.add-image-button:active {
    background-color: #298e46;
    box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;
}
</style>