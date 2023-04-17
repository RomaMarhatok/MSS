<script setup>
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"

import { useStore } from 'vuex'
import { onBeforeMount, computed, ref } from 'vue';
import Tag from 'primevue/tag';
import Menu from 'primevue/menu'
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import AddTreatmentHistoryDialog from '@/components/ui/Dialogs/addTreatmentHistoryDialog.vue'
import SingleTreatmentHistorySection from "@/components/ui/Sections/SingleTreatmentHistorySection.vue"

const store = useStore()
const treatmentHistoryIsSelected = ref(false)
const selectedTSSlug = ref("")
const selectedAppointment = computed(() => store.getters["appointment/getSelectedAppointment"])
const treatmentHistories = computed(() => {
    return store.getters["treatments/getTreatmentsHistories"]
})
const patientPersonalInfo = computed(() => {
    return store.getters["treatments/getPatientInfo"]
})
const selectTreatementHistory = (tsSlug, IsSelected) => {
    selectedTSSlug.value = tsSlug
    treatmentHistoryIsSelected.value = IsSelected
    swapOnChangeForm.value = false
}
onBeforeMount(() => {
    store.dispatch("treatments/fetchTreatmentsHistories",
        {
            patientSlug: selectedAppointment.value.patient.slug,
            doctorSpecializationSlug: selectedAppointment.value.doctor_specialization.slug
        }
    )
})

const menuLabel = computed(() => !swapOnChangeForm.value ? "Изменить" : "Отмена")
const menuIcon = computed(() => !swapOnChangeForm.value ? 'pi pi-plus' : 'pi pi-minus')
const swapOnChangeForm = ref(false)
const menu = ref(false)
const menuOptions = ref([
    {
        label: "Действия",
        items: [
            {
                label: menuLabel,
                icon: menuIcon,
                command: () => {
                    swapOnChangeForm.value = !swapOnChangeForm.value
                }
            }
        ]
    }
])
const toggleMenu = (event) => {
    menu.value.toggle(event)
}

</script>
<template>
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
        <div class="flex-section">
            <section class="treatment_history__section w-5/12">
                <div class="bordered__section bg__section flex flex-col p-2 gap-3 w-full">
                    <div class="flex justify-between">
                        <p class="text-2xl font-bold text-center">Истории лечения</p>
                        <AddTreatmentHistoryDialog />
                    </div>
                    <div v-for="(ts, index) in treatmentHistories" :key="index" class="treatment_history__item bg-white"
                        @click="selectTreatementHistory(ts.treatment_history.slug, true)">
                        <div class="flex justify-between">
                            <div class="flex gap-1 text-sm font-medium justify-end">
                                <Tag :value="'Создано ' + ts.treatment_history.string_date" severity="info" />
                            </div>
                            <div class="flex justify-end text-sm font-medium">
                                <Tag :value="'Создатель ' + ts.treatment_history.doctor.full_name" severity="success" />
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
                    <button class="p-panel-header-icon p-link mr-2" @click="toggleMenu">
                        <span class="pi pi-cog"></span>
                    </button>
                    <Menu ref="menu" :model="menuOptions" id="config_change_menu" popup />
                    <SingleTreatmentHistorySection :treatment-history-slug="selectedTSSlug"
                        :swap-on-change-form="swapOnChangeForm" />
                </div>
            </section>
        </div>
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