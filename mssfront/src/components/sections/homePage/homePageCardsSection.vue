<script setup>
import { ref } from "vue";
import homePageCard from "@/components/cards/homePageCard.vue"
const title = ref("SOME TEXT")
const text = ref("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
</script>
<template>
    <div class="pt-5 pl-5 pr-5 flex flex-row justify-evenly">
        <homePageCard :text="text" :title="title" />
        <homePageCard :text="text" :title="title" />
        <homePageCard :text="text" :title="title" />
    </div>
</template>