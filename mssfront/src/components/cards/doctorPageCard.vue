<script setup>
import { defineProps, computed } from "vue"
import getBaseApi from "@/apis/baseApi";
const props = defineProps({
    personalInfo: Object,
    doctorTypes: Array,
})
const getImageSrc = computed(() => {
    return getBaseApi.getUri() + props.personalInfo.image
})
</script>
<template>
    <div class="card">
        <div class="img-container">
            <img class="card-img" :src="getImageSrc">
        </div>
        <div class="card-text">
            <p class="text">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Et asperiores assumenda ipsum
                suscipit animi, laborum, iure modi culpa fugiat sit minus voluptates quas fuga perferendis rem tempore
                doloribus sint cum!</p>
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
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 0.5rem;
}

.card-img {
    border-radius: 10px;
    width: 100%;
    height: auto;
}

.card-text {
    padding: 1rem;
    width: 100%;
}

.text {
    font-size: 0.9rem;
}

.card:hover {
    transition: 200ms;
    color: white;
    background-color: rgba(19, 48, 94, 1);
    border-radius: 20px;
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