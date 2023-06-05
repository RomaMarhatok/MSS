<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    email: String,
})
</script>
<template>
    <div>
        <p class="text-center">
            На почту {{ props.email }} было отправлено сообщение для подтверждения аккаунта
        </p>
    </div>
</template>