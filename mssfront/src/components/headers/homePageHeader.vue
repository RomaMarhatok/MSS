<script setup>
import mssLogo from "./logo/mssLogo.vue";
import homePageNavBar from "@/components/navbars/homePageNavBar.vue";
</script>
<template>
  <header class="header">
    <mssLogo />
    <homePageNavBar />
  </header>
</template>
<style scoped>
.header {
  display: flex;
  flex-direction: row;
}
</style>