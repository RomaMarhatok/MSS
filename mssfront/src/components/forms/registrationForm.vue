<script setup>
import registrationPageHeader from "@/components/headers/registrationPageHeader.vue"
import registrationFormEmailInput from '../inputs/registrationForm/registrationFormEmailInput.vue';
import registrationFormPasswordInput from '../inputs/registrationForm/registrationFormPasswordInput.vue';
import registrationFormSubmitButton from '../buttons/registrationFormSubmitButton.vue';
import { ref } from 'vue';
const password = ref("")
const login = ref("")
</script>
<template>
    <form class="form" method="post">
        <registrationPageHeader />
        <registrationFormEmailInput v-model="login" />
        <registrationFormPasswordInput v-model="password" />
        <registrationFormSubmitButton />
        <p class="a">{{ password }}</p>
        <p class="a">{{ login }}</p>

    </form>
</template>
<style scoped>
.form {
    display: flex;
    flex-direction: column;
}
</style>