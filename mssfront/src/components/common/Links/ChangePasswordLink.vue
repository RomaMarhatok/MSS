<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const redirect = () => router.push({ name: "pre-reset-password-page" })
</script>
<template>
    <footer class="flex justify-center mt-2">
        <a @click="redirect" class="footer__link">Забыли свой пароль ?</a>
    </footer>
</template>
<style scoped>
.footer__link {
    color: black;
    position: relative;
    padding: 0.2em 0;
}

.footer__link:visited {
    color: black;
}

.footer__link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 0.1em;
    background-color: rgba(19, 48, 94, 1);
    opacity: 0;
    transition: opacity 300ms, transform 300ms;
}

.footer__link:hover {
    transition: 0.2s;
    color: rgba(19, 48, 94, 1);
}

.footer__link:hover::after,
.footer__link:focus::after {
    opacity: 1;
    transform: translate3d(0, 0.2em, 0);
}
</style>