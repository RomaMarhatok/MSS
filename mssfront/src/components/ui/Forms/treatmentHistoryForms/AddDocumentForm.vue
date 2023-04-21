<script setup>
import { Field } from 'vee-validate';
import { string, object } from 'yup'
import { onBeforeMount, computed, ref, defineProps, defineEmits } from 'vue'
import { useStore } from 'vuex';

import TreatmentHistoryService from '@/../services/TreatmentHistoryService';
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue';
import FormInputPayload from '../../Payloads/FormInputPayload.vue';
import FormSubmitButton from '../../Buttons/FormSubmitButton.vue';
import Dropdown from 'primevue/dropdown';
const store = useStore()
const treatmentHistoryService = new TreatmentHistoryService()
const props = defineProps({
    treatmentHistorySlug: String
})
const emit = defineEmits(["onAddDocument"])
const errors = ref([])
const documentSlug = ref("")
const documents = computed(() => store.getters["doctorDocuments/getDocuments"])
const slug = computed(() => store.getters["user/getSlug"])
const validationSchema = object({
    document_slug: string().required("Документ обязателен")
})
const submit = async () => {
    const data = {
        treatment_history_slug: props.treatmentHistorySlug,
        document_slug: documentSlug.value,
    }
    console.log(data)
    await treatmentHistoryService.createTreatmentHistoryDocument(data).then(response => {
        store.commit("treatments/addDocument",
            {
                document: response.data.document,
                treatmentHistorySlug: props.treatmentHistorySlug
            })
        emit("onAddDocument")
    }).catch(error => errors.value.push(error.response.data.description))
}
onBeforeMount(() => {
    store.dispatch("doctorDocuments/fetchDocuments", slug.value)
})
</script>
<template>
    <BaseForm :schema="validationSchema" :errors="errors" @SubmitForm="submit" class="w-full">
        <FormInputPayload label-text="Документ" id="document_slug">
            <Field name="document_slug" v-slot="{ value, handleChange }" v-model="documentSlug">
                <Dropdown editable @update:model-value="handleChange" :model-value="value" :options="documents"
                    optionLabel="name" optionValue="slug" placeholder="Выберите пациента" />
            </Field>
        </FormInputPayload>
        <FormSubmitButton :button-text="'Добавить документ'" />
    </BaseForm>
</template>