<script setup>
import doctorPageCard from '@/components/cards/doctorPageCard.vue';
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const searchString = ref("")
const selectedDoctorType = ref(null)
const doctors = computed(() => filter())
const filter = () => {
    let doctorsBySearchString = store.getters["doctors/getDoctorsByString"](searchString.value)
    console.log("doctorsBySearchString", doctorsBySearchString)
    if (selectedDoctorType.value) {
        let doctorsBydoctorType = store.getters["doctors/getDoctorByDoctorTypes"](selectedDoctorType.value)
        console.log("doctorsBydoctorType", doctorsBydoctorType)
        let result = doctorsBySearchString.filter(d => doctorsBydoctorType.some(doctor => doctor.doctor_slug == d.doctor_slug))
        console.log("intercaption", result)
        return result
    }
    return doctorsBySearchString
}
const doctorTypes = computed(() => store.state.doctors.doctorTypes)
</script>
<template>
    <main class="main">
        <section class="w-4/5 flex flex-row gap-7">
            <div class="search-bar-container">
                <input class="search-bar" placeholder="search by fio" v-model="searchString">
            </div>
            <div class="flex justify-center">
                <div class="w-96 h-full">
                    <select class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal 
                    text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded
                    transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 
                    focus:outline-none h-full" v-model="selectedDoctorType">
                        <option disabled value="" selected>Please select doctor type</option>
                        <option v-for="doctorType in doctorTypes" :key="doctorType.slug" :value="doctorType">{{
                            doctorType.name
                        }}
                        </option>
                    </select>
                </div>
            </div>
        </section>

        <section class="doctor-list-section" v-if="doctors">
            <doctorPageCard v-for="doctor in doctors" :key="doctor.doctor_slug" :personalInfo="doctor.personal_info"
                :doctorTypes="doctor.doctor_types" :summary="doctor.doctor_summary.short_summary" />
        </section>
    </main>
</template>
<style scoped>
.main {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    width: 100%;
}

.search-bar-container {
    display: flex;
    justify-content: center;
    width: 80%;
}

.search-bar {
    border-radius: 10px;
    padding: 10px;
    border: 2px solid rgb(185, 185, 188);
    width: 100%;
    font-size: 1rem;
}

.search-bar:focus {
    background-color: white;
    border: 2px solid rgb(37, 99, 235);
    outline-width: 0;
}

.doctor-list-section {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-flow: row dense;
    gap: 10px;
    justify-items: center;
    width: 90%;
}

@media screen and (max-width: 1000px) {
    .doctor-list-section {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-auto-flow: row dense;
        gap: 10px;
        justify-items: center;
        width: 80%;
    }

}

@media screen and (max-width: 650px) {
    .doctor-list-section {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        grid-auto-flow: row dense;
        gap: 10px;
        justify-items: center;
        width: 80%;
    }

}
</style>