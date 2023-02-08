<script setup>
import { defineProps, computed, getCurrentInstance } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()
const route = useRoute()
const props = defineProps({
    document: Object
})
const component = getCurrentInstance()

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
function redirectOnSingleDocumentPage() {
    const documentSlug = component.vnode.key
    const userSlug = route.params.userSlug
    router.push(`/user/${userSlug}/document/${documentSlug}/`)
}
</script>
<template>
    <button class="p-3 cursor-pointer bg-none border-none bg-white rounded-2xl hover:bg-sky-300 hover:text-white"
        @click="redirectOnSingleDocumentPage">
        <div class="text-6xl">
            <font-awesome-icon :icon="getIcon" />
        </div>
        <div>
            <p>
                {{ props.document.name }}
            </p>
        </div>
    </button>
</template>