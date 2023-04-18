<script setup>
import { string, object } from 'yup'
import { Field } from 'vee-validate';
import { reactive, defineProps, defineEmits, ref } from 'vue'
import { useStore } from 'vuex';
import FileUpload from 'primevue/fileupload'
import Textarea from 'primevue/textarea'
import BaseForm from '../Base/BaseForm.vue';
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue';
import FormSubmitButton from '@/components/ui/Buttons/FormSubmitButton.vue'
import TreatmentHistoryService from '@/../services/TreatmentHistoryService';
const emit = defineEmits(["onAddImage"])
const store = useStore()
const props = defineProps({
    treatmentHistorySlug: String,
})
const errors = ref([])
const treatmentHistoryService = new TreatmentHistoryService()
const data = reactive({
    description: "",
    image: null,
})
const imageUploader = async (event) => {
    const file = event.files[0]
    console.log(file)
    data.image = file
}
const validationSchema = object({
    description: string().required("Описание обязательно")
})
const submit = async () => {
    const formData = new FormData()
    formData.append("image", data.image)
    formData.append("description", data.description)
    formData.append("treatment_history_slug", props.treatmentHistorySlug)
    await treatmentHistoryService.createTreatmentHistoryImageForAnalyze(formData).then(response => {
        const img = response.data.image_for_analyze
        store.commit("treatments/addImageForAnalyze", {
            img,
            treatmentHistorySlug: props.treatmentHistorySlug,
        })
        emit("onAddImage")
    }).catch(error => {
        if (error.response.status == 400) {
            for (let key in error.response.data) {
                errors.value.push(error.response.data[key])
            }
            errors.value = errors.value.flat(3)
        }

    })
    console.log(errors)
}
</script>
<template>
    <div class="flex gap-4">
        <BaseForm class="w-full" @SubmitForm="submit" :schema="validationSchema" :errors="errors">
            <FormInputPayload id="description" label-text="Описание">
                <Field name="description" type="textarea" class="base" id="description" v-slot="{ field }"
                    v-model="data.description">
                    <Textarea v-bind="field" name="description" />
                </Field>
            </FormInputPayload>
            <div class="flex flex-col">
                <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" customUpload class="w-full"
                    @select="imageUploader($event)" choose-label="Выберите изображение" />
            </div>
            <FormSubmitButton :button-text="'Добавить'" class="mt-4" />
        </BaseForm>
    </div>
</template>
<style lang="css" scoped>
.font {
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 1.15em;
    line-height: 30px;
    font-weight: 600;
    position: relative;
}
</style>
