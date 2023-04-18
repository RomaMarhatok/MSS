<script setup>
import { defineProps, ref, computed } from 'vue'
import { useStore } from 'vuex';
import TreatmentHistoryService from '@/../services/TreatmentHistoryService';
import Dialog from "primevue/dialog";
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
const treatmentHistoryService = new TreatmentHistoryService()
const toast = useToast()
const store = useStore()
const props = defineProps({
    treatmentHistorySlug: String,
})
const images = computed(() => store.getters["treatments/getImageForAnalyzes"](props.treatmentHistorySlug))
const dialog = ref(false)
const imageSlug = ref("")
const selectImage = (slug) => {
    dialog.value = true
    imageSlug.value = slug
}
const selectedImage = computed(() => {
    if (imageSlug.value.length) {
        return images.value.find(img => img.slug == imageSlug.value)
    }
    return {
        image: "",
        description: "Изображение не найдено"
    }
})

const deleteImage = (imgSlug) => {
    const data = {
        treatment_history_slug: props.treatmentHistorySlug,
        image_for_analyzes_slug: imgSlug
    }
    console.log(data)
    treatmentHistoryService.deleteTreatmentHistoryImageForAnalyze(data).then(response => {
        if (response.status == 200) {
            store.commit("treatments/deleteImageForAnalyze", {
                imageSlug: response.data.deleted_image_slug,
                treatmentHistorySlug: response.data.treatment_history_slug
            })
            toast.add({ severity: 'success', summary: 'Успех', detail: 'Запись удалена', life: 3000 });
        }
    }).catch(error => console.log(error))
}
</script>
<template>
    <Toast />
    <div class="p-2">
        <p>Прилогающиеся изображения</p>
        <div v-if="!images.length">
            <p>НЕТ</p>
        </div>
        <div v-else v-for="(img, index) in images" :key="img.slug" class="flex justify-between">
            <p @click="selectImage(img.slug)" class="cursor-pointer">{{ index + 1 }}.{{ img.description }}</p>
            <button @click="deleteImage(img.slug)"><i class="pi pi-times"></i></button>
        </div>
    </div>
    <Dialog v-model:visible="dialog" modal header="Изображение" :style="{ width: '70vw' }">
        <p>{{ selectedImage.description }}</p>
        <img :src="selectedImage.image" />
    </Dialog>
</template>