<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref } from 'vue'
const items = ref([
    { label: 'Home', icon: 'pi pi-fw pi-home', to: "/home/" },
    { label: 'Doctors', icon: 'pi pi-fw pi-calendar', to: "/doctors/" },
    { label: 'Documents', icon: 'pi pi-fw pi-file', to: "/home/documents/" },
    { label: 'Sign out', icon: 'pi pi-fw pi-sign-out', to: '/' }
])
</script>
<template>
    <TabMenu :model="items"></TabMenu>
</template>
<style>
@media screen and (max-width:515px) {
    .p-tabmenu-nav {
        display: flex;
        flex-direction: column;
    }
}
</style>