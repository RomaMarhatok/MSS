<script setup>
import mssLogo from "./logo/mssLogo.vue";
import frontPageNavBar from "../navbars/frontPageNavBar.vue";
</script>
<template>
  <header class="header">
    <mss-logo />
    <front-page-nav-bar />
  </header>
</template>
<style scoped>
.header {
  display: flex;
  flex-direction: row;
}
</style>