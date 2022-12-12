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
  text: "Log in",
  link: "#/registration/",
})
const signUp = reactive({
  text: "Sign up",
  link: "#/authentication/"
})
</script>
<template>
  <nav class="w-11/12 flex flex-row justify-end gap-4">
    <nav-bar-link :text="aboutLink.text" :link="aboutLink.link" />
    <nav-bar-link :text="contactsLink.text" :link="contactsLink.link" />
    <nav-bar-link :text="homeLink.text" :link="homeLink.link" />
    <nav-bar-link :text="loginLink.text" :link="loginLink.link" />
    <nav-bar-link :text="signUp.text" :link="signUp.link" />
  </nav>
</template>