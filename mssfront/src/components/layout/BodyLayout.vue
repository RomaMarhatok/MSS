<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    class: {
        type: String,
        default: () => ""
    }
})
</script>
<template>
    <main :class="props.class">
        <slot></slot>
    </main>
</template>