<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'
import { reactive, computed } from 'vue'
import BaseForm from './Base/BaseForm.vue';
import '@vuepic/vue-datepicker/dist/main.css'
import Datepicker from '@vuepic/vue-datepicker';
import FormSubmitButton from '../Buttons/FormSubmitButton.vue';
import BaseSelector from '@/components/common/Selectors/Base/BaseSelector.vue';
const store = useStore()
const router = useRouter()
const userSlug = computed(() => store.state.user.slug)
const formData = reactive({
    doctor_specialization: "",
    doctor_slug: "",
    appointment_date: new Date(),
    patient_slug: userSlug.value
})
const doctorTypes = computed(() => {
    return store.state.doctors.doctorTypes
})
const doctors = computed(() => {
    console.log(formData.doctor_specialization)
    return formData.doctor_specialization.length == 0 ? store.state.doctors.doctors : store.getters["doctors/getDoctorByDoctorTypeSlug"](formData.doctor_specialization)
})
function submit() {
    store.dispatch("appointments/fetchCreateAppointemtns", formData).then(responseStatus => {
        if (responseStatus == 200) {
            store.dispatch("response/resetErrors")
            router.push("/home/")
        }
    })

}
</script>

<template>
    <div class="flex w-full justify-center ">
        <BaseForm @SubmitForm="submit">
            <Datepicker v-model="formData.appointment_date" placeholder="Input date ..." text-input></Datepicker>
            <BaseSelector v-model="formData.doctor_specialization" :selection-values="doctorTypes"></BaseSelector>
            <BaseSelector v-model="formData.doctor_slug" :selection-values="doctors"></BaseSelector>
            <FormSubmitButton :button-text="'create appointment'"></FormSubmitButton>
        </BaseForm>
    </div>
</template>