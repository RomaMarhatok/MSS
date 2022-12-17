<script setup>

import { defineProps } from 'vue';
import errorMessage from '@/components/messages/errorMessage.vue';
import successMessage from '@/components/messages/succesMessage.vue';
const props = defineProps({
    errors: {
        type: Array,
        default: () => []
    },
    message: String,
})
</script>
<template>
    <div class="section">
        <successMessage v-if="props.message" :errorText="props.message" />
        <div v-if="props.errors.length" class="flex flex-col">
            <errorMessage severity="error" v-for="(error, index) in props.errors" :key="index" :errorText="error" />
        </div>
        <form @submit.prevent="$emit('SubmitForm')" class="flex flex-col" method="post">
            <slot>Fallback content</slot>
        </form>
    </div>
</template>