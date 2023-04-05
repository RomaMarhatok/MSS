<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    buttonText: String,
    buttonType: String,
    buttonEvent: Function,
})
</script>
<template>
    <button class="form__button border-1 border-black border-solid cursor-pointer text-base p-1 rounded-xl"
        :type="props.buttonType" @click="props.buttonEvent">
        {{ props.buttonText }}
    </button>
</template>
<style scoped>
.form__button {
    background-color: rgba(19, 48, 94, 1);
    color: rgba(171, 134, 69, 1);
}

.form__button:hover {
    color: rgb(194, 153, 81);
    background-color: rgb(31, 70, 131);
    transition: 0.5s;
}
</style>