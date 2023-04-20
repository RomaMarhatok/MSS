<script setup>
import { string, object } from 'yup'
import { defineProps } from 'vue'
import BaseForm from '@/components/ui/Forms/Base/BaseForm.vue'

import Toast from 'primevue/toast';

const props = defineProps({
    submit: Function
})

const validationSchema = object({
    title: string().required("Название обязательно"),
    short_description: string(),
    description: string().required("Описание обязательно"),
    conclusion: string().required("Заключение обязательно")
})

</script>
<template>
    <Toast />
    <BaseForm :schema="validationSchema" @SubmitForm="props.submit" class="w-full">
        <slot></slot>
    </BaseForm>
</template>