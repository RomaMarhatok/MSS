<script setup>
import navBarLink from "@/components/common/Links/NavBarLink.vue";
import { reactive } from "vue";
const homeLink = reactive({
  text: "Главная",
  link: "#/",
})
const loginLink = reactive({
  text: "Зарегистрироваться",
  link: "#/registration/",
})
const signUp = reactive({
  text: "Войти",
  link: "#/authentication/"
})
const aboutLink = reactive({
  text: 'Справка',
  link: '#/about/'
})
const aboutProgramLink = reactive({
  text: 'О программе',
  link: '#/about-program/'
})
</script>
<template>
  <nav class="nav-bar">
    <navBarLink :text="homeLink.text" :link="homeLink.link" />
    <navBarLink :text="loginLink.text" :link="loginLink.link" />
    <navBarLink :text="signUp.text" :link="signUp.link" />
    <navBarLink :text="aboutLink.text" :link="aboutLink.link" />
    <navBarLink :text="aboutProgramLink.text" :link="aboutProgramLink.link" />
  </nav>
</template>
<style lang="css" scoped>
/**flex flex-row w-full justify-end gap-4 max-[600px]:flex-col max-[600px]:items-center */
.nav-bar {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: flex-end;
  gap: 1em;
  padding-right: 1em;
}

@media screen and (max-width: 600px) {
  .nav-bar {
    flex-direction: column;
    align-items: center;
    gap: 0;
  }
}
</style>