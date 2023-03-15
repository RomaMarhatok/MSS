<script setup>
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { reactive, onBeforeMount } from "vue"

import BaseForm from "@/components/ui/Forms/Base/BaseForm.vue"
import FormEmailInput from '@/components/ui/Inputs/FormEmailInput.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import FormPasswordInput from '@/components/ui/Inputs/FormPasswordInput.vue';

import BodyLayout from '@/components/layout/BodyLayout.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import FooterLayout from '@/components/layout/FooterLayout.vue';
import ChangePasswordLink from '@/components/common/Links/ChangePasswordLink.vue';

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
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <HeaderLayout :class="'pt-3'">
            <header class="flex flex-col gap-3 mb-5">
                <div class="text-5xl font-black underline decoration-2">MSS</div>
                <div class="text-lg font-black">Log in to improve your medical experience!</div>
            </header>
        </HeaderLayout>
        <BodyLayout :class="'w-4/5'">
            <BaseForm @SubmitForm="submitForm">
                <FormEmailInput v-model="formData.login" />
                <FormPasswordInput v-model="formData.password" />
                <FormSubmitButton :buttonText="'Log in'" />
            </BaseForm>
        </BodyLayout>
        <FooterLayout>
            <ChangePasswordLink></ChangePasswordLink>
        </FooterLayout>
    </main>
</template>