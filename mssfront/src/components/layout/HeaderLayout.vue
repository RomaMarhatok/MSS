<script setup>
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
import { useRouter } from 'vue-router'
const router = useRouter()
const redirect = () => router.push("/home/")
</script>
<template>
  <header class="header__wrapper">
    <p class="text" @click="redirect">MSS</p>
    <TabMenu />
  </header>
</template>
<style lang="css" scoped>
.header__wrapper {
  display: flex;
  justify-content: space-between;
  background-color: rgb(19 48 94);
  box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
}

@media screen and (max-width: 900px) {

  .header__wrapper {
    flex-direction: column;
  }

}

.text {
  display: inline-block;
  font-weight: 600;
  font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  font-size: 2em;
  text-decoration: underline;
  cursor: pointer;
  color: #fff;
  padding-left: 10px;
}
</style>