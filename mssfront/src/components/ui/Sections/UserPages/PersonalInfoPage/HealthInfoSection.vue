<script setup>
import dataSection from './Base/DataSection.vue';
import { computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const healthInfo = computed(() => store.getters["user/getHealthInfo"])
</script>
<template>
    <dataSection :headerText="'Health info'" :data="healthInfo" />
</template>