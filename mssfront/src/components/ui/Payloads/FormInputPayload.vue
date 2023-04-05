<script setup>
import { defineProps } from 'vue';
import { ErrorMessage } from 'vee-validate';
const props = defineProps({
    labelText: String,
    id: String,
})
</script>
<template>
    <div class="field flex flex-col gap-1 w-full focus:shadow-outline">
        <label class="font-black text-lg" :for="props.id">{{ props.labelText }}</label>
        <slot></slot>
        <small class="text-red-500" :id=props.id>
            <ErrorMessage :name="props.id" />
        </small>
    </div>
</template>
<style>
.base {
    padding: 0.5rem;
    background-color: white;
    border: 2px solid#D1D5DB;
    border-radius: 0.75rem;
    font-size: 1rem;
    line-height: 1.5rem;
    margin-bottom: 0.25rem;
    appearance: none;
    margin: 0
}

.base:focus {
    outline: none;
    border-color: #93C5FD;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}
</style>