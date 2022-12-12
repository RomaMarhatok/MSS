<script setup>
import registrationPageHeader from "@/components/headers/registrationPageHeader.vue"
import authenticationForm from "@/components/forms/authenticationForm.vue";
import registrationPageLink from '@/components/links/registrationPageLink.vue';
import { ref } from 'vue';
const changePasswordLink = ref("#/")
</script>
<template>
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <div class="flex flex-col w-4/5">
            <registrationPageHeader />
            <authenticationForm />
            <registrationPageLink :link="changePasswordLink" />
        </div>

    </main>
</template>