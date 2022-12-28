<script setup>
import { computed } from 'vue';
import { useStore } from 'vuex';
import errorMessage from '@/components/messages/errorMessage.vue';
import successMessage from '@/components/messages/succesMessage.vue';
const store = useStore()
const errors = computed(() => store.getters["responseErrors/generalErrors"])
const message = computed(() => store.state.registration.message)
</script>
<template>
    <div class="section">
        <successMessage v-if="message" :messageText="message" />
        <div v-if="errors.length" class="flex flex-col">
            <errorMessage severity="error" v-for="(error, index) in errors" :key="index" :errorText="error" />
        </div>
        <form @submit.prevent="$emit('SubmitForm')" class="flex flex-col" method="post">
            <slot>Fallback content</slot>
        </form>
    </div>
</template>