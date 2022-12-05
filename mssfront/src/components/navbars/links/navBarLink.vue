<script setup>
import { defineProps } from "vue";
const props = defineProps({
  text: String,
});
</script>
<template>
  <div class="navbar__button">
    <a href="" class="button__a">{{ props.text }}</a>
  </div>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans&display=swap');

.navbar__button {
  height: 100%;
  font-family: "Fira Sans", sans-serif;
  text-align: center;
  width: max-content;
  font-size: 1.2em;
}

.button__a {
  font-style: normal;
  display: inline-block;
  padding: 20px 30px 15px 25px;
  color: #787474;
  text-decoration: none;
  font-size: 1em;
  padding-bottom: 10px;
}

.button__a:hover {
  color: black;
  cursor: pointer;
}

.button__a:last-child {
  padding-left: 0;
}
</style>
