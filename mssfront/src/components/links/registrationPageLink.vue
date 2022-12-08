<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    link: String
})
</script>
<template>
    <footer class="footer">
        <a :href="props.link" class="footer__link">Forgot your password ?</a>
    </footer>
</template>
<style scoped>
.footer {
    margin-top: 30px;
    display: flex;
    justify-content: center;
}

.footer__link {
    color: black;
}

.footer__link:visited {
    color: black;
}

.footer__link:hover {
    color: rgba(19, 48, 94, 1);
}
</style>