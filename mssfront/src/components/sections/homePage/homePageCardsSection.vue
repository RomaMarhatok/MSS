<script setup>
import { ref } from "vue";
import homePageCard from "@/components/cards/homePageCard.vue"
const title = ref("SOME TEXT")
const text = ref("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
</script>
<template>
    <div class="cards__container">
        <homePageCard :text="text" :title="title" />
        <homePageCard :text="text" :title="title" />
        <homePageCard :text="text" :title="title" />
    </div>
</template>
<style scoped>
.cards__container {
    padding-left: 5%;
    padding-right: 5%;
    display: flex;
    flex-direction: row;
    padding-top: 2%;
    justify-content: space-between;
}
</style>