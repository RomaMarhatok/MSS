<script setup>
import { defineProps } from "vue"
import Card from 'primevue/card'
const props = defineProps({
    title: String,
    text: String,
})
</script>
<template>
    <Card class="w-60 shadow-2xl border rounded-2xl">
        <template #header>
            <img src="https://mdbootstrap.com/img/new/standard/city/044.jpg" class="max-w-full h-auto rounded-t-2xl" alt="">
        </template>
        <template #title>
            <p class="bg-custom-dark-blue text-custom-dark-aqua bg-c text-base font-bold text-center pt-3">
                {{ props.title }}
            </p>
        </template>
        <template #content>
            <p class="bg-custom-dark-blue text-custom-dark-aqua bg-c text-center rounded-b-2xl p-3">
                {{ props.text }}
            </p>
        </template>
    </Card>
</template>