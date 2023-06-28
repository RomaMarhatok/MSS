<script setup>
import { object, string, ref } from 'yup';
import { Field } from 'vee-validate';
import { reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import UserService from '@/../services/UserService'
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue';
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
const toast = useToast()
const router = useRouter()
const route = useRoute()
const token = route.params.token
const uid = route.params.uid
const passwordsData = reactive({
    password1: "",
    password2: "",
})
const data = reactive({
    token: token,
    uid: uid,
})

const validationSchema = object({
    password1: string()
        .required("Пароль не можеть быть пустым")
        .matches(/^[a-zA-Z0-9]{8,100}$/,
            "Пароль может содержать только Английские символы и числа минимальная длинна пароля 8"
        ),
    password2: string()
        .required("Пароль не можеть быть пустым")
        .matches(/^[a-zA-Z0-9]{8,100}$/,
            "Пароль может содержать только Английские символы и числа минимальная длинна пароля 8"
        ).oneOf([ref("password1"), null, ""], "Пароли должны совпадать"),
})
const userService = new UserService()

const submit = async () => {
    data["password"] = passwordsData.password2
    console.log(data)
    userService.resetPassword(data)
        .then(response => {
            if (response.status == 200) {
                toast.add({ severity: 'success', summary: 'Успех', detail: 'Сообщение отправлено на почту', life: 3000 });
            }
        })
        .then(() => router.push({
            name: "authentication-page"
        }))
        .catch(error => {
            toast.add({ severity: 'error', summary: 'Ошибка', detail: error.response.data.description, life: 3000 });
        })
}
</script>
<template>
    <Toast />
    <main class="flex justify-center p-4">
        <section class="flex flex-col items-center w-full">
            <div>
                <div class="flex w-full pt-3">
                    <header class="flex w-full flex-col gap-3 mb-5">
                        <div class="text-5xl font-black underline decoration-2">MSS</div>
                        <div class="text-lg font-black">Введите новый пароль</div>
                    </header>
                </div>
            </div>
            <BaseForm @submit-form="submit" :schema="validationSchema">
                <FormInputPayload label-text="Пароль" id="password1">
                    <Field id="password1" type='password' class="base" name="password1" v-model="passwordsData.password1" />
                </FormInputPayload>
                <FormInputPayload label-text="Повторите пароль" id="password2">
                    <Field id="password2" type='password' class="base" name="password2" v-model="passwordsData.password2" />
                </FormInputPayload>
                <FormSubmitButton button-text="Отправить" />
            </BaseForm>
        </section>
    </main>
</template>