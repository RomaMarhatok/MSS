<script setup>
import { defineProps } from "vue";
const props = defineProps({
  text: String,
  link: String,
});
</script>
<template>
  <div class="h-full text-left w-max">
    <a :href="props.link" class="button__a flex w-full h-full text-gray-600 text-lg justify-center items-center">
      {{ props.text }}
    </a>
  </div>
</template>
<style scoped>
.button__a:hover {
  color: black;
  cursor: pointer;
}
</style>
