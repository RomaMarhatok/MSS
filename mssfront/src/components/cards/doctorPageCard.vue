<script setup>
import { defineProps, computed, getCurrentInstance } from "vue"
import { useRouter } from "vue-router";
import getBaseApi from "@/apis/baseApi";
const instance = getCurrentInstance()
const router = useRouter()
const props = defineProps({
    personalInfo: Object,
    doctorTypes: {
        type: Array,
        default: () => []
    }
})
const getImageSrc = computed(() => {
    return getBaseApi.getUri() + props.personalInfo.image
})
function redirectOnSingleDoctorPage() {
    const slug = instance.vnode.key
    router.push(`/doctor/${slug}/`)
}
</script>
<template>
    <div class="card" @click="redirectOnSingleDoctorPage">
        <div class="img-container">
            <img class="card-img" :src="getImageSrc">
            <div class="container">
                <p class="small-text" v-for="doctorType in props.doctorTypes" :key="doctorType.slug">
                    {{ doctorType.name }}
                </p>
            </div>
        </div>
        <div class="card-text">
            <p class="text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum, ipsa distinctio harum sit
                repellendus incidunt dolorem laudantium corporis assumenda totam quos reiciendis enim odio neque
                possimus, atque fugit, ratione nulla.</p>

            <!-- <p class="text">{{ props.personalInfo.short_resume }}</p> -->
        </div>
    </div>
</template>
<style scoped>
.card {
    display: flex;
    flex-direction: row;
    border: 1px solid black;
}

.img-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    padding: 0.5rem;
}

.card-img {
    border-radius: 10px;
    width: 100%;
    height: auto;
}

.card-text {
    padding: 0.5rem;
    width: 100%;
}

.small-text {
    font-size: 0.8rem;
}

.text {
    font-size: 0.8rem;
}

.card:hover {
    transition: 200ms;
    color: white;
    background-color: rgba(19, 48, 94, 1);
    border-radius: 20px;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 10px;
}

@media screen and (max-width: 450px) {
    .card {
        display: flex;
        flex-direction: column;
    }

    .card-text {
        text-align: center;
    }
}
</style>