<script setup>
import HeaderLayout from '@/components/layout/HeaderLayout.vue'
import DoctorTabMenu from '@/components/ui/Menu/DoctorTabMenu.vue';
import Column from 'primevue/column'
import DataTable from 'primevue/datatable'
// import Toolbar from 'primevue/toolbar';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { onBeforeMount, computed } from 'vue';
const store = useStore()
const router = useRouter()
const appointments = computed(() => store.getters["doctorAppointments/getAppointments"])
const onclick = (appointment) => {
    console.log(appointment.data)
    store.commit("appointment/setSelectedAppointment", appointment.data)
    router.push("/doctor/appointment/")
}

onBeforeMount(() => {
    store.dispatch("doctorAppointments/fetchAppointments", store.state.user.slug)
    store.dispatch("patients/fetchPatients")
})

</script>
<template>
    <HeaderLayout>
        <DoctorTabMenu />
    </HeaderLayout>
    <main class="flex">
        <section v-if="!appointments.length" class="w-full flex justify-center">
            <p class="text-3xl text-slate-400">Записей к вам пока нет.</p>
        </section>
        <section v-else class="w-full">
            <div>
                <DataTable :value="appointments" @row-click="onclick">
                    <Column header="Пациент">
                        <template #body="slotProps">
                            <p>{{ slotProps.data.patient.full_name }}</p>
                        </template>
                    </Column>
                    <Column header="Дата">
                        <template #body="slotProps">
                            <div class="flex flex-col justify-center">
                                <div class="flex max-[900px]:justify-center gap-1">
                                    <p class="font-bold">{{ slotProps.data.parsed_date.day }}</p>
                                    <p class="font-bold">{{ slotProps.data.parsed_date.mounth }}</p>
                                    <p class="font-bold">{{ slotProps.data.parsed_date.year }}</p>
                                    <p class="">{{ slotProps.data.parsed_date.hours }}:{{
                                        slotProps.data.parsed_date.minutes
                                    }}</p>
                                </div>
                            </div>
                        </template>
                    </Column>
                    <Column header="Тип доктора">
                        <template #body="slotProps">
                            <div>{{ slotProps.data.doctor_specialization.name }}</div>
                        </template>
                    </Column>
                    <!-- <Column header="Options">
                            <template #body>
                                <Toolbar>
                                    <template #end>
                                        <button class="delete-button"><i class="pi pi-times"></i></button>
                                    </template>
                                </Toolbar>
                            </template>
                        </Column> -->
                </DataTable>
            </div>
        </section>
    </main>
</template>
<style lang="css" scoped>
.delete-button {
    background: #e62143;
    border-radius: 11px;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: flex;
    font-family: Mija, -apple-system, BlinkMacSystemFont, Roboto, "Roboto Slab", "Droid Serif", "Segoe UI", system-ui, Arial, sans-serif;
    font-size: 1.15em;
    font-weight: 700;
    justify-content: center;
    line-height: 33.4929px;
    padding: .8em 1em;
    text-align: center;
    text-decoration: none;
    text-decoration-skip-ink: auto;
    text-shadow: rgba(0, 0, 0, .3) 1px 1px 1px;
    text-underline-offset: 1px;
    transition: all .2s ease-in-out;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    width: 100%;
    word-break: break-word;
    border: 0;
}

.delete-button:hover {
    background-color: rgb(255, 0, 0);
}
</style>