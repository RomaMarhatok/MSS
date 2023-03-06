<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const redirect = () => router.push("/home/")
</script>
<template>
    <header class="flex flex-col">
        <div class="flex bg-custom-dark-blue w-full">
            <div class="pl-5 font-extrabold text-3xl text-white underline decoration-3 hover:cursor-pointer"
                @click="redirect">MSS</div>
        </div>
    </header>
</template>