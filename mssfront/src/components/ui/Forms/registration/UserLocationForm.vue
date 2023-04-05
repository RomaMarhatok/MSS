<script setup>

// libraries
import { useStore } from 'vuex';
import { string, object } from 'yup'
import { Field } from 'vee-validate'
import { reactive, ref, computed } from 'vue'

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
const options = ref([
    {
        name: "Country Name",
        value: "Country Value",
    }
])
const data = reactive(
    {
        country: "",
        city: "",
        address: "",
    }
)

//schemas
const validationSchema = object(
    {
        country: string().required("Страна не может быть пустым"),
        city: string().required("Город не может быть пустым"),
        address: string().required("Адрес не может быть пустым"),
    }
)
</script>
<template>
    <BaseForm :schema="validationSchema" @SubmitForm="$emit('SubmitUserLocationForm', data)" :errors="errors">
        <FormInputPayload :label-text="'Страна'" :id="'country'">
            <Field name="country" v-slot="{ value, errorMessage, handleChange }">
                <label for="country">Country</label>
                <Dropdown @update:model-value="handleChange" :model-value="value" :options="options" optionLabel="name"
                    optionValue="value" placeholder="Выберите страну" />
                <small class="p-error">{{ errorMessage }}</small>
            </Field>
        </FormInputPayload>

        <!-- TODO thing about city and adress fields validation -->
        <FormInputPayload :label-text="'Город'" :id="'city'">
            <Field id="city" type='text' class="base" name="city" v-model="data.city" />
        </FormInputPayload>
        <FormInputPayload :label-text="'Адрес'" :id="'address'">
            <Field id="addess" type="text" class="base" name="address" v-model="data.address" />
        </FormInputPayload>
        <FormSubmitButton :buttonText="'Следующий шаг'" />
    </BaseForm>
</template>