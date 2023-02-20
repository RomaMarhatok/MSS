<script setup>
import formBaseInput from './Base/formBaseInput.vue';
import { reactive, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const passwordInput = reactive({
    labelText: "Password",
    inputPlaceholder: "password",
    inputType: "password",
    labelFor: "password_input",
})
const errors = computed(() => store.getters["response/passwordErrors"])
</script>
<template>
    <formBaseInput :labelText="passwordInput.labelText" :inputPlaceholder="passwordInput.inputPlaceholder"
        :inputType="passwordInput.inputType" :labelFor="passwordInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" :errors="errors" />
</template>