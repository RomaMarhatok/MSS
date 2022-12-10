<script setup>
import { reactive, ref, computed } from "vue"
import { useRouter } from "vue-router";
import baseForm from "@/components/forms/base/baseForm.vue"
import AuthenticationService from "../../../services/AuthenticationService";
import formEmailInput from '@/components/inputs/formEmailInput.vue';
import formPasswordInput from '@/components/inputs/formPasswordInput.vue';
import formSubmitButton from '@/components/buttons/formSubmitButton.vue';
const authenticationService = ref(new AuthenticationService())
const router = useRouter()
const errors = reactive({
    general: [],
    login: [],
    password: [],
})
const formData = reactive({
    login: "",
    password: "",
})
const generalErrors = computed(() => {
    return errors.general ?? []
})
const loginErrors = computed(() => {
    return errors.login ?? []
})
const passwordErrors = computed(() => {
    return errors.password ?? []
})
function submitForm() {
    for (let key in errors) errors[key] = []

    authenticationService.value.authenticateUser(formData).then(() => {
        router.push("/")
    }).catch(error => {
        let errorsFromResponce = error.response.data.errors
        errors.general = errorsFromResponce.general
        errors.login = errorsFromResponce.login
        errors.password = errorsFromResponce.password
        console.log(generalErrors)
    })
}
</script>
<template>
    <baseForm @SubmitForm="submitForm" :errors="generalErrors">
        <formEmailInput v-model="formData.login" :errors="loginErrors" />
        <formPasswordInput v-model="formData.password" :errors="passwordErrors" />
        <formSubmitButton :buttonText="'Log in'" />
    </baseForm>
</template>