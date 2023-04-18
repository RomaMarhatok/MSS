<script setup>
import "primeflex/primeflex.css";
import "primevue/resources/themes/lara-light-blue/theme.css";
import "primevue/resources/primevue.min.css";
import { defineProps, ref } from "vue";
import Checkbox from 'primevue/checkbox'
const check = ref(null)
const props = defineProps({
    slug: String,
    name: String,
})
</script>
<template>
    <div class="flex items-end">
        <div class="p-1">
            <Checkbox v-model="check" :value="props.slug" @change="$emit('filter', check)" />
        </div>
        <p class="text-base font">{{ props.name }}</p>
    </div>
</template>
<style lang="css" scoped>
.font {
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
}
</style>