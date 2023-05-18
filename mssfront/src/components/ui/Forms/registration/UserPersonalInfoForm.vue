<script setup>

// libraries
import { useStore } from 'vuex';
import { Field } from 'vee-validate';
import { reactive, computed } from 'vue'
import { string, object, number } from 'yup'

//components
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue'
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'

//stores
const store = useStore()

//refs
const errors = computed(() => store.getters["registration/getErrors"])
const data = reactive(
    {
        first_name: "",
        second_name: "",
        patronymic: "",
        email: "",
        age: 0,
        gender: "",
    }
)
//schemas
const validationSchema = object(
    {
        first_name: string()
            .required("Имя не может быть пустым")
            .matches(/^[\u0400-\u04FF]+$/, "Может содержать только буквы"),
        second_name: string()
            .required("Фамилия не может быть пустым")
            .matches(/^[\u0400-\u04FF]+$/, "Может содержать только буквы"),
        patronymic: string()
            .required("Отчество не может быть пустым")
            .matches(/^[\u0400-\u04FF]+$/, "Может содержать только буквы"),
        email: string()
            .required("Почта не может быть пустой")
            .email("Не является строкой типа test@example.com")
            .matches(/^[\w-\\._\\+%]+@(gmail|yandex)\./, "Поддерживается почта только от Yandex и Gmail"),
        gender: string()
            .required("Пол не может быть пустым"),
        age: number()
            .required("Возраст не может быть пустым",)
            .min(0, "Минимальное значение 0")
            .max(130, "Максимальное занчение 130")
    }
)
</script>
<template>
    <BaseForm :schema="validationSchema" @SubmitForm="$emit('SubmitUserPersonalInfoForm', data)" :errors="errors"
        class="w-full">
        <div class="flex flex-row gap-2">
            <FormInputPayload label-text="Имя" id="first_name">
                <Field id="first_name" type='text' class="base" name="first_name" v-model="data.first_name" />
            </FormInputPayload>
            <FormInputPayload label-text="Фамилия" id="second_name">
                <Field id="second_name" type='text' class="base" name="second_name" v-model="data.second_name" />
            </FormInputPayload>
        </div>
        <FormInputPayload label-text="Отчество" id="patronymic">
            <Field id="patronymic" type='text' class="base" name="patronymic" v-model="data.patronymic" />
        </FormInputPayload>
        <FormInputPayload label-text="Почта" id="email">
            <Field id="email" type="email" class="base" name="email" v-model="data.email"></Field>
        </FormInputPayload>
        <FormInputPayload label-text="Возраст" id="age">
            <Field id="age" type='number' class="base" name="age" v-model="data.age" />
        </FormInputPayload>
        <div class="flex m-3 gap-2">
            <label class="font-black text-lg">Пол</label>
            <Field name="gender" type="radio" v-model="data.gender" :value="'F'" />Ж
            <Field name="gender" type="radio" v-model="data.gender" :value="'M'" />М
        </div>
        <FormSubmitButton :buttonText="'Следующий шаг'" />
    </BaseForm>
</template>