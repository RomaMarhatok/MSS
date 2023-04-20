<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import HeaderLayout from '@/components/layout/HeaderLayout.vue'
import BodyLayout from '@/components/layout/BodyLayout.vue'
const route = useRoute()
const store = useStore()
const doctorSlug = route.params.doctorSlug
const doctor = computed(() => store.getters["doctors/getDoctorBySlug"](doctorSlug))
</script>
<template>
    <HeaderLayout />
    <BodyLayout>
        <section class="main-data-section">
            <section class="personal-image">
                <Image class="img" :src="doctor.personal_info.image" />
                <div class="content">
                    <p>{{ fullName }}</p>
                </div>
            </section>
            <transition name="slide-fade">
                <div class="m-4" v-if="show">
                    <AppointmentForm></AppointmentForm>
                </div>
            </transition>
            <div class="resume-section">
                <header class="header__section">
                    Resume
                </header>
                <div class="table-wrapper">
                    <p class="label-text">
                        {{ doctor.doctor_summary.summary }}
                    </p>
                </div>
            </div>
        </section>

    </BodyLayout>
</template>
<style scoped>
.resume-section {
    display: flex;
    flex-direction: column;
    width: 70%;
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
    padding: 1rem;
}

.header__section {
    text-align: center;
}

.table-wrapper {
    display: flex;
    justify-content: center;
}

.label-text {
    width: 80%;
}

.main-data-section {
    display: flex;
    flex-direction: row;
    margin-top: 10px;
    justify-content: space-evenly;
}

@media screen and (max-width: 1100px) {
    .main-data-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin-top: 10px;
    }
}
</style>