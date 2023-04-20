<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import Dialog from "primevue/dialog";
import Menu from 'primevue/menu'
import AddTreatmentHistoryForm from '@/components/ui/Forms/treatmentHistoryForms/AddTreatmentHistoryForm.vue';
const store = useStore()
const selectedAppointment = computed(() => store.getters["appointment/getSelectedAppointment"])
const dialog = ref(false)
const menu = ref(false)
const menuOptions = ref([
    {
        label: "Действия",
        items: [
            {
                label: "Добавить",
                icon: 'pi pi-plus',
                command: () => {
                    dialog.value = !dialog.value
                }
            }
        ]
    }
])
const toggle = (event) => menu.value.toggle(event)
</script>
<template>
    <main>
        <button class="p-panel-header-icon p-link mr-2" @click="toggle">
            <span class="pi pi-cog"></span>
        </button>
        <Menu ref="menu" :model="menuOptions" id="config_menu" popup />
        <Dialog v-model:visible="dialog" modal header="Добавить запись" :style="{ width: '50vw' }">
            <AddTreatmentHistoryForm :patient_slug="selectedAppointment.patient.slug"
                :doctor_slug="selectedAppointment.doctor.slug" />
        </Dialog>
    </main>
</template>