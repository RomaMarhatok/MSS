<script setup>
import registrationPageHeader from "@/components/layout/Headers/RegistrationPageHeader.vue"
import authenticationForm from "@/components/ui/Forms/AuthenticationForm.vue";
import registrationPageLink from '@/components/common/Links/ChangePasswordLink.vue';
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