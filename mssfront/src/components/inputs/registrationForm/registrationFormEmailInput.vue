<script setup>
import registrationFormBaseInput from './Base/registrationFormBaseInput.vue';
import { reactive } from 'vue';
const emailInput = reactive({
    labelText: "Email",
    inputPlaceholder: "name@email.com",
    inputType: "email",
    labelFor: "email_input"
})
</script>
<template>
    <registrationFormBaseInput :labelText="emailInput.labelText" :inputPlaceholder="emailInput.inputPlaceholder"
        :inputType="emailInput.inputType" :labelFor="emailInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" />
</template>