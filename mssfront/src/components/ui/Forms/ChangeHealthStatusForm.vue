<script setup>
import BaseForm from './Base/BaseForm.vue';
import Textarea from 'primevue/textarea';
import FormInputPayload from '../Payloads/FormInputPayload.vue';
import FormSubmitButton from '../Buttons/FormSubmitButton.vue';
import { object, string } from 'yup';
import { Field } from 'vee-validate';
import { defineProps, onBeforeMount, defineEmits } from 'vue';
import UserService from '@/../services/UserService';
import { useStore } from 'vuex';
import { useToast } from 'primevue/usetoast';
const store = useStore()
const toast = useToast()
const emit = defineEmits(["OnUpdateUserProfile"])
const userService = new UserService()
const props = defineProps({
    patientSlug: String,
    personalInfo: Object,
})
const updateData = ({})
const validationSchema = object({
    health_status: string().required("Это поле обязательно")
})
const update = async () => {
    updateData.user_slug = props.patientSlug
    await userService.updateUserPersonalInfo(updateData)
        .then(response => {
            if (response.status == 200) {
                console.log(response.data.personal_info)
                store.commit("treatments/setPatientInfo",
                    response.data.personal_info
                )
                toast.add({ severity: 'warn', summary: 'Успех', detail: 'Запись изменена', life: 3000 })
                emit("OnUpdateUserProfile")
            }
        })
        .catch(error => console.log(error))
}
onBeforeMount(() => {
    Object.assign(updateData, props.personalInfo)
})
</script>
<template>
    <BaseForm :schema="validationSchema" @submit-form="update">
        <FormInputPayload id="health_status">
            <Field name="health_status" type="textarea" class="base" id="health_status" v-slot="{ field }"
                v-model="updateData.health_status">
                <Textarea v-bind="field" name="health_status" />
            </Field>
        </FormInputPayload>
        <FormSubmitButton :button-text="'Изменить'" />
    </BaseForm>
</template>