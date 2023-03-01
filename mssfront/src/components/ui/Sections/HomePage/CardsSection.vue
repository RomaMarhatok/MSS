<script setup>
import { ref } from "vue";
import homePageCard from "@/components/layout/Cards/HomePageCard.vue"
const title = ref("SOME TEXT")
const text = ref("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
</script>
<template>
    <div class="card-container pt-5 pl-5 pr-5 flex flex-row justify-evenly">
        <homePageCard :text="text" :title="title" />
        <homePageCard :text="text" :title="title" />
        <homePageCard :text="text" :title="title" />
    </div>
</template>
<style scoped>
@media screen and (max-width: 600px) {
    .card-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-auto-flow: row dense;
        justify-items: center;
        row-gap: 1rem;
    }

}

@media screen and (max-width: 550px) {
    .card-container {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        grid-auto-flow: row dense;
        justify-items: center;
    }

}
</style>