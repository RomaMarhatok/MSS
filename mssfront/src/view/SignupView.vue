<script setup>
import { useStore } from 'vuex'
import { useRouter } from "vue-router";
import { reactive, onBeforeMount } from "vue"

import BodyLayout from '@/components/layout/BodyLayout.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';

import BaseForm from "@/components/ui/Forms/Base/BaseForm.vue"
import FormEmailInput from '@/components/ui/Inputs/FormEmailInput.vue';
import FormPasswordInput from '@/components/ui/Inputs/FormPasswordInput.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import FormFirstNameInput from '@/components/ui/Inputs/FormFirstNameInput.vue';
import FormSecondNameInput from '@/components/ui/Inputs/FormSecondNameInput.vue';

const store = useStore()
const router = useRouter()
const formData = reactive({
    login: "",
    password: "",
    first_name: "",
    second_name: "",
})

onBeforeMount(() => {
    store.dispatch("response/resetErrors")
    store.dispatch("registration/resetMessage")
})

function submitForm() {
    store.dispatch("response/resetErrors")
    store.dispatch("registration/registrateUser", formData).then((status) => {
        console.log("submit", status)
        if (status == 200) {
            router.push("/")
            store.dispatch("response/resetErrors")
            store.dispatch("registration/resetMessage")
        }
    })
}
</script>
<template>
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <HeaderLayout>
            <header class="flex flex-col gap-3 mb-5">
                <div class="text-5xl font-black underline decoration-2">MSS</div>
                <div class="text-lg font-black">Nice to meet you in our medical system!</div>
            </header>
        </HeaderLayout>
        <BodyLayout :class="'w-4/5'">
            <BaseForm @SubmitForm="submitForm">
                <div class="flex flex-row gap-3">
                    <FormFirstNameInput v-model="formData.first_name" />
                    <FormSecondNameInput v-model="formData.second_name" />
                </div>
                <FormEmailInput v-model="formData.login" />
                <FormPasswordInput v-model="formData.password" />
                <FormSubmitButton :buttonText="'Sign up'" />
            </BaseForm>
        </BodyLayout>
    </main>
</template>