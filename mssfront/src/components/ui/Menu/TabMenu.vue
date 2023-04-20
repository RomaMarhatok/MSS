<script setup>
import TabMenu from 'primevue/tabmenu';
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import { ref } from 'vue'
const items = ref([
    { label: 'Home', icon: 'pi pi-fw pi-home', to: "/home/" },
    { label: 'Doctors', icon: 'pi pi-fw pi-calendar', to: "/home/doctors/" },
    { label: 'Documents', icon: 'pi pi-fw pi-file', to: "/home/documents/" },
    { label: "Treatments", icon: 'pi pi-file', to: "/home/treatments/" },
    { label: 'Log out', icon: 'pi pi-fw pi-sign-out', to: '/logout/' },
])
</script>
<template>
    <TabMenu :model="items"></TabMenu>
</template>
<style>
@media screen and (max-width:660px) {
    .p-tabmenu-nav {
        display: flex;
        flex-direction: column;
    }
}
</style>