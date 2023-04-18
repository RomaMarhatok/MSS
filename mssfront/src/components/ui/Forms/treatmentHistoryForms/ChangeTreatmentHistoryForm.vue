<script setup>
import { Field } from 'vee-validate'
import { reactive, defineProps, onBeforeMount, defineEmits } from 'vue'
import { useStore } from 'vuex'
import { useToast } from "primevue/usetoast";
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'
import BaseTreatmentHistoryForm from './BaseTreatmentHistoryForm.vue';
import TreatmentHistoryService from '@/../services/TreatmentHistoryService'
import Textarea from 'primevue/textarea'
const emit = defineEmits(["changeSuccess"])
const store = useStore()
const toast = useToast()
const props = defineProps({
    treatmentHistory: {
        type: Object,
        default: () => { }
    },
})
const updateData = reactive({})
const treatmentHistoryService = new TreatmentHistoryService()
const submit = () => {
    updateData.treatment_history_slug = props.treatmentHistory.slug
    treatmentHistoryService.updateTreatmentHistory(updateData).then(
        response => {
            if (response.status == 200) {
                toast.add({ severity: 'warn', summary: 'Успех', detail: 'Запись изменена', life: 3000 })
                store.commit("treatments/updateTreatmentHistory", response.data.treatment_history)
                emit("changeSuccess", response.status)
            }
        }
    ).catch(error => console.log(error))
}
onBeforeMount(() => {
    Object.assign(updateData, props.treatmentHistory)
})
</script>
<template>
    <BaseTreatmentHistoryForm :submit="submit">
        <FormInputPayload id="title" label-text="Название записи">
            <Field name="title" type="text" class="base" id="title" v-model="updateData.title" />
        </FormInputPayload>
        <FormInputPayload id="short_description" label-text="Краткое описание (необязательно)">
            <Field name="short_description" type="textarea" class="base" id="short_description" v-slot="{ field }"
                v-model="updateData.short_description">
                <Textarea v-bind="field" name="short_description" />
            </Field>
        </FormInputPayload>
        <FormInputPayload id="description" label-text="Описание">
            <Field name="description" type="textarea" class="base" id="description" v-slot="{ field }"
                v-model="updateData.description">
                <Textarea v-bind="field" name="description" />
            </Field>
        </FormInputPayload>
        <FormInputPayload id="conclusion" label-text="Заключение">
            <Field name="conclusion" type="textarea" class="base" id="conclusion" v-slot="{ field }"
                v-model="updateData.conclusion">
                <Textarea v-bind="field" name="conclusion" />
            </Field>
        </FormInputPayload>
        <FormSubmitButton button-text="Изменить" />
    </BaseTreatmentHistoryForm>
</template>