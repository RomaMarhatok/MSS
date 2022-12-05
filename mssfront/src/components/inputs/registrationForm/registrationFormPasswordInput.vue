<script setup>
import registrationFormBaseInput from './Base/registrationFormBaseInput.vue';
import { reactive } from 'vue';

const passwordInput = reactive({
    labelText: "Password",
    inputPlaceholder: "password",
    inputType: "password",
    labelFor: "password_input",
})
</script>
<template>
    <registrationFormBaseInput :labelText="passwordInput.labelText" :inputPlaceholder="passwordInput.inputPlaceholder"
        :inputType="passwordInput.inputType" :labelFor="passwordInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" />
</template>