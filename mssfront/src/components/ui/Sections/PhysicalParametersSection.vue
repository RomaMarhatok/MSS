<script setup>
import Chart from 'primevue/chart'
import { onBeforeMount, computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const slug = computed(() => store.getters["user/getSlug"])
const chartData = computed(() => store.getters["physicalParameters/getChartsDataSet"])
onBeforeMount(() => {
    store.dispatch("physicalParameters/fetchPhysicalParameters", slug.value)
})

</script>
<template>
    <div class="bg-white p-4">
        <Chart type="line" :data="chartData" :height="80" />
    </div>
</template>