<script setup>
import { useRouter } from 'vue-router';
import { onMounted, reactive, ref } from 'vue';
import { Field } from 'vee-validate';
import { object, string } from 'yup';
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue';
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import EmailService from '@/../services/EmailService'
import { useToast } from 'primevue/usetoast';
import Toast from 'primevue/toast';
const router = useRouter()
const toast = useToast()
const emailService = new EmailService()
const data = reactive({
    email: ""
})
const errors = ref([])
const validationSchema = object({
    email: string()
        .required("Почта не может быть пустой")
        .email("Не является строкой типа test@example.com"),
})
const submit = async () => {
    const redirectLink = `${window.origin}/#/reset/`
    await emailService.sendEmail({
        "link": redirectLink,
        "email": data.email,
        "is_reset_password": true,
    }).then((response) => {
        if (response.status == 200) {
            toast.add({ severity: 'success', summary: 'Успех', detail: 'Сообщение отправлено на почту', life: 3000 });
            errors.value = []
        }
    }).catch(error => {
        const errorsObj = error.response.data
        for (const key in errorsObj) {
            if (errors.value.indexOf(errorsObj[key]) === -1) {
                errors.value.push(errorsObj[key])
            }
        }
    })
}
onMounted(async () => {
    errors.value = []
})
const homeRedirect = () => router.push({ name: "site-home-page" })

</script>
<template>
    <Toast />
    <main class="flex justify-center p-4">
        <section class="flex flex-col items-center w-full">
            <div>
                <div class="flex w-full pt-3">
                    <header class="flex w-full flex-col gap-3 mb-5">
                        <div class="text-5xl font-black underline decoration-2  hover:cursor-pointer" @click="homeRedirect">
                            MSS</div>
                        <div class="text-lg font-black">Введите свою почту для изменение пароля</div>
                    </header>
                </div>
            </div>
            <BaseForm :schema="validationSchema" @submit-form="submit" :errors="errors">
                <FormInputPayload label-text="Почта" id="email">
                    <Field id="email" type="email" class="base" name="email" v-model="data.email"></Field>
                </FormInputPayload>
                <FormSubmitButton :button-text="'Отправить'" />
            </BaseForm>
        </section>
    </main>
</template>