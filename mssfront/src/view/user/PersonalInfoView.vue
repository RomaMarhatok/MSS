<script setup>
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"

import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router';
import { onBeforeMount, computed, ref } from 'vue';
import { useToast } from 'primevue/usetoast';

import Tag from 'primevue/tag';
import Dialog from 'primevue/dialog';
import SelectButton from "primevue/selectbutton";
import Toast from 'primevue/toast'

import HeaderLayout from '@/components/layout/HeaderLayout.vue'
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
import AppointmentForm from '@/components/ui/Forms/AppointmentForm.vue'
import PhysicalParametersSection from "@/components/ui/Sections/PhysicalParametersSection.vue";

const toast = useToast()
const store = useStore()
const route = useRoute()
const router = useRouter()
const select = ref("upcoming")
const visible = ref(false)
const options = ref([
    {
        name: "Предстоящие записи",
        value: "upcoming",
    },
    {
        name: "Прошедшие записи",
        value: "past"
    },
    {
        name: "Календарь",
        value: "calendar",
    },
    {
        name: "Физ. параметры",
        value: "physical"
    }
])
const personalInfo = computed(() => store.getters["user/getPersonalInfo"])
const upComingAppointments = computed(() => store.getters["appointments/getUpComingAppointments"])
const pastAppointments = computed(() => store.getters["appointments/getPastAppointments"])
const getAppointments = computed(() => select.value == 'upcoming' ? upComingAppointments.value : pastAppointments.value)
const newestDocuments = computed(() => store.getters["documents/getNewestDocuments"])
const calendarAppointments = computed(() => store.getters["appointments/getAllAppointmentsForCalendar"])
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)

const redirect = async (documentSlug) => {
    store.dispatch("documents/fetchDocument", {
        slug: slug.value,
        document_slug: documentSlug
    }).then(() => router.push(`/home/document/${documentSlug}/`))

}
const closeAppointmentForm = () => {
    toast.add({ severity: 'success', summary: 'Успех', detail: 'Запись добавлена', life: 3000 });
    visible.value = false
}
onBeforeMount(async () => {
    store.dispatch("user/fetchUserPersonalInfo", slug.value)
    store.dispatch("appointments/fetchAppointments", slug.value)
    store.dispatch("documents/fetchNewestDocument", slug.value)
})
</script>
<template>
    <Toast />
    <HeaderLayout>
        <TabMenu />
    </HeaderLayout>
    <main class="p-2 flex gap-2 flex-col">
        <section class="flex-media__section gap-8">
            <section class="bg__section bordered__section p-4 rounded-2xl flex flex-col w-full">
                <div>
                    <div class="p-4">
                        <p class="text-2xl font-bold text-center">
                            {{ personalInfo.first_name }} {{ personalInfo.second_name }}
                        </p>
                        <p class="text-slate-400 font-thin text-center">{{ personalInfo.email }}</p>
                    </div>
                    <div class="flex flex-col w-full p-4">
                        <div class="grid grid-cols-2 grid-rows-2 gap-9">
                            <div class="flex flex-col">
                                <p class="pb-4 text-slate-400 font-normal">Пол</p>
                                <p class="pb-2 border-b-slate-200 border-b-2 font-thin">{{ personalInfo.gender }}</p>
                            </div>
                            <div class="flex flex-col">
                                <p class="pb-4 text-slate-400 font-normal">Возраст</p>
                                <p class="pb-2 border-b-slate-200 border-b-2 font-thin">{{ personalInfo.age }}</p>
                            </div>
                            <div class="flex flex-col">
                                <p class="pb-4 text-slate-400 font-normal">Город</p>
                                <p class="pb-2 border-b-slate-200 border-b-2 font-thin h-full">{{ personalInfo.city }}
                                </p>
                            </div>
                            <div class="flex flex-col">
                                <p class="pb-4 text-slate-400 font-normal">Адресс</p>
                                <p class="pb-2 border-b-slate-200 border-b-2 font-thin">{{ personalInfo.address }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-span-2">
                    <p class="pb-4 text-slate-400 font-normal ">Здоровье</p>
                    <p class="font-thin">{{ personalInfo.health_status }}</p>
                </div>
            </section>
            <section
                class="bordered__section flex-width__section document__section max-w-1/2 w-full p-4 flex flex-col gap-1">
                <p class="text-2xl font-semibold text-left">Недавно добавленные документы</p>
                <Tag value="New"></Tag>
                <div v-for="(document, index) in newestDocuments" :key="index"
                    class="document_wrapper bordered__section bg-white p-3" @click="redirect(document.slug)">
                    <div>
                        <div class="flex justify-between">
                            <p class="text-gray-600">{{ document.document_type.name }}</p>
                            <Tag severity="info" class="inline-block"
                                :value="'Добавлен ' + document.parsed_date.day + ' ' + document.parsed_date.mounth + ' ' + document.parsed_date.year">
                            </Tag>
                        </div>
                        <p>{{ document.name }}</p>
                    </div>
                </div>
            </section>
        </section>
        <main class="flex-media__section gap-8 justify-between mb-4">
            <section class="bordered__section w-full">
                <header class="p-4">
                    <div class="flex justify-between items-center max-[900px]:flex-col max-[900px]:gap-4">
                        <SelectButton v-model="select" :options="options" option-label="name" option-value="value"
                            class="flex" />
                        <button class="add-appointment-button" @click="visible = true">Добавить запись</button>
                    </div>
                </header>
                <section class="bordered__section bg__section">
                    <div v-if="select != 'calendar' && select != 'physical'" class="flex flex-col m-4 p-4 gap-3">
                        <div v-if="!getAppointments.length">
                            <p class="text-2xl font-bold text-center">Записей пока нет</p>
                        </div>
                        <div v-else v-for="(appointment, index) in getAppointments" :key="index">
                            <div class="flex-media__section bg-white rounded-xl p-4 flex w-full gap-2">
                                <div
                                    class="border-media_section flex-width__section flex flex-col px-4 justify-center w-1/4">
                                    <div class="flex gap-2 max-[900px]:justify-center">
                                        <p class="text-2xl font-bold">{{ appointment.parsed_date.day }}</p>
                                        <p class="text-2xl font-bold">{{ appointment.parsed_date.mounth }}</p>
                                        <p class="text-2xl font-bold">{{ appointment.parsed_date.year }}</p>
                                    </div>
                                    <div class="max-[900px]:text-center">
                                        <p class="text-lg text-slate-400">{{ appointment.parsed_date.hours }}:{{
                                            appointment.parsed_date.minutes
                                        }}</p>
                                    </div>
                                </div>
                                <div
                                    class="flex-width__section border-media_section flex flex-col gap-2 px-4 text-center w-1/4">
                                    <p class="font-extralight text-slate-400">Доктор</p>
                                    <p class="text-2xl font-bold self-center">{{ appointment.doctor.full_name }}</p>
                                </div>
                                <div
                                    class="flex-width__section border-media_section flex flex-col gap-2 px-4 text-center w-1/3">
                                    <p class="font-extralight text-slate-400"> Специадизация доктора</p>
                                    <p class="text-2xl font-bold self-center whitespace-normal break-all">{{
                                        appointment.doctor_specialization.name }}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else-if="select == 'physical'" class="p-4">
                        <PhysicalParametersSection />
                    </div>
                    <div v-else>
                        <v-calendar show-weeknumbers="right" :attributes="calendarAppointments" expanded />
                    </div>
                </section>
            </section>
        </main>
        <Dialog v-model:visible="visible" header="Создать запись" :style="{ width: '50vw' }">
            <AppointmentForm @on-add-appointment="closeAppointmentForm" />
        </Dialog>
    </main>
</template>
<style lang="css" scoped>
.bg__section {
    background-color: rgba(110, 131, 165, 0.103);
}

.border-media_section {
    border-right: 3px solid;
    border-color: rgb(226 232 240);
}

.flex-media__section {
    display: flex;
}

.flex-width__section {
    width: 30%;
}

@media screen and (max-width: 900px) {
    .flex-width__section {
        width: 100%;
    }

    .flex-media__section {
        flex-direction: column;
    }

    .border-media_section {
        border-right: 0;
        border-bottom: 3px solid;
        border-color: rgb(226 232 240);
        padding-bottom: 1px;
    }
}

.bordered__section {
    border: 1px solid rgb(218, 218, 218);
    border-radius: 5px;
}

.document__section {
    background-color: rgba(138, 183, 255, 0.103);
}

.document_wrapper {
    box-shadow: 5px 5px 5px -5px rgba(34, 60, 80, 0.6);
}

.add-appointment-button {
    background-color: #0095ff;
    border: 1px solid transparent;
    border-radius: 3px;
    box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", "Liberation Sans", sans-serif;
    font-size: 15px;
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
    height: 100%;
}

.add-appointment-button:hover,
.add-appointment-button:focus {
    background-color: #07c;
}

.add-appointment-button:focus {
    box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);
}

.add-appointment-button:active {
    background-color: #0064bd;
    box-shadow: none;
}
</style>