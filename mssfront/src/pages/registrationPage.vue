<script setup>
import registrationPageHeader from "@/components/headers/registrationPageHeader.vue"
import registrationForm from '@/components/forms/registrationForm.vue';
import registrationPageLink from '@/components/links/registrationPageLink.vue';
import { ref } from 'vue';
const changePasswordLink = ref("#/")
</script>
<template>
    <main class="main">
        <div class="wrapper">
            <registrationPageHeader />
            <registrationForm />
            <registrationPageLink :link="changePasswordLink" />
        </div>

    </main>
</template>
<style scoped>
.main {
    display: flex;
    flex-direction: column;
    font-family: 'Fira Sans';
    justify-content: center;
    align-items: center;
    min-height: 85vh;
    width: 100%;
}

.wrapper {
    display: flex;
    flex-direction: column;
    width: 80%;
}
</style>