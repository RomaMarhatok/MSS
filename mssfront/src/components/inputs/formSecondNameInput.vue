<script setup>
import formBaseInput from '@/components/inputs/base/formBaseInput.vue';
import { reactive, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const passwordInput = reactive({
    labelText: "Second Name",
    inputPlaceholder: "second name",
    inputType: "text",
    labelFor: "second_name_input",
})
const errors = computed(() => store.getters["responseErrors/secondNameErrors"])

</script>
<template>
    <formBaseInput :labelText="passwordInput.labelText" :inputPlaceholder="passwordInput.inputPlaceholder"
        :inputType="passwordInput.inputType" :labelFor="passwordInput.labelFor"
        @input="$emit('update:modelValue', $event.target.value)" :errors="errors" />
</template>