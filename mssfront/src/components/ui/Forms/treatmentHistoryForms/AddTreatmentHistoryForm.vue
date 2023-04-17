<script setup>
import { Field } from 'vee-validate'
import { reactive, defineProps } from 'vue'
import { useStore } from 'vuex'
import { useToast } from "primevue/usetoast";
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'
import BaseTreatmentHistoryForm from './BaseTreatmentHistoryForm.vue';
import TreatmentHistoryService from '@/../services/TreatmentHistoryService'
import Textarea from 'primevue/textarea'
const store = useStore()
const toast = useToast()
const props = defineProps({
    patient_slug: String,
    doctor_slug: String,
})
const data = reactive({
    date: new Date(),
    title: "",
    short_description: "",
    description: "",
    conclusion: "",
    patient_slug: props.patient_slug,
    doctor_slug: props.doctor_slug,
})
const treatmentHistoryService = new TreatmentHistoryService()
const submit = () => {
    data.date = new Date()
    console.log(data)
    treatmentHistoryService.createTreatmentHistory(data)
        .then(response => {
            if (response.status == 200) {
                toast.add({ severity: 'success', summary: 'Успех', detail: 'Запись добавлена', life: 3000 });
                store.commit("treatments/addTreatmentHistory", response.data)
            }
        }).catch(error => console.log(error))
}

</script>
<template>
    <BaseTreatmentHistoryForm :submit="submit">
        <FormInputPayload id="title" label-text="Название записи">
            <Field name="title" type="text" class="base" id="title" v-model="data.title" />
        </FormInputPayload>
        <FormInputPayload id="short_description" label-text="Краткое описание (необязательно)">
            <Field name="short_description" type="textarea" class="base" id="short_description" v-slot="{ field }"
                v-model="data.short_description">
                <Textarea v-bind="field" name="short_description" />
            </Field>
        </FormInputPayload>
        <FormInputPayload id="description" label-text="Описание">
            <Field name="description" type="textarea" class="base" id="description" v-slot="{ field }"
                v-model="data.description">
                <Textarea v-bind="field" name="description" />
            </Field>
        </FormInputPayload>
        <FormInputPayload id="conclusion" label-text="Заключение">
            <Field name="conclusion" type="textarea" class="base" id="conclusion" v-slot="{ field }"
                v-model="data.conclusion">
                <Textarea v-bind="field" name="conclusion" />
            </Field>
        </FormInputPayload>
        <FormSubmitButton button-text="Добавить" />
    </BaseTreatmentHistoryForm>
</template>