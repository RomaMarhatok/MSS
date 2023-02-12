<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    selectPlaceholder: String
})
</script>
<template>
    <select class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal 
                    text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded
                    transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 
                    focus:outline-none h-full hover:cursor-pointer">
        <option value="" disabled selected>{{ props.selectPlaceholder }}</option>
        <slot>Fallback content</slot>
    </select>
</template>