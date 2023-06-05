<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    messageText: String
})
</script>
<template>
    <main class="bg-success-message-bg p-1 rounded-3xl">
        <div class="pl-4">
            <p class="text-success-message-color">{{ props.messageText }}</p>
        </div>
    </main>
</template>
