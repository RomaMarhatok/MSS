<script setup>
import formBaseInput from './Base/formBaseInput.vue';
import { reactive, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const emailInput = reactive({
    labelText: "Username",
    inputPlaceholder: "EANkEtoR",
    inputType: "text",
    labelFor: "text_input"
})
const errors = computed(() => store.getters["response/loginErrors"])
</script>
<template>
    <formBaseInput :labelText="emailInput.labelText" :inputPlaceholder="emailInput.inputPlaceholder"
        :inputType="emailInput.inputType" :labelFor="emailInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" :errors="errors" />
</template>