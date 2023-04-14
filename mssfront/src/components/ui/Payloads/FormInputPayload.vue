<script setup>
import { defineProps } from 'vue';
import { ErrorMessage } from 'vee-validate';
const props = defineProps({
    labelText: String,
    id: String,
})
</script>
<template>
    <div class="field__wrapper">
        <label class="field__label" :for="props.id">{{ props.labelText }}</label>
        <slot></slot>
        <small class="error" :id=props.id>
            <ErrorMessage :name="props.id" />
        </small>
    </div>
</template>
<style>
.field__wrapper {
    display: flex;
    flex-direction: column;
}

.field__label {
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 1.15em;
    line-height: 30px;
    font-weight: 600;
    position: relative;
}

.error {
    padding: 5px;
    color: rgb(239 68 68);
    line-height: 15px;
    font-weight: 400;
    font-size: 0.9em;
}

.base {
    padding: 0.5rem;
    border: 1px solid #D1D5DB;
    border-radius: 0.75rem;
    font-size: 1rem;
    line-height: 1.5rem;
    margin-bottom: 0.25rem;
    appearance: none;
    margin: 0;
}

.base:focus {
    outline: none;
    border: 1px solid #93C5FD;
    box-shadow: rgba(23, 0, 0, 0.5) 3px;
}
</style>