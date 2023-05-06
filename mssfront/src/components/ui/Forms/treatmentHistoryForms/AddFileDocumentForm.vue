<script setup>
import { ref } from 'vue'
import { Field } from 'vee-validate';
import { mixed, object } from 'yup';
import FileUpload from 'primevue/fileupload';
import BaseForm from '../Base/BaseForm.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue';
const data = ref()
const fileUploader = async (event) => {
    const file = event.files[0]
    console.log(file)
    data.value = file
}
const validationSchema = object({
    file: mixed().required("Файл обязателен")
})
</script>
<template>
    <BaseForm :schema="validationSchema">
        <Field name="file">
            <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" customUpload class="w-full"
                @select="fileUploader($event)" choose-label="Выберите изображение" />
        </Field>
        <FormSubmitButton :button-text="'Добавить'" class="mt-4" />
    </BaseForm>
</template>