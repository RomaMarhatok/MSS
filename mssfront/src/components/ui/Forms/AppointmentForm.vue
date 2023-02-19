<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'
import { reactive, computed } from 'vue'
import BaseForm from './Base/BaseForm.vue';
import '@vuepic/vue-datepicker/dist/main.css'
import Datepicker from '@vuepic/vue-datepicker';
import FormSubmitButton from '../Buttons/FormSubmitButton.vue';
import DoctorTypeSelector from '@/components/common/Selectors/DoctorTypeSelector.vue';
import DoctorSelector from '@/components/common/Selectors/DoctorSelector.vue';
const store = useStore()
const router = useRouter()
const userSlug = computed(() => store.state.user.slug)
const formData = reactive({
    doctor_specialization: "",
    doctor_slug: "",
    appointment_date: new Date(),
    patient_slug: userSlug.value
})
const errors = computed(() => store.getters["responseErrors/generalErrors"])
const doctorTypes = computed(() => {
    return store.state.doctors.doctorTypes
})
const doctors = computed(() => {
    return formData.doctor_specialization.length == 0 ? store.state.doctors.doctors : store.getters["doctors/getDoctorByDoctorTypeSlug"](formData.doctor_specialization)
})
function submit() {
    store.dispatch("user/fetchCreateAppointemtns", formData).then(responseStatus => {
        console.log(responseStatus)
        console.log((Object.keys(errors.value).length))
        if ((Object.keys(errors.value).length === 0) && responseStatus == 200) {
            store.dispatch("responseErrors/clearErrors")
            router.push("/user/" + store.state.user.slug + "/home/")
        }
    })

}
</script>

<template>
    <div class="flex w-full justify-center ">
        <BaseForm @SubmitForm="submit">
            <Datepicker v-model="formData.appointment_date" placeholder="Input date ..." text-input></Datepicker>
            <DoctorTypeSelector v-model="formData.doctor_specialization" :doctor-types="doctorTypes">
            </DoctorTypeSelector>
            <DoctorSelector v-model="formData.doctor_slug" :doctors="doctors"></DoctorSelector>
            <FormSubmitButton :button-text="'create appointment'"></FormSubmitButton>
        </BaseForm>
    </div>
</template>