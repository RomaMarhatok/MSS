<script setup>

import { defineProps } from 'vue';

const props = defineProps({
    errors: Object,
    message: String,
})
</script>
<template>
    <div class="section">
        <p v-if="props.message" class="section__message">{{ props.message }}</p>
        <ul v-if="errors" class="section__ul">
            <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
        <form @submit.prevent="$emit('SubmitForm')" class="form" method="post">
            <slot>Fallback content</slot>
        </form>
    </div>
</template>
<style scoped>
.form {
    display: flex;
    flex-direction: column;
}

.form__header {
    display: flex;
    flex-direction: row;
    gap: 10px;
}

.section__ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.section__ul>li {
    border-radius: 10px;
    padding: 5px;
    color: rgb(114, 75, 75);
    background-color: pink;
    margin-bottom: 5px;
}

.section__message {
    text-align: center;
    border-radius: 10px;
    padding: 5px;
    color: rgb(78, 139, 63);
    background-color: rgb(220, 255, 192);
}
</style>