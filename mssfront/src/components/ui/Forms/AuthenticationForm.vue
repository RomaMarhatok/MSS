<script setup>
import { reactive, computed, onBeforeMount } from "vue"
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import baseForm from "./Base/BaseForm.vue"
import formEmailInput from '@/components/ui/Inputs/FormEmailInput.vue';
import formPasswordInput from '@/components/ui/Inputs/FormPasswordInput.vue';
import formSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
const store = useStore()
const router = useRouter()
const errors = computed(() => store.state.responseErrors.errors)
const formData = reactive({
    login: "",
    password: "",
})
onBeforeMount(() => {
    store.dispatch("responseErrors/clearErrors")
})
function submitForm() {
    console.log(formData)
    store.dispatch("authentication/authenticateUser", formData).then((responseStatus) => {
        if ((Object.keys(errors.value).length === 0) && responseStatus == 200) {
            store.dispatch("responseErrors/clearErrors")
            router.push("/user/" + store.state.user.slug + "/home/")
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