<script setup>
import navBarLink from "@/components/common/Links/HomePageNavBarLink.vue";
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
  text: "SignUp",
  link: "#/registration/",
})
const signUp = reactive({
  text: "Login",
  link: "#/authentication/"
})
</script>
<template>
  <nav class="w-11/12 flex flex-row justify-end gap-4 max-[600px]:flex-col max-[600px]:items-center max-[600px]:w-full">
    <navBarLink :text="aboutLink.text" :link="aboutLink.link" />
    <navBarLink :text="contactsLink.text" :link="contactsLink.link" />
    <navBarLink :text="homeLink.text" :link="homeLink.link" />
    <navBarLink :text="loginLink.text" :link="loginLink.link" />
    <navBarLink :text="signUp.text" :link="signUp.link" />
  </nav>
</template>