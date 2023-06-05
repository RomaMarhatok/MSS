<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    text: {
        type: String,
        default: () => "default"
    },
    href: String
})
</script>
<template>
    <div class="link-container">
        <a :href="props.href" class="link">{{ props.text }}</a>
    </div>
</template>
<style scoped>
.link {
    text-decoration: none;
    color: inherit;
    width: 100%;
    text-align: center;
}

.link-container {
    display: flex;
    padding-top: 5px;
    padding-bottom: 5px;
    border: 1px solid rgb(165, 165, 165);
    color: black;
}

.link-container:hover {
    transition: 300ms;
    border-radius: 10px;
    background-color: rgba(19, 48, 94, 1);
    color: white;
}
</style>