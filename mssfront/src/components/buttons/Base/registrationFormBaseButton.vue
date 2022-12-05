<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    buttonText: String,
    buttonType: String
})
</script>
<template>
    <button class="form__button" :type="props.buttonType">{{ props.buttonText }}</button>
</template>
<style scoped>
.form__button {
    background-color: rgba(19, 48, 94, 1);
    color: rgba(171, 134, 69, 1);
    border: 1px solid black;
    border-radius: 10px;
    font-family: 'Fira Sans';
    padding: 5px;
    font-size: 1em;
    cursor: pointer;
}
</style>