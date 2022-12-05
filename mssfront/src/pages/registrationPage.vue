<script setup>
import registrationForm from '@/components/forms/registrationForm.vue';
</script>
<template>
    <main class="main">
        <section class="section">
            <registrationForm />
        </section>
    </main>
</template>
<style scoped>
.main {
    display: flex;
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