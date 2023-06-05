<script setup>
// libraries
import { useStore } from 'vuex';
import { Field } from 'vee-validate'
import { string, object } from 'yup'
import { reactive, computed } from 'vue'

// components
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue'
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'

//stores
const store = useStore()

//refs
const errors = computed(() => store.getters["registration/getErrors"])
const data = reactive(
    {
        login: "",
        password: ""
    }
)

// schemas
const validationSchema = object({
    login: string()
        .required("Логин не может быть пустым")
        .matches(/^[a-zA-Z0-9_-]{3,100}$/,
            "Введите валидный логин. Логин может содержать только Английские символы, числа, и эти сиволы '_', '-'."
        ),
    password: string()
        .required("Пароль не можеть быть пустым")
        .matches(/^[a-zA-Z0-9]{8,100}$/,
            "Пароль может содержать только Английские символы и числа минимальная длинна пароля 8"
        )
})
</script>
<template>
    <BaseForm :schema="validationSchema" @SubmitForm="$emit('SubmitUserForm', data)" :errors="errors" class="w-full">
        <FormInputPayload :label-text="'Логин'" :id="'login'">
            <Field id="login" type='text' class="base" name="login" v-model="data.login" />
        </FormInputPayload>
        <FormInputPayload :label-text="'Пароль'" :id="'password'">
            <Field id="password" type='password' class="base" name="password" v-model="data.password" />
        </FormInputPayload>
        <FormSubmitButton :buttonText="'Следующий шаг'" />
    </BaseForm>
</template>