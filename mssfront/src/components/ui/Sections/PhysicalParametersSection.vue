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
    <main>
        <div v-if="!chartData.labels.length" class="flex justify-center bg-white p-4">
            <p class="text-3xl text-slate-400">Информации о физ. параметрах пока нет.</p>
        </div>
        <div v-else class="bg-white p-4">
            <Chart type="line" :data="chartData" :height="80" />
        </div>
    </main>
</template>