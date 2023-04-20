<script setup>
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import DoctorTabMenu from '@/components/ui/Menu/DoctorTabMenu.vue';
import ChangeDocumentForm from '@/components/ui/Forms/documentForms/ChangeDocumentForm.vue';
import { onBeforeMount, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const activeDocument = computed(() => store.getters["doctorDocuments/getActiveDocument"])
console.log("CHANGE DOCUMENT VIEW", activeDocument.value)
onBeforeMount(() => {
    store.dispatch("patients/fetchPatients")
})
</script>
<template>
    <HeaderLayout>
        <DoctorTabMenu />
    </HeaderLayout>
    <main class="flex flex-col justify-center  p-2">
        <div class="flex justify-center text-2xl">
            <p>Изменить документ</p>
        </div>
        <div class="flex justify-center">
            <ChangeDocumentForm :document="activeDocument" />
        </div>
    </main>
</template>