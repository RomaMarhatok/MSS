<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    buttonText: String,
    buttonType: String,
    buttonEvent: Function,
})
</script>
<template>
    <button class="button" :type="props.buttonType" @click="props.buttonEvent">
        {{ props.buttonText }}
    </button>
</template>
<style scoped>
.button {
    appearance: none;
    background-color: rgb(48, 103, 192);
    color: #fff;
    border: 1px solid rgba(27, 31, 35, .15);
    border-radius: 6px;
    cursor: pointer;
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 1em;
    line-height: 2em;
    font-weight: 600;
    position: relative;
    text-align: center;
    text-decoration: none;
    user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
    white-space: nowrap;
}

.button:hover {
    background-color: rgb(43, 91, 168);
}
</style>