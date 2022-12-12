<script setup>

import { defineProps } from 'vue';
import Message from 'primevue/message';
const props = defineProps({
    errors: Object,
    message: String,
})
</script>
<template>
    <div class="section">
        <Message v-if="props.message" severity="success">{{ props.message }}</Message>
        <div v-if="errors" class="flex flex-col">
            <Message severity="error" v-for="(error, index) in props.errors" :key="index">
                {{ error }}
            </Message>
        </div>
        <form @submit.prevent="$emit('SubmitForm')" class="flex flex-col" method="post">
            <slot>Fallback content</slot>
        </form>
    </div>
</template>