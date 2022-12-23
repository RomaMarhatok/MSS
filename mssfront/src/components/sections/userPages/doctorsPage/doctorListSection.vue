<script setup>
import doctorPageCard from '@/components/cards/doctorPageCard.vue';
import { onMounted, ref } from 'vue';
import DoctorService from '@/../services/DoctorService';
const doctors = ref([])
onMounted(() => {
    const doctorService = ref(new DoctorService());
    doctorService.value.getAllDoctors().then(response => {
        doctors.value = response.data.doctors
    }).catch(error => console.log(error))
})
</script>
<template>
    <main class="main">
        <div class="search-bar-container">
            <input class="search-bar" placeholder="search">
        </div>
        <section class="doctor-list-section" v-if="doctors">
            <doctorPageCard v-for="doctor in doctors" :key="doctor.doctor_slug" :personalInfo="doctor.personal_info"
                :doctorTypes="doctor.doctor_types" />
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
    width: 60%;
}

.search-bar {
    border-radius: 10px;
    padding: 10px;
    border: 2px solid rgb(185, 185, 188);
    width: 100%;
    font-size: 1rem;
}

.doctor-list-section {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-auto-flow: row dense;
    gap: 10px;
    justify-items: center;
    width: 80%;
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