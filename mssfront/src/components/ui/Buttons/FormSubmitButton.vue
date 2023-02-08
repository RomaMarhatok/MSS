<script setup>
import formBaseButton from "./Base/FormBaseButton.vue"
import { reactive, defineProps } from "vue";
const submitButton = reactive({
    buttonType: "submit",
})
const props = defineProps({
    buttonText: String
})

</script>
<template>
    <formBaseButton :buttonType="submitButton.buttonType" :buttonText="props.buttonText" />
</template>
