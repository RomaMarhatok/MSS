<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    errorText: String
})
</script>
<template>
    <main class="bg-error-message-bg p-1 rounded-3xl">
        <div class="pl-4">
            <p class="text-red-600">{{ props.errorText }}</p>
        </div>
    </main>
</template>
