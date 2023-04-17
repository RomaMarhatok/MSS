<script setup>
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"

import { string, object } from 'yup'
import { Field } from 'vee-validate'
import { useStore } from 'vuex'
import { onBeforeMount, computed, ref, reactive } from 'vue';

import { useToast } from "primevue/usetoast";
import Tag from 'primevue/tag';
import Dialog from "primevue/dialog";
import Menu from 'primevue/menu'
import Textarea from 'primevue/textarea'
import Toast from 'primevue/toast';

import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import AddTreatmentHistoryForm from "@/components/ui/Forms/AddTreatmentHistoryForm.vue";
import BaseForm from "@/components/ui/Forms/Base/BaseForm.vue";
import FormInputPayload from "@/components/ui/Payloads/FormInputPayload.vue";
import FormSubmitButton from "@/components/ui/Buttons/FormSubmitButton.vue";

import TreatmentHistoryService from "@/../services/TreatmentHistoryService"
// store
const store = useStore()

//toast
const toast = useToast()
//init services
const treatmentHistoryService = new TreatmentHistoryService()

//refs
const imageDialog = ref(false)

// refs add ts
const addTreatmentHistoryDialog = ref(false)
const treatmentHistoryListMenu = ref(false)
const selectedIndexOfImage = ref(-1)
const addTreatmentHistoryMenu = ref([
    {
        label: "Действия",
        items: [
            {
                label: "Добавить",
                icon: 'pi pi-plus',
                command: () => {
                    addTreatmentHistoryDialog.value = !addTreatmentHistoryDialog.value
                }
            }
        ]
    }
])

// refs change ts
const updateData = reactive({})
const treatmentHistoryIsSelected = ref(false)
const selectedTSSlug = ref("")
const changeTreatmentHistoryMenu = ref(false)
const swapOnChangeForm = ref(false)
const changeMenu = ref([
    {
        label: "Действия",
        items: [
            {
                label: "Изменить",
                icon: 'pi pi-plus',
                command: () => {
                    Object.assign(updateData, selectedTreatmentHistoryAndImages.value.treatment_history)
                    console.log(updateData)
                    swapOnChangeForm.value = !swapOnChangeForm.value
                }
            }
        ]
    }
])

//schema
const validationSchema = object({
    title: string().required("Название обязательно"),
    short_description: string(),
    description: string().required("Описание обязательно"),
    conclusion: string().required("Заключение обязательно")
})
//methods

// main data
const selectedAppointment = computed(() => store.getters["appointment/getSelectedAppointment"])
const treatmentHistories = computed(() => {
    return store.getters["treatments/getTreatmentsHistories"]
})
const patientPersonalInfo = computed(() => {
    return store.getters["treatments/getPatientInfo"]
})


const selectedTreatmentHistoryAndImages = computed(() => store.getters["treatments/getTreatmentHistoryBySlug"](selectedTSSlug.value))


const toggleListMenu = (event) => {
    treatmentHistoryListMenu.value.toggle(event);
}
const toggleChangeMenu = (event) => {
    changeTreatmentHistoryMenu.value.toggle(event)
}
const selectTreatementHistory = (tsSlug, IsSelected) => {
    selectedTSSlug.value = tsSlug
    treatmentHistoryIsSelected.value = IsSelected
    changeTreatmentHistoryMenu.value = false
    swapOnChangeForm.value = false
}
const selectImage = (index) => {
    selectedIndexOfImage.value = index
}
const updateSubmit = () => {
    updateData.treatment_history_slug = selectedTreatmentHistoryAndImages.value.treatment_history.slug
    treatmentHistoryService.updateTreatmentHistory(updateData).then(
        response => {
            if (response.status == 200) {
                toast.add({ severity: 'warn', summary: 'Успех', detail: 'Запись изменена', life: 3000 })
                changeTreatmentHistoryMenu.value = false
                swapOnChangeForm.value = false
                store.commit("treatments/updateTreatmentHistory", response.data.treatment_history)
            }
        }
    ).catch(error => console.log(error))
}
onBeforeMount(() => {
    store.dispatch("treatments/fetchTreatmentsHistories",
        {
            patientSlug: selectedAppointment.value.patient.slug,
            doctorSpecializationSlug: selectedAppointment.value.doctor_specialization.slug
        }
    )
})


</script>
<template>
    <Toast />
    <HeaderLayout />
    <main class="main-flex__section">
        <section class="patinet_info__section">
            <div class="flex bg__section bordered__section">
                <div class="w-1/3 p-4">
                    <p class="text-xl font-bold text-center">Пациент</p>
                    <p class="text-2xl font-bold text-center">
                        {{ patientPersonalInfo.first_name }} {{ patientPersonalInfo.second_name }}
                    </p>
                    <p class="text-slate-400 font-thin text-center">{{ patientPersonalInfo.email }}</p>
                    <div class="flex flex-col">
                        <p class="pb-4 text-slate-400 font-normal">Пол</p>
                        <p class="pb-2 border-b-slate-200 border-b-2 font-thin">{{ patientPersonalInfo.gender }}ale
                        </p>
                    </div>
                    <div class="flex flex-col">
                        <p class="pb-4 text-slate-400 font-normal">Возраст</p>
                        <p class="pb-2 border-b-slate-200 border-b-2 font-thin">{{ patientPersonalInfo.age }}</p>
                    </div>
                </div>
                <div class="flex flex-col p-4">
                    <div class="grid grid-cols-2 grid-rows-2 gap-9">
                        <div class="col-span-2">
                            <p class="pb-4 text-slate-400 font-normal ">Здоровье</p>
                            <p class="font-thin">{{ patientPersonalInfo.health_status }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <div class="flex gap-4">
            <section class="w-5/12">
                <div class="flex flex-col p-2 gap-3 bordered__section bg__section w-full">
                    <div class="flex justify-between">
                        <p class="text-2xl font-bold text-center">Истории лечения</p>
                        <button class="p-panel-header-icon p-link mr-2" @click="toggleListMenu">
                            <span class="pi pi-cog"></span>
                        </button>
                        <Menu ref="treatmentHistoryListMenu" :model="addTreatmentHistoryMenu" id="config_menu" popup />
                    </div>
                    <div v-for="(ts, index) in treatmentHistories" :key="index" class="treatment_history__item bg-white"
                        @click="selectTreatementHistory(ts.treatment_history.slug, true)">
                        <div class="flex justify-between">
                            <div class="flex gap-1 text-sm font-medium justify-end">
                                <Tag :value="'Создано ' + ts.treatment_history.string_date" severity="info" />
                            </div>
                            <div class="flex justify-end text-sm font-medium">
                                <Tag :value="'Создатель' + ts.treatment_history.doctor.full_name" severity="success" />
                            </div>
                        </div>
                        <div>
                            <p class="font-medium pb-2">{{ ts.treatment_history.title }}</p>
                            <Tag :value="'кол-во изображений ' + ts.treatment_history.count_of_images" severity="info" />
                        </div>
                    </div>
                </div>
            </section>
            <section class="flex treatment_history__section bg__section bordered__section w-7/12">
                <div v-if="!treatmentHistoryIsSelected" class="self-center w-full items-center">
                    <p class="text-center">История лечения не выбрана</p>
                </div>
                <div v-else class="flex flex-col p-1 justify-start w-full">
                    <button class="p-panel-header-icon p-link mr-2" @click="toggleChangeMenu">
                        <span class="pi pi-cog"></span>
                    </button>
                    <Menu ref="changeTreatmentHistoryMenu" :model="changeMenu" id="config_change_menu" popup />
                    <div v-if="!swapOnChangeForm">
                        <div class="flex-col p-2">
                            <p>Название</p>
                            <p>{{ selectedTreatmentHistoryAndImages.treatment_history.title }}</p>
                        </div>
                        <div class="flex-col p-2">
                            <p>Описание</p>
                            <p>{{ selectedTreatmentHistoryAndImages.treatment_history.description }}</p>
                        </div>
                        <div class="flex-col p-2">
                            <p>Заключение</p>
                            <p>{{ selectedTreatmentHistoryAndImages.treatment_history.conclusion }}</p>
                        </div>
                        <div class="p-2">
                            <p>Прилогающиеся изображения</p>
                            <div v-if="!selectedTreatmentHistoryAndImages.images_for_analyzes.length">
                                <p>НЕТ</p>
                            </div>
                            <div v-else v-for="(img, index) in selectedTreatmentHistoryAndImages.images_for_analyzes"
                                :key="index">
                                <p @click="imageDialog = true; selectImage(index);" class="cursor-pointer">{{
                                    img.description }}</p>
                            </div>
                        </div>
                    </div>
                    <div v-else class="flex flex-col w-full gap-4">
                        <div>
                            <BaseForm :schema="validationSchema" @SubmitForm="updateSubmit" class="w-full h-full">
                                <FormInputPayload id="title" label-text="Название записи">
                                    <Field name="title" type="text" class="base" id="title" v-model="updateData.title" />
                                </FormInputPayload>
                                <FormInputPayload id="short_description" label-text="Краткое описание">
                                    <Field name="short_description" type="textarea" class="base" id="short_description"
                                        v-slot="{ field }" v-model="updateData.short_description">
                                        <Textarea v-bind="field" name="short_description" />
                                    </Field>
                                </FormInputPayload>
                                <FormInputPayload id="description" label-text="Описание">
                                    <Field name="description" type="textarea" class="base" id="description"
                                        v-slot="{ field }" v-model="updateData.description">
                                        <Textarea v-bind="field" name="description" />
                                    </Field>
                                </FormInputPayload>
                                <FormInputPayload id="conclusion" label-text="Заключение">
                                    <Field name="conclusion" type="textarea" class="base" id="conclusion" v-slot="{ field }"
                                        v-model="updateData.conclusion">
                                        <Textarea v-bind="field" name="conclusion" />
                                    </Field>
                                </FormInputPayload>
                                <FormSubmitButton button-text="Изменить" />
                            </BaseForm>
                        </div>
                        <div class="bordered__section w-full">
                            <p class="text-center text-lg">Список изображений</p>
                            <div class="flex flex-col">
                                <div v-if="!selectedTreatmentHistoryAndImages.images_for_analyzes.length">
                                    <p>НЕТ</p>
                                </div>
                                <div v-else v-for="(img, index) in selectedTreatmentHistoryAndImages.images_for_analyzes"
                                    :key="index" class="bg-white rounded-md flex p-2 justify-between">
                                    <div>
                                        <p @click="imageDialog = true; selectImage(index);" class="cursor-pointer w-full">{{
                                            img.description }}</p>
                                    </div>
                                    <div>
                                        <span><i class="pi pi-times"></i></span>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </section>
        </div>
        <Dialog v-model:visible="imageDialog" modal header="Изображение" :style="{ width: '70vw' }">
            <p>{{ selectedTreatmentHistoryAndImages.images_for_analyzes[selectedIndexOfImage].description }}</p>
            <img :src="selectedTreatmentHistoryAndImages.images_for_analyzes[selectedIndexOfImage].image" />
        </Dialog>
        <Dialog v-model:visible="addTreatmentHistoryDialog" modal header="Добавить запись" :style="{ width: '50vw' }">
            <AddTreatmentHistoryForm :patient_slug="selectedAppointment.patient.slug"
                :doctor_slug="selectedAppointment.doctor.slug" />
        </Dialog>
    </main>
</template>
<style lang="css" scoped>
.patinet_info__section {
    border-radius: 1rem;
}

.bg__section {
    background-color: rgba(110, 131, 165, 0.103);
}

.bordered__section {
    border: 1px solid rgb(218, 218, 218);
    border-radius: 5px;
}

.treatment_history__item {
    border: 1px solid rgb(218, 218, 218);
    border-radius: 10px;
    padding: 0.5em;
}

.flex-section {
    display: flex;
    gap: 1em;
}

.main-flex__section {
    display: flex;
    gap: 1em;
    padding: 1em;
    flex-direction: column;
}

@media screen and (max-width:900px) {
    .flex-section {
        flex-direction: column;
    }

    .patinet_info__section {
        width: 100%;
    }
}

@media screen and (max-width: 1250px) {
    .main-flex__section {
        flex-direction: column;
    }

    .treatment_history__section {
        width: 100%;
    }

    .flex-section {
        justify-content: space-evenly;
    }

}
</style>