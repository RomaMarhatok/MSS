<script setup>
import registrationFormBaseButton from "./Base/registrationFormBaseButton.vue"
import { reactive } from "vue";
const submitButton = reactive({
    buttonType: "submit",
    buttonText: "Log in"
})
</script>
<template>
    <registrationFormBaseButton :buttonType="submitButton.buttonType" :buttonText="submitButton.buttonText" />
</template>
