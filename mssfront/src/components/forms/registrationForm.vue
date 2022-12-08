<script setup>
import { reactive, ref, computed } from "vue"
import { useRouter } from "vue-router";
import baseForm from "@/components/forms/base/baseForm.vue"
import RegistrationService from "@/../services/RegistrationService"
import formEmailInput from '@/components/inputs/formEmailInput.vue';
import formPasswordInput from '@/components/inputs/formPasswordInput.vue';
import formSubmitButton from '@/components/buttons/formSubmitButton.vue';
import formFirstNameInput from '@/components/inputs/formFirstNameInput.vue';
import formSecondNameInput from '@/components/inputs/formSecondNameInput.vue';
const message = ref("")
const registrationService = ref(new RegistrationService())
const router = useRouter()
const errors = reactive({
    general: [],
    login: [],
    password: [],
    first_name: [],
    second_name: [],
})
const formData = reactive({
    login: "",
    password: "",
    first_name: "",
    second_name: "",
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
const firstNameErrors = computed(() => {
    return errors.first_name ?? []
})
const secondNameErrors = computed(() => {
    return errors.second_name ?? []
})
function submitForm() {
    message.value = ""
    for (let key in errors) errors[key] = []

    registrationService.value.registerUser(formData).then(response => {
        message.value = response.data.message
        router.push("/")
    }).catch(error => {
        let errorsFromResponce = error.response.data.errors
        errors.general = errorsFromResponce.general
        errors.login = errorsFromResponce.login
        errors.password = errorsFromResponce.password
        errors.first_name = errorsFromResponce.first_name
        errors.second_name = errorsFromResponce.second_name
    })
}
</script>
<template>
    <baseForm @SubmitForm="submitForm" :errors="generalErrors" :message="message">
        <div class="form__header">
            <formFirstNameInput v-model="formData.first_name" :errors="firstNameErrors" />
            <formSecondNameInput v-model="formData.second_name" :errors="secondNameErrors" />
        </div>
        <formEmailInput v-model="formData.login" :errors="loginErrors" />
        <formPasswordInput v-model="formData.password" :errors="passwordErrors" />
        <formSubmitButton :buttonText="'Sign up'" />
    </baseForm>
</template>
<style scoped>
.form__header {
    display: flex;
    flex-direction: row;
    gap: 10px;
}
</style>