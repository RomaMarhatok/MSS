<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'
import { reactive, computed, defineProps } from 'vue'
import BaseForm from './Base/BaseForm.vue';
import '@vuepic/vue-datepicker/dist/main.css'
import Datepicker from '@vuepic/vue-datepicker';
import FormSubmitButton from '../Buttons/FormSubmitButton.vue';
import Dropdown from 'primevue/dropdown';
const store = useStore()
const router = useRouter()
const userSlug = computed(() => store.state.user.slug)
const formData = reactive({
    doctor_specialization: "",
    doctor_slug: "",
    appointment_date: new Date(),
    patient_slug: userSlug.value
})
const props = defineProps({
    doctorTypes: {
        type: Array,
        default: () => [],
    },
    doctor_slug: {
        type: String
    },
    doctor_full_name: {
        type: String
    }
})
function submit() {
    formData.doctor_slug = props.doctor_slug
    store.dispatch("appointments/fetchCreateAppointemtns", formData).then(responseStatus => {
        if (responseStatus == 200) {
            store.dispatch("response/resetErrors")
            router.push("/home/")
        }
    })
}

</script>

<template>
    <div class="flex w-full justify-center flex-col my-12">
        <BaseForm @SubmitForm="submit">
            <p>{{ props.doctor_full_name }}</p>
            <Datepicker v-model="formData.appointment_date" placeholder="Input date ..." text-input></Datepicker>
            <div class="card flex justify-content-center">
                <Dropdown v-model="formData.doctor_specialization" option-value="slug" option-label="name"
                    :options="props.doctorTypes" class="w-full md:w-14rem"></Dropdown>
            </div>
            <FormSubmitButton :button-text="'create appointment'"></FormSubmitButton>
        </BaseForm>
    </div>
</template>
<style>
.p-dropdown-items-wrapper {
    z-index: 0;
}
</style>