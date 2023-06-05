<script setup>

// libraries
import { useStore } from 'vuex';
import { string, object } from 'yup'
import { Field } from 'vee-validate'
import { reactive, computed } from 'vue'
//components
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue'

//stores
const store = useStore()

//refs
const errors = computed(() => store.getters["registration/getErrors"])
const data = reactive(
    {
        country: "Беларусь",
        city: "",
        address: "",
    }
)
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
    <BaseForm :schema="validationSchema" @SubmitForm="$emit('SubmitUserLocationForm', data)" :errors="errors"
        class="w-full">
        <FormInputPayload :label-text="'Город'" :id="'city'">
            <Field id="city" type="text" class="base" name="city" v-model="data.city" />
            <!-- <Field name="city" v-slot="{ value, errorMessage, handleChange }" v-model="data.city">
                <Dropdown @update:model-value="handleChange" :model-value="value" :options="cities" optionLabel="label"
                    optionValue="value" placeholder="Выберите город" />
                <small class="p-error">{{ errorMessage }}</small>
            </Field> -->
        </FormInputPayload>
        <FormInputPayload :label-text="'Адрес'" :id="'address'">
            <Field id="addess" type="text" class="base" name="address" v-model="data.address" />
        </FormInputPayload>
        <FormSubmitButton :buttonText="'Следующий шаг'" />
    </BaseForm>
</template>