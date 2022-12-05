<script setup>
import { defineProps } from "vue"
const props = defineProps({
    title: String,
    text: String,
})
</script>
<template>
    <div class="container__card">
        <div class="card__head">
            <img class="card__image" src="@/assets/placeHolderIcon.svg">
        </div>
        <div class="card__body">
            <p class="body__title">{{ props.title }}</p>
            <p class="body__text">{{ props.text }}</p>
        </div>
    </div>
</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans&display=swap');

.container__card {
    margin-left: 2%;
    box-shadow: 15px 10px 30px rgba(0, 0, 0, 0.25);
    border-radius: 25px;
    background: linear-gradient(0deg, rgba(19, 48, 94, 1) 60%, white 50%);
}

.card__head .card__image {
    margin-left: auto;
    margin-right: auto;
    display: block;
    width: 45%;
}

.card__head {
    padding-top: 5%;
}

.card__body {
    color: rgba(171, 134, 69, 1);
    text-align: center;
    font-family: 'Fira Sans';
    font-size: 1.2em;
}
</style>