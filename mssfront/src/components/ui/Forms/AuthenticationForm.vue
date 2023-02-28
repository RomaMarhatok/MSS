<script setup>
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import baseForm from "./Base/BaseForm.vue"
import { reactive, onBeforeMount } from "vue"
import formEmailInput from '@/components/ui/Inputs/FormEmailInput.vue';
import formSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import formPasswordInput from '@/components/ui/Inputs/FormPasswordInput.vue';
const store = useStore()
const router = useRouter()
const formData = reactive({
    login: "",
    password: "",
})
onBeforeMount(() => {
    store.dispatch("response/resetErrors")
    store.dispatch("registration/resetMessage")
})
function submitForm() {
    console.log(formData)
    store.dispatch("authentication/authenticate", formData).then(status => {
        console.log("status authentication", status)
        if (status == 200) {
            router.push("/home/")
        }
    })
}
</script>
<template>
    <baseForm @SubmitForm="submitForm">
        <formEmailInput v-model="formData.login" />
        <formPasswordInput v-model="formData.password" />
        <formSubmitButton :buttonText="'Log in'" />
    </baseForm>
</template>