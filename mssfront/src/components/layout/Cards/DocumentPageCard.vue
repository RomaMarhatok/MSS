<script setup>
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import { defineProps, computed } from 'vue';
import { useRouter } from 'vue-router';
import Card from 'primevue/card'
const router = useRouter()
const props = defineProps({
    document: Object
})
const getIcon = computed(() => {
    let className = ""
    if (props.document.document_type.name == "test") {
        className = "fa-solid fa-flask"
    }
    if (props.document.document_type.name == "analyzes") {
        className = "fa-solid fa-vials"
    }
    if (props.document.document_type.name == "conclusions") {
        className = "fa-solid fa-file"
    }
    return className
})
console.log(props)
const redirect = (slug) => router.push(`/home/document/${slug}/`)
</script>
<template>
    <Card @click="redirect(props.document.slug)" class="w-full  hover:cursor-pointer">
        <template #title>
            <div class="flex flex-row gap-2 text-center align-bottom">
                <div>
                    <font-awesome-icon :icon="getIcon" />
                </div>
                {{ props.document.document_type.name }}
            </div>
        </template>
        <template #content>
            <p>{{ props.document.name }}</p>
        </template>
    </Card>
</template>