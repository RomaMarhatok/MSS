<script setup>
import navBarLink from "./links/navBarLink.vue";
import { ref } from "vue";
const about = ref("About");
const contacts = ref("Contacts");
const home = ref("Home");
const login = ref("Login");
</script>
<template>
  <nav class="header__navbar">
    <nav-bar-link :text="about" />
    <nav-bar-link :text="contacts" />
    <nav-bar-link :text="home" />
    <nav-bar-link :text="login" />
  </nav>
</template>
<style>
.header__navbar {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
</style>