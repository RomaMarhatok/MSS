<script setup>
import { ref } from 'vue'
import Dialog from 'primevue/dialog';
import AddPhysicalParametersForm from '@/components/ui/Forms/AddPhysicalParametersForm.vue';
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
        <button class="add-ph-button" @click="openDialog">Добваить запись</button>
        <Dialog v-model:visible="dialog" header="Добавить запись">
            <AddPhysicalParametersForm @add-physical-parameters="closeDialog" />
        </Dialog>
    </main>
</template>
<style lang="css" scoped>
.add-ph-button {
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

.add-ph-button:focus:not(:focus-visible):not(.focus-visible) {
    box-shadow: none;
    outline: none;
}

.add-ph-button:hover {
    background-color: #2c974b;
}

.add-ph-button:focus {
    box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
    outline: none;
}

.add-ph-button:disabled {
    background-color: #94d3a2;
    border-color: rgba(27, 31, 35, .1);
    color: rgba(255, 255, 255, .8);
    cursor: default;
}

.add-ph-button:active {
    background-color: #298e46;
    box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;
}
</style>