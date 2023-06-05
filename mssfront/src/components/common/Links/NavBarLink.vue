<script setup>
import { defineProps } from "vue";
const props = defineProps({
  text: String,
  link: String,
});
</script>
<template>
  <div class="h-full text-left w-max">
    <a :href="props.link" class="link flex w-full h-full text-lg justify-center items-center">
      {{ props.text }}
    </a>
  </div>
</template>
<style lang="css" scoped>
.link {
  color: rgb(75 85 99);
}

.link:hover {
  color: black;
}
</style>