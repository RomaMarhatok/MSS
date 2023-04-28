<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex';
import Toast from 'primevue/toast'
import Chart from 'primevue/chart';
import addPhysicalParameterDialog from "@/components/ui/Dialogs/addPhysicalParameterDialog.vue";
import PhysicalService from '@/../services/PhysicalService';
import { useToast } from 'primevue/usetoast';
const store = useStore()
const toast = useToast()
const physicalService = new PhysicalService()
const physicalParameters = computed(() => store.getters["treatments/getPhysicalParameters"])
const chartData = (ph) => {
    let chData = {
        labels: ["Вес", "Рост", "Давление"],
        datasets: [
            {
                label: ph.created_at,
                data: [ph.weight, ph.height, ph.pressure],
                backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)'],
                borderColor: ['rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(54, 162, 235)'],
            }
        ],
    }
    return chData
}
const deletePhysicalParameter = (physicalParameterSlug) => {
    physicalService.deletePhysicalParameters({
        slug: physicalParameterSlug
    }).then(response => {
        if (response.status == 200) {
            store.commit("treatments/deletePhysicalParameter", response.data.physical_parameters_deleted_slug)
            toast.add({ severity: 'success', summary: 'Успех', detail: 'Запись удалена', life: 3000 });
        }
    }).catch(error => console.log(error))
}
</script>
<template>
    <div class="flex flex-col gap-2 p-2 rounded-md">
        <div>
            <Toast />
            <addPhysicalParameterDialog />
        </div>
        <div class="grid p-4">
            <div v-for="(ph, index) in physicalParameters" :key="index" class="bg-white rounded-md">
                <button @click="deletePhysicalParameter(ph.slug)"><i class="pi pi-times"></i></button>
                <div class="flex flex-col gap-1 p-1 w-fit">
                    <Chart type="bar" :data="chartData(ph)" />
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="css" scoped>
.grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 1em 1em;
}
</style>