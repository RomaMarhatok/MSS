<script setup>
import Image from 'primevue/image'
import DataView from 'primevue/dataview'
import Dropdown from 'primevue/dropdown';
import Button from 'primevue/button'
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import { computed, ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'
const sortKey = ref("")
const router = useRouter()
const store = useStore()
const layout = ref("list")
const doctors = computed(() => sortKey.value.length == 0 ? store.state.doctors.doctors : store.getters["doctors/getDoctorByDoctorTypeSlug"](sortKey.value))
const doctorTypes = computed(() => store.state.doctors.doctorTypes)
const redirect = (slug) => router.push(`/doctor/${slug}`)
</script>
<template>
    <main class="main">
        <DataView :value="doctors" :paginator="true" :rows="10" :layout="layout">
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
                <div class="doctor-list" @click="redirect(slotProps.data.doctor_slug)">
                    <div class="doctor-list-item">
                        <div class="image-container">
                            <Image class="doctor-image" src="https://placehold.co/150x100/" />
                            <div class="doctor-name">{{ slotProps.data.personal_info.full_name }}</div>
                        </div>
                        <div class="doctor-detail">
                            <div class="doctor-types" v-for="doctor_type in slotProps.data.doctor_types"
                                :key="doctor_type.slug">{{ doctor_type.name }}</div>
                        </div>
                        <div class="doctor-list-action">
                            <Button label="Create appoitments" class="p-button-info w-full"></Button>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
    </main>
</template>
<style scoped>
.doctor-list-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 1rem;
    width: 100%;
}

.doctor-image {
    width: 150px;
    height: 100px;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
    margin-right: 2rem;
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
    justify-content: center;
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