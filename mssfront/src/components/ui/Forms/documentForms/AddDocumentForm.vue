<script setup>
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue';
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
import { Field } from 'vee-validate';
import { object, string } from 'yup';
import Textarea from 'primevue/textarea';
import Dropdown from 'primevue/dropdown';
import { computed, ref, reactive } from 'vue';
import { useStore } from 'vuex';
import DocumentService from '@/../services/DocumentService';
import { useRouter } from 'vue-router';
const store = useStore()
const router = useRouter()
const errors = ref([])
const documentService = new DocumentService()
const documentTypes = computed(() => store.getters["doctorDocuments/getDocumentTypes"])
const patients = computed(() => store.getters["patients/getPatients"])
const userSlug = computed(() => store.getters["user/getSlug"])
const updateData = reactive({
    name: "",
    content: "",
    document_type_slug: "",
    user_slug: "",
    creator_slug: userSlug.value,
})
const validationSchema = object({
    name: string().required("Имя обязательно"),
    content: string().required("Содержание обязательно"),
    document_type_slug: string().required("Тип документа обязателен"),
    user_slug: string().required("Пациент обязателен"),
})
const submit = async () => {
    await documentService.createDocument(updateData)
        .then(response => {
            if (response.status == 200) {
                store.commit("doctorDocuments/addDocument", response.data)
                router.push("/doctor/documents/")
            }
        })
        .catch(error => errors.value.push(error.response.data.description))

}
</script>

<template>
    <BaseForm :schema="validationSchema" :errors="errors" @SubmitForm="submit">
        <FormInputPayload id="name" label-text="Название документа">
            <Field name="name" type="text" class="base" id="name" v-model="updateData.name" />
        </FormInputPayload>
        <FormInputPayload id="content" label-text="Содержание">
            <Field name="content" type="textarea" class="base" id="content" v-slot="{ field }" v-model="updateData.content">
                <Textarea v-bind="field" name="content" />
            </Field>
        </FormInputPayload>
        <FormInputPayload label-text="Тип документа" id="document_type_slug">
            <Field name="document_type_slug" v-slot="{ value, handleChange }" v-model="updateData.document_type_slug">
                <Dropdown @update:model-value="handleChange" :model-value="value" :options="documentTypes"
                    optionLabel="name" optionValue="slug" placeholder="Выберите тип документа" />
            </Field>
        </FormInputPayload>
        <FormInputPayload label-text="Пациент" id="user_slug">
            <Field name="user_slug" v-slot="{ value, handleChange }" v-model="updateData.user_slug">
                <Dropdown editable @update:model-value="handleChange" :model-value="value" :options="patients"
                    optionLabel="full_name" optionValue="slug" placeholder="Выберите пациента" />
            </Field>
        </FormInputPayload>
        <FormSubmitButton button-text="Добавить" />
    </BaseForm>
</template>