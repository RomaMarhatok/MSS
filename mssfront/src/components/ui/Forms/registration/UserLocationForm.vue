<script setup>

// libraries
import { useStore } from 'vuex';
import { string, object } from 'yup'
import { Field } from 'vee-validate'
import { reactive, computed, ref } from 'vue'

// libraries components
import Dropdown from 'primevue/dropdown'

//components
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue'

//stores
const store = useStore()

//refs
const errors = computed(() => store.getters["registration/getErrors"])
// const options = ref([
//     {
//         name: "Country Name",
//         value: "Country Value",
//     }
// ])
const data = reactive(
    {
        country: "Беларусь",
        city: "",
        address: "",
    }
)
const cities = ref([
    {
        label: "Березино",
        value: "Березино"
    },
    {
        label: "Борисов",
        value: "Борисов"
    },
    {
        label: "Вилейка",
        value: "Вилейка"
    },
    {
        label: "Воложин",
        value: "Воложин"
    },
    {
        label: "Дзержинск",
        value: "Дзержинск"
    },
    {
        label: "Жодино",
        value: "Жодино"
    },
    {
        label: "Заславль",
        value: "Заславль"
    },
    {
        label: "Клецк",
        value: "Клецк"
    },
    {
        label: "Копыль",
        value: "Копыль"
    },
    {
        label: "Крупки",
        value: "Крупки"
    },
    {
        label: "Логойск",
        value: "Логойск"
    },
    {
        label: "Любань",
        value: "Любань"
    },
    {
        label: "Марьина Горка",
        value: "Марьина Горка"
    },
    {
        label: "Минск",
        value: "Минск"
    },
    {
        label: "Молодечно",
        value: "Молодечно"
    },
    {
        label: "Мядель",
        value: "Мядель"
    },
    {
        label: "Несвиж",
        value: "Несвиж"
    },
    {
        label: "Слуцк",
        value: "Слуцк"
    },
    {
        label: "Смолевичи",
        value: "Смолевичи"
    },
    {
        label: "Солигорск",
        value: "Солигорск"
    },
    {
        label: "Старые Дороги",
        value: "Старые Дороги"
    },
    {
        label: "Столбцы",
        value: "Столбцы"
    },
    {
        label: "Узда",
        value: "Узда",
    },
    {
        label: "Фаниполь",
        value: "Фаниполь"
    },
    {
        label: "Червень",
        value: "Червень"
    }

])

//schemas
const validationSchema = object(
    {
        // country: string().required("Страна не может быть пустым"),
        city: string().required("Город не может быть пустым"),
        address: string().required("Адрес не может быть пустым"),
    }
)
</script>
<template>
    <BaseForm :schema="validationSchema" @SubmitForm="$emit('SubmitUserLocationForm', data)" :errors="errors">
        <FormInputPayload :label-text="'Город'" :id="'city'">
            <Field name="city" v-slot="{ value, errorMessage, handleChange }" v-model="data.city">
                <Dropdown @update:model-value="handleChange" :model-value="value" :options="cities" optionLabel="label"
                    optionValue="value" placeholder="Выберите город" />
                <small class="p-error">{{ errorMessage }}</small>
            </Field>
        </FormInputPayload>
        <FormInputPayload :label-text="'Адрес'" :id="'address'">
            <Field id="addess" type="text" class="base" name="address" v-model="data.address" />
        </FormInputPayload>
        <FormSubmitButton :buttonText="'Следующий шаг'" />
    </BaseForm>
</template>