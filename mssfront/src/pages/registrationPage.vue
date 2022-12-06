<script setup>
import registrationForm from '@/components/forms/registrationForm.vue';
import registrationPageLink from '@/components/links/registrationPageLink.vue';
import { ref } from 'vue';
const changePasswordLink = ref("#/")
</script>
<template>
    <main class="main">
        <section class="section">
            <registrationForm />
        </section>
        <registrationPageLink :link="changePasswordLink" />
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
}

.section {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
</style>