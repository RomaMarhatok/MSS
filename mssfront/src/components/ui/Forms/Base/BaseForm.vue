<script setup>
import { defineProps, ref, defineEmits } from 'vue';
import { Form } from 'vee-validate'
import { ObjectSchema } from 'yup';
defineEmits(["SubmitForm"])
const props = defineProps({
    schema: ObjectSchema,
    errors: {
        type: Array,
        default: () => [],
    }
})

const invalidForm = ref(false)
</script>
<template>
    <Form as="div" :validation-schema="props.schema" @submit="$emit('SubmitForm'); invalidForm = false"
        @invalid-submit=" invalidForm = true " class="form__wrapper">
        <form class="flex flex-col" method="post">
            <div v-if=" invalidForm ">
                <p class="text-red-500">Введите верные данные</p>
            </div>
            <div v-if=" props.errors.length ">
                <p v-for="(  error, index  ) in   props.errors  " :key=" index " class="text-red-500">
                    {{ error }}
                </p>
            </div>
            <slot>Fallback content</slot>
        </form>
    </Form>
</template>
<style lang="css" scoped>
.form__wrapper {
    width: 80%;
}
</style>