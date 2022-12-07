<script setup>
import formBaseInput from '@/components/inputs/base/formBaseInput.vue';
import { reactive } from 'vue';

const passwordInput = reactive({
    labelText: "Second Name",
    inputPlaceholder: "second name",
    inputType: "text",
    labelFor: "second_name_input",
})
</script>
<template>
    <formBaseInput :labelText="passwordInput.labelText" :inputPlaceholder="passwordInput.inputPlaceholder"
        :inputType="passwordInput.inputType" :labelFor="passwordInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" />
</template>