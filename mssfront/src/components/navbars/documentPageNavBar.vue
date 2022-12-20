<script setup>
import documentPageLink from '@/components/links/documentPageLink.vue';
import { reactive } from 'vue'
const documentLink = reactive({
    link: "#/",
    text: "Documents",
    active: true,
})
const appoitmentsLink = reactive({
    link: "#/",
    text: "Appoitments",
    active: false,

})
const doctorLink = reactive({
    link: "#/",
    text: "Doctors",
    active: false,

})
</script>
<template>
    <nav class="flex flex-row justify-evenly mt-3">
        <documentPageLink :href="documentLink.link" :text=documentLink.text :active="documentLink.active" />
        <documentPageLink :href="appoitmentsLink.link" :text="appoitmentsLink.text" :active="appoitmentsLink.active" />
        <documentPageLink :href="doctorLink.link" :text="doctorLink.text" :active="doctorLink.active" />
    </nav>
</template>