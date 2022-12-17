<script setup>
import documentPageLink from '@/components/links/documentPageLink.vue';
import { reactive } from 'vue'
const documentLink = reactive({
    link: "/",
    text: "Documents"
})
const appoitmentsLink = reactive({
    link: "/",
    text: "Appoitments"
})
const doctorLink = reactive({
    link: "/",
    text: "Doctors",
})
</script>
<template>
    <nav class="flex flex-row justify-evenly mt-3">
        <documentPageLink :href="documentLink.link" :text=documentLink.text />
        <documentPageLink :href="appoitmentsLink.link" :text="appoitmentsLink.text" />
        <documentPageLink :href="doctorLink.link" :text="doctorLink.text" />
    </nav>
</template>