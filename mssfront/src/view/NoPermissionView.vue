<script setup>
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import ROLES from '@/../roles/roles'
const store = useStore()
const router = useRouter()
const redirect = async () => {
    const token = localStorage.getItem("auth_token")
    if (token === null) {
        router.push({ name: 'site-home-page' })
    }
    else {
        const userRole = store.state.user.role
        if (userRole === ROLES.Doctor) {
            router.push({ name: 'doctor-home-page' })
        }
        else if (userRole === ROLES.Patient) {
            router.push({ name: 'profile-page' })
        }
        else {
            router.push({ name: 'site-home-page' })
        }
    }
}
</script>
<template>
    <main class="flex w-full h-screen gap-4 justify-center items-center">
        <p class="text-5xl text-slate-400">К данной странице нет доступа.</p>
        <a class="link text-5xl text-slate-400" @click="redirect">На главную ?</a>
    </main>
</template>
<style lang="css">
.link {
    cursor: pointer;
    position: relative;
}

.link:visited {
    color: rgb(148 163 184);
}

.link:hover {
    transition: 0.2s;
    color: rgba(19, 48, 94, 1);
}
</style>