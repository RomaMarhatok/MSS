<script setup>
import { useRoute, useRouter } from 'vue-router';
import UserService from '@/../services/UserService'
const route = useRoute()
const router = useRouter()
const token = route.params.token
const uid = route.params.uid
const userService = new UserService()
userService.verifyUser(uid, token).then(() => router.push({
    name: "authentication-page"
}))

</script>
<template>
    <p>Verify</p>
</template>