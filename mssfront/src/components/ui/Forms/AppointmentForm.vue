<script setup>
import '@vuepic/vue-datepicker/dist/main.css'

import { useStore } from 'vuex';
import { Field } from 'vee-validate'
import { string, object, date } from 'yup'
import { reactive, computed, ref, onBeforeMount, defineEmits } from 'vue'
import { useToast } from 'primevue/usetoast';

import AppointmentService from '@/../services/AppointmentService';

import Toast from 'primevue/toast';
import Dropdown from 'primevue/dropdown';
import OverlayPanel from 'primevue/overlaypanel'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

import BaseForm from './Base/BaseForm.vue';
import FormSubmitButton from '../Buttons/FormSubmitButton.vue';
import FormInputPayload from '@/components/ui/Payloads/FormInputPayload.vue'

const emit = defineEmits(["onAddAppointment"])
const toast = useToast()
const appointmentService = new AppointmentService()
const store = useStore()

const selectedDoctor = ref({})
const errors = ref([])
const op = ref(false)
const calendarRules = ref({
    hours: [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    seconds: 0,
    milliseconds: 0,
})

const data = reactive({
    doctor_specialization_slug: "",
    doctor_slug: "",
    date: null,
})

const userSlug = computed(() => store.getters["user/getSlug"])
const doctors = computed(() => store.getters["doctors/getAllDoctors"])
const buttonLabel = computed(() => Object.hasOwn(selectedDoctor.value, "doctor_full_name") ? selectedDoctor.value.doctor_full_name : 'Выберите доктора')
const doctorTypes = computed(() => Object.hasOwn(selectedDoctor.value, "doctor_types") ? selectedDoctor.value.doctor_types : [])

const validationSchema = object({
    doctor_specialization_slug: string().required("Специализация не может быть пустой"),
    date: date().required("Дата не может быть пустой").min(new Date(), "Нельзя устанавливать время в прошлом")
})

function submit() {
    data.patient_slug = userSlug.value
    data.doctor_slug = selectedDoctor.value.doctor_slug
    console.log(data)
    appointmentService.createPatientAppointments(data).then(response => {
        store.commit("appointments/addAppointment", response.data.appointment)
        emit("onAddAppointment")
    }).catch(error => {
        try {
            const responseErrors = error.response.data
            if (errors.value.indexOf(responseErrors.description) === -1) {
                errors.value.push(responseErrors.description)
            }
            toast.add({ severity: 'error', summary: 'Ошибка', detail: responseErrors.description, life: 3000 });
        }
        catch (e) {
            errors.value = []
        }
    })
}
const toggle = (event) => {
    op.value.toggle(event);
};
const onDoctorSelect = () => {
    op.value.hide()
}
onBeforeMount(() => {
    store.dispatch("doctors/fetchAllDoctors")
})
</script>

<template>
    <Toast />
    <div class="flex w-full justify-center flex-col my-12">
        <BaseForm @SubmitForm="submit" :schema="validationSchema" :errors="errors" class="w-full">
            <FormInputPayload id="date" label-text="Дата">
                <Field name="date" v-slot="{ value, handleChange }" v-model="data.date">
                    <v-date-picker @update:model-value="handleChange" :model-value="value" mode="dateTime" is24hr
                        :rules="calendarRules" expanded />
                </Field>
            </FormInputPayload>
            <FormInputPayload id="doctors" :label-text="'Доктора'">
                <OverlayPanel ref="op">
                    <DataTable v-model:selection="selectedDoctor" :value="doctors" selectionMode="single" :paginator="true"
                        :rows="4" @row-click="onDoctorSelect">
                        <Column field="doctor_full_name" header="Имя" />
                        <Column header="Специализация">
                            <template #body="slotProps">
                                <div v-for="dt in slotProps.data.doctor_types" :key="dt.slug">
                                    <p>{{ dt.name }}</p>
                                </div>
                            </template>
                        </Column>
                    </DataTable>
                </OverlayPanel>
                <button @click="toggle" type="button" class="select-doctor-button p-2">{{ buttonLabel }}</button>
            </FormInputPayload>
            <FormInputPayload label-text="Специализация доктора" id="doctor_specialization_slug">
                <Field name="doctor_specialization_slug" v-slot="{ value, handleChange }"
                    v-model="data.doctor_specialization_slug">
                    <Dropdown @update:model-value="handleChange" :model-value="value" :options="doctorTypes"
                        optionLabel="name" optionValue="slug" placeholder="Выберите специализацию врача" />
                </Field>
            </FormInputPayload>
            <FormSubmitButton :button-text="'Создать запись'"></FormSubmitButton>
        </BaseForm>
    </div>
</template>
<style lang="css" scoped>
.select-doctor-button {
    background-color: #0095ff;
    border: 1px solid transparent;
    border-radius: 3px;
    box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", "Liberation Sans", sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: 1.15385;
    margin: 0;
    outline: none;
    padding: 8px .8em;
    position: relative;
    text-align: center;
    text-decoration: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: baseline;
    white-space: nowrap;
}

.select-doctor-button:hover,
.select-doctor-button:focus {
    background-color: #07c;
}

.select-doctor-button:focus {
    box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);
}

.select-doctor-button:active {
    background-color: #0064bd;
    box-shadow: none;
}
</style>