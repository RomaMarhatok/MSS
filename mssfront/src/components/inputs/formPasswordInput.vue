<script setup>
import formBaseInput from '@/components/inputs/base/formBaseInput.vue';
import { reactive, defineProps } from 'vue';

const passwordInput = reactive({
    labelText: "Password",
    inputPlaceholder: "password",
    inputType: "password",
    labelFor: "password_input",
})
const props = defineProps({
    errors: Object,
})
</script>
<template>
    <formBaseInput :labelText="passwordInput.labelText" :inputPlaceholder="passwordInput.inputPlaceholder"
        :inputType="passwordInput.inputType" :labelFor="passwordInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" :errors="props.errors" />
</template>