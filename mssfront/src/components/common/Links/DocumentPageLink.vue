<script setup>
import { defineProps, computed } from "vue";
import { useRoute } from "vue-router";
const route = useRoute()
const props = defineProps({
    href: String,
    text: String,
    active: Boolean
})
const getButtonStyle = computed(() => {
    return !props.active ? "button" : "button active"
})
const getHref = computed(() => {
    return !props.active ? props.href : `#${route.path}`
})
</script>
<template>
    <div :class="getButtonStyle">
        <a class="link" :href=getHref>
            {{ props.text }}
        </a>
    </div>
</template>
<style>
/* "flex border-3 w-fit py-2 px-4 rounded-xl text-black hover:bg-header-dark-blue hover:text-white hover:duration-100" */
.button {
    display: flex;
    border-width: 3px;
    width: fit-content;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
    border-radius: 0.75rem;
    --tw-text-opacity: 1;
    color: rgb(0 0 0 / var(--tw-text-opacity));
}

.button:hover {
    --tw-bg-opacity: 1;
    background-color: rgb(16 32 57 / var(--tw-bg-opacity));
    color: white;
    animation-duration: 100ms;
}

.button.active {
    display: flex;
    border-width: 3px;
    width: fit-content;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
    border-radius: 0.75rem;
    color: white;
    background-color: rgb(16, 32, 57);
}

/* "flex justify-center items-center font-normal text-inherit text-lg cursor-pointer" */
link {
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 400;
    color: inherit;
    font-size: 1.125rem;
    line-height: 1.75rem;
    cursor: pointer;
}
</style>