<script setup>
import { useStore } from 'vuex';
import { onBeforeMount, computed, ref } from 'vue';
import { useRouter } from 'vue-router'

import DataView from 'primevue/dataview'
import Button from 'primevue/button'
import Dropdown from 'primevue/dropdown'

import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import BodyLayout from '@/components/layout/BodyLayout.vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
import AppointmentForm from '@/components/ui/Forms/AppointmentForm.vue'


const store = useStore()
const router = useRouter()
const sortKey = ref("")
const show = ref(false)
const layout = ref("list")
const doctors = computed(() => sortKey.value.length == 0 ? store.state.doctors.doctors : store.getters["doctors/getDoctorByDoctorTypeSlug"](sortKey.value))
const doctorTypes = computed(() => store.getters["doctors/getDoctorTypes"])
const redirect = (slug) => router.push(`/home/doctor/${slug}`)
const onclick = () => {
    show.value = !show.value
}
onBeforeMount(() => {
    store.dispatch("doctors/fetchAllDoctors")
    store.dispatch("doctors/fetchAllDoctorTypes")
})

</script>
<template>
    <HeaderLayout>
        <TabMenu />
    </HeaderLayout>
    <BodyLayout :class="'flex flex-row'">
        <div class="flex flex-col gap-4 w-full">
            <DataView :value="doctors" :paginator="true" :rows="10" :layout="layout" data-key="doctor_slug">
                <template #header>
                    <div class="flex justify-between">
                        <div class="flex">
                            <Dropdown v-model="sortKey" :options="doctorTypes" option-label="name" option-value="slug"
                                placeholder="Search by doctor type" class="mr-4"></Dropdown>
                            <Button label="Clear" class="p-button-danger" @click="sortKey = ''"></Button>
                        </div>
                    </div>
                </template>
                <template #list="slotProps">
                    <div class="doctor-list">
                        <div class="doctor-list-item">
                            <div class="image-container">
                                <div class="doctor-name">{{ slotProps.data.full_name }}</div>
                            </div>
                            <div class="doctor-detail">
                                <div class="doctor-types" v-for="doctor_type in slotProps.data.doctor_types"
                                    :key="doctor_type.slug">{{ doctor_type.name }}</div>
                            </div>
                            <div class="doctor-list-action">
                                <Button label="Create appoitments" class="p-button-info w-full" @click="onclick"></Button>
                                <Transition>
                                    <AppointmentForm v-if="show" :doctor_slug="slotProps.data.doctor_slug"
                                        :doctor_full_name="slotProps.data.personal_info.full_name"
                                        :doctor-types="slotProps.data.doctor_types" />
                                </Transition>
                                <Button label="Open doctor Info" class="p-button-info w-full"
                                    @click="redirect(slotProps.data.doctor_slug)"></Button>
                            </div>
                        </div>
                    </div>
                </template>
            </DataView>
        </div>
    </BodyLayout>
</template>
<style scoped>
.doctor-list-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 1rem;
    width: 100%;
    cursor: pointer;
}

.doctor-image {
    width: 150px;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}

.doctor-detail {
    flex: 1 1 0;
    text-align: center;
}

.doctor-name {
    font-size: 1.5rem;
    font-weight: 700;
}

.doctor-summary {
    padding: 1rem;
}

.image-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.doctor-list-action {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

@media screen and (max-width:600px) {
    .doctor-list-item {
        display: flex;
        flex-wrap: wrap;
    }

    .doctor-list-action {
        padding-top: 1rem;
        width: 100%;
    }

    .doctor-image {
        margin-left: auto;
        margin-right: auto;
    }

    .doctor-detail {
        text-align: center;
    }
}

@media screen and (max-width:400px) {
    .doctor-list-item {
        display: flex;
        flex-direction: column;
    }

}
</style>