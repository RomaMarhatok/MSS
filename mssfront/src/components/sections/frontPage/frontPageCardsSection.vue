<script setup>
import { ref } from "vue";
import frontPageCard from "../../cards/frontPageCard.vue"
const title = ref("SOME TEXT")
const text = ref("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
</script>
<template>
    <div class="cards__container">
        <front-page-card :text="text" :title="title" />
        <front-page-card :text="text" :title="title" />
        <front-page-card :text="text" :title="title" />
    </div>
</template>
<style>
.cards__container {
    padding-left: 5%;
    padding-right: 5%;
    display: flex;
    flex-direction: row;
    padding-top: 2%;
    justify-content: space-between;
}
</style>