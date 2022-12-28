<script setup>
import { reactive, computed, onMounted } from "vue"
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import baseForm from "@/components/forms/base/baseForm.vue"
import formEmailInput from '@/components/inputs/formEmailInput.vue';
import formPasswordInput from '@/components/inputs/formPasswordInput.vue';
import formSubmitButton from '@/components/buttons/formSubmitButton.vue';
const store = useStore()
const router = useRouter()
const errors = computed(() => store.state.responseErrors.errors)
const formData = reactive({
    login: "",
    password: "",
})
onMounted(() => {
    store.dispatch("responseErrors/clearErrors")
})
function submitForm() {
    console.log(formData)
    store.dispatch("authentication/authenticateUser", formData).then((responseStatus) => {
        if (responseStatus == 200) {
            store.dispatch("responseErrors/clearErrors")
        }
        if (Object.keys(errors.value).length === 0) {
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