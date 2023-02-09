<script setup>
import { useStore } from 'vuex'
import { reactive, computed } from 'vue'
import DataSection from './Base/DataSection.vue';
const store = useStore()
const recentAppoitments = reactive({
    header: "recent appoitments",
    data: [],
})
recentAppoitments.data = computed(() => store.getters["user/getRecentAppointments"])
</script>
<template>
    <DataSection v-if="recentAppoitments.data.length" :headerText="recentAppoitments.header"
        :data="recentAppoitments.data" />
</template>