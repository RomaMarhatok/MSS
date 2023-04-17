<script setup>
import { defineProps, ref, computed } from 'vue'
import Dialog from "primevue/dialog";
const props = defineProps({
    images: {
        type: Array,
        default: () => []
    }
})
const dialog = ref(false)
const imageSlug = ref("")
const selectImage = (slug) => {
    dialog.value = true
    imageSlug.value = slug
}
const selectedImage = computed(() => {
    if (imageSlug.value.length) {
        return props.images.find(img => img.slug == imageSlug.value)
    }
    return {
        image: "",
        description: "Изображение не найдено"
    }
})


</script>
<template>
    <div class="p-2">
        <p>Прилогающиеся изображения</p>
        <div v-if="!props.images.length">
            <p>НЕТ</p>
        </div>
        <div v-else v-for="img in props.images" :key="img.slug">
            <p @click="selectImage(img.slug)" class="cursor-pointer">{{ img.description }}</p>
        </div>
    </div>
    <Dialog v-model:visible="dialog" modal header="Изображение" :style="{ width: '70vw' }">
        <p>{{ selectedImage.description }}</p>
        <img :src="selectedImage.image" />
    </Dialog>
</template>