<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    document: Object
})
</script>
<template>
    <button class="p-3 cursor-pointer bg-none border-none bg-white rounded-2xl hover:bg-sky-300">
        <div class="text-6xl">
            <font-awesome-icon icon="fa-solid fa-flask" />
            <font-awesome-icon icon="fa-solid fa-vials" />
        </div>
        <div>
            <p>
                {{ props.document.content }}
            </p>
        </div>
    </button>
</template>