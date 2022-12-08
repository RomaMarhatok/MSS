<script setup>
import formBaseInput from '@/components/inputs/base/formBaseInput.vue';
import { reactive, defineProps } from 'vue';
const emailInput = reactive({
    labelText: "Username",
    inputPlaceholder: "EANkEtoR",
    inputType: "text",
    labelFor: "text_input"
})
const props = defineProps({
    errors: Object,
})
</script>
<template>
    <formBaseInput :labelText="emailInput.labelText" :inputPlaceholder="emailInput.inputPlaceholder"
        :inputType="emailInput.inputType" :labelFor="emailInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" :errors="props.errors" />
</template>