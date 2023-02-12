<script setup>
import { useStore } from 'vuex';
import BaseForm from './Base/BaseForm.vue';
import { reactive, computed } from 'vue'
import '@vuepic/vue-datepicker/dist/main.css'
import Datepicker from '@vuepic/vue-datepicker';
import FormSubmitButton from '../Buttons/FormSubmitButton.vue';
import DoctorTypeSelector from '@/components/common/Selectors/DoctorTypeSelector.vue';
import DoctorSelector from '@/components/common/Selectors/DoctorSelector.vue';
const store = useStore()
// const date = ref(new Date())
const userSlug = computed(() => store.state.user.slug)
const formData = reactive({
    selectedDoctorTypeSlug: "",
    doctor_slug: "",
    appointment_date: new Date(),
    patient_slug: userSlug.value
})
const doctorTypes = computed(() => {
    return store.state.doctors.doctorTypes
})
const doctors = computed(() => {
    return formData.selectedDoctorTypeSlug.length == 0 ? store.state.doctors.doctors : store.getters["doctors/getDoctorByDoctorTypeSlug"](formData.selectedDoctorTypeSlug)
})
function submit() {
    console.log(formData)
}
</script>

<template>
    <div class="flex w-full justify-center ">
        <BaseForm @SubmitForm="submit">
            <Datepicker v-model="formData.appointment_date" placeholder="Input date ..." text-input></Datepicker>
            <DoctorTypeSelector v-model="formData.selectedDoctorTypeSlug" :doctor-types="doctorTypes">
            </DoctorTypeSelector>
            <DoctorSelector v-model="formData.doctor_slug" :doctors="doctors"></DoctorSelector>
            <FormSubmitButton :button-text="'create appointment'"></FormSubmitButton>
        </BaseForm>
    </div>
</template>