<script setup>
import formBaseInput from './Base/formBaseInput.vue';
import { reactive, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const passwordInput = reactive({
    labelText: "First Name",
    inputPlaceholder: "first name",
    inputType: "text",
    labelFor: "first_name_input",
})
const errors = computed(() => store.getters["response/firstNameErrors"])
</script>
<template>
    <formBaseInput :labelText="passwordInput.labelText" :inputPlaceholder="passwordInput.inputPlaceholder"
        :inputType="passwordInput.inputType" :labelFor="passwordInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" :errors="errors" />
</template>