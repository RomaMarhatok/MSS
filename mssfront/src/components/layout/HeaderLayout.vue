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
  <header :class="props.class">
    <slot></slot>
  </header>
</template>