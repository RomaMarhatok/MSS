<script setup>
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue';
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import Textarea from 'primevue/textarea';
import Dropdown from 'primevue/dropdown';

import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { Field } from 'vee-validate';
import { object, string } from 'yup';
import { computed, ref, reactive, onBeforeMount, defineProps } from 'vue';

import DocumentService from '@/../services/DocumentService';
const props = defineProps({
    document: {
        type: Object,
        default: () => { }
    }
})
const store = useStore()
const router = useRouter()
const errors = ref([])
const documentService = new DocumentService()
const documentTypes = computed(() => store.getters["doctorDocuments/getDocumentTypes"])
const patients = computed(() => store.getters["patients/getPatients"])
const userSlug = computed(() => store.getters["user/getSlug"])
const data = reactive({})
const validationSchema = object({
    name: string().required("Имя обязательно"),
    content: string().required("Содержание обязательно"),
    document_type_slug: string().required("Тип документа обязателен"),
    user_slug: string().required("Пациент обязателен"),
})
const submit = async () => {
    data.creator_slug = userSlug.value
    data.document_slug = props.document.slug
    await documentService.updateDocument(data)
        .then(response => {
            if (response.status == 200) {
                store.commit("doctorDocuments/changeDocument", response.data.document)
                router.push("/doctor/documents/")
            }
        })
        .catch(error => errors.value.push(error.response.data.description))
}
onBeforeMount(() => {
    console.log(data)
    console.log(props.document)
    Object.assign(data, props.document)
    console.log(data)

})
</script>

<template>
    <BaseForm :schema="validationSchema" :errors="errors" @SubmitForm="submit">
        <FormInputPayload id="name" label-text="Название документа">
            <Field name="name" type="text" class="base" id="name" v-model="data.name" />
        </FormInputPayload>
        <FormInputPayload id="content" label-text="Содержание">
            <Field name="content" type="textarea" class="base" id="content" v-slot="{ field }" v-model="data.content">
                <Textarea v-bind="field" name="content" />
            </Field>
        </FormInputPayload>
        <FormInputPayload label-text="Тип документа" id="document_type_slug">
            <Field name="document_type_slug" v-slot="{ value, handleChange }" v-model="data.document_type_slug">
                <Dropdown @update:model-value="handleChange" :model-value="value" :options="documentTypes"
                    optionLabel="name" optionValue="slug" placeholder="Выберите тип документа" />
            </Field>
        </FormInputPayload>
        <FormInputPayload label-text="Пациент" id="user_slug">
            <Field name="user_slug" v-slot="{ value, handleChange }" v-model="data.user_slug">
                <Dropdown editable @update:model-value="handleChange" :model-value="value" :options="patients"
                    optionLabel="full_name" optionValue="slug" placeholder="Выберите пациента" />
            </Field>
        </FormInputPayload>
        <FormSubmitButton button-text="Изменить" />
    </BaseForm>
</template>