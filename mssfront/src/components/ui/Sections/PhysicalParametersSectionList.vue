<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex';
import Toast from 'primevue/toast'
import addPhysicalParameterDialog from "@/components/ui/Dialogs/addPhysicalParameterDialog.vue";
import PhysicalService from '@/../services/PhysicalService';
import { useToast } from 'primevue/usetoast';
const store = useStore()
const toast = useToast()
const physicalService = new PhysicalService()
const physicalParameters = computed(() => store.getters["treatments/getPhysicalParameters"])
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
    <div class="bg__section flex flex-col gap-2 p-2">
        <div>
            <Toast />
            <addPhysicalParameterDialog />
        </div>
        <div class="flex flex-col gap-2 p-2">
            <div v-for="(ph, index) in physicalParameters" :key="index" class="flex justify-between bg-white rounded-md">
                <div class="flex gap-4 p-1 w-fit">
                    <p>вес: {{ ph.weight }}</p>
                    <p>рост: {{ ph.height }}</p>
                    <p>давление: {{ ph.pressure }}</p>
                </div>
                <button @click="deletePhysicalParameter(ph.slug)"><i class="pi pi-times"></i></button>
            </div>

        </div>
    </div>
</template>
<style lang="css" scoped>
.bg__section {
    background-color: rgba(110, 131, 165, 0.103);
}
</style>