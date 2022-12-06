<script setup>
import navBarLink from "./links/navBarLink.vue";
import { reactive } from "vue";
const aboutLink = reactive({
  text: "about",
  link: "#/",
})
const contactsLink = reactive({
  text: "contacts",
  link: "#/",
})
const homeLink = reactive({
  text: "home",
  link: "#/"
})
const loginLink = reactive({
  text: "login",
  link: "#/registration/",
})
</script>
<template>
  <nav class="header__navbar">
    <nav-bar-link :text="aboutLink.text" :link="aboutLink.link" />
    <nav-bar-link :text="contactsLink.text" :link="contactsLink.link" />
    <nav-bar-link :text="homeLink.text" :link="homeLink.link" />
    <nav-bar-link :text="loginLink.text" :link="loginLink.link" />
  </nav>
</template>
<style scoped>
.header__navbar {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
</style>