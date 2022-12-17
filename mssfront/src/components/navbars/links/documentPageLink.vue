<script setup>
import { defineProps } from "vue";
const props = defineProps({
    href: String,
    text: String,
})
</script>
<template>
    <div
        class="flex border-3 w-fit py-2 px-4 rounded-xl text-black hover:bg-header-dark-blue hover:text-white hover:dura">
        <a class="flex justify-center items-center font-normal text-inherit text-lg cursor-pointer " :href=props.href>
            {{ props.text }}
        </a>
    </div>
</template>