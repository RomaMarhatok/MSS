<script setup>
import BaseForm from './Base/BaseForm.vue'
import FormInputPayload from '../Payloads/FormInputPayload.vue'
import FormSubmitButton from '../Buttons/FormSubmitButton.vue'
import { object, number } from 'yup'
import { Field } from 'vee-validate'
import { reactive, onBeforeMount, defineEmits } from 'vue'
import { useStore } from 'vuex'
import { useToast } from 'primevue/usetoast'
import PhysicalService from '@/../services/PhysicalService'
const store = useStore()
const toast = useToast()
const data = reactive({})
const physicalService = new PhysicalService()
const emit = defineEmits(["addPhysicalParameters"])
const validationSchema = object({
    weight: number("Должно быть числом").positive("Должно быть положительным числом"),
    height: number("Должно быть числом").positive("Должно быть положительным числом"),
    pressure: number("Должно быть числом").positive("Должно быть положительным числом"),
})
const submit = async () => {
    await physicalService.createPhysicalParameters(data).then(response => {
        if (response.status == 200) {
            store.commit("treatments/addPhysicalParameter", response.data.physical_parameters)
            toast.add({ severity: 'success', summary: 'Успех', detail: 'Запись добавлена', life: 3000 });
            emit('addPhysicalParameters')
        }
    })
}
onBeforeMount(() => {
    const lastPh = store.getters["treatments/getLastPhysicalParameter"]
    Object.assign(data, lastPh)
})
</script>
<template>
    <BaseForm :schema="validationSchema" @submit-form="submit" class="w-full">
        <FormInputPayload label-text="Вес" id="weight">
            <Field id="weight" type="number" class="base" name="weight" v-model="data.weight" step="0.01" />
        </FormInputPayload>
        <FormInputPayload label-text="Давление" id="pressure">
            <Field id="pressure" type="number" class="base" name="pressure" v-model="data.pressure" step="0.01" />
        </FormInputPayload>
        <FormInputPayload label-text="Рост" id="height">
            <Field id="height" type="number" class="base" name="height" v-model="data.height" step="0.01" />
        </FormInputPayload>
        <FormSubmitButton :button-text="'Добавить'" />
    </BaseForm>
</template>