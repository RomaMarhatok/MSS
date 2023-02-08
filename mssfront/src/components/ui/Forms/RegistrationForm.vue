<script setup>
import { reactive, onBeforeMount } from "vue"
import { useStore } from 'vuex'
import { useRouter } from "vue-router";
import baseForm from "./Base/BaseForm.vue"
import formEmailInput from '@/components/ui/Inputs/FormEmailInput.vue';
import formPasswordInput from '@/components/ui/Inputs/FormPasswordInput.vue';
import formSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import formFirstNameInput from '@/components/ui/Inputs/FormFirstNameInput.vue';
import formSecondNameInput from '@/components/ui/Inputs/FormSecondNameInput.vue';
const store = useStore()
const router = useRouter()
const formData = reactive({
    login: "",
    password: "",
    first_name: "",
    second_name: "",
})
onBeforeMount(() => {
    store.dispatch("responseErrors/clearErrors")
    store.dispatch("registration/clearAll")

})

function submitForm() {
    store.dispatch("responseErrors/clearErrors")
    store.dispatch("registration/registrateUser", formData).then((message) => {
        if (message) {
            router.push("/")
            store.dispatch("responseErrors/clearErrors")
        }
    })

}
</script>
<template>
    <baseForm @SubmitForm="submitForm">
        <div class="flex flex-row gap-3">
            <formFirstNameInput v-model="formData.first_name" />
            <formSecondNameInput v-model="formData.second_name" />
        </div>
        <formEmailInput v-model="formData.login" />
        <formPasswordInput v-model="formData.password" />
        <formSubmitButton :buttonText="'Sign up'" />
    </baseForm>
</template>