<script setup>
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import DoctorTabMenu from '@/components/ui/Menu/DoctorTabMenu.vue';
import AddDocumentForm from '@/components/ui/Forms/documentForms/AddDocumentForm.vue';
import { onBeforeMount } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
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
            <p>Добавить новый документ</p>
        </div>
        <div class="flex justify-center">
            <AddDocumentForm />
        </div>
    </main>
</template>