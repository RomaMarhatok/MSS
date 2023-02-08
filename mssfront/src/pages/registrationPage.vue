<script setup>
import registrationPageHeader from "@/components/layout/Headers/RegistrationPageHeader.vue"
import registrationForm from '@/components/ui/Forms/RegistrationForm.vue';
import registrationPageLink from '@/components/common/Links/ChangePasswordLink.vue';
import { ref } from 'vue';
const changePasswordLink = ref("#/")
</script>
<template>
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <div class="flex flex-col w-4/5">
            <registrationPageHeader />
            <registrationForm />
            <registrationPageLink :link="changePasswordLink" />
        </div>
    </main>
</template>