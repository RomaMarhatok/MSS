<template>
    <footer class="flex justify-center mt-2">
        <a :href="'http://127.0.0.1:8000/admin/'" class="footer__link">Войти как админ</a>
    </footer>
</template>
<style scoped>
.footer__link {
    cursor: pointer;
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