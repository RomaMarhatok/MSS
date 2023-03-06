<script setup>
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
import Dropdown from 'primevue/dropdown'
import { ref, defineProps } from 'vue'
const props = defineProps({
    selectionValues: {
        type: Array,
        default: () => [],
    },
    modelValue: String
})
const selectedValue = ref(null)
</script>
<template>
    <div>
        <Dropdown class="w-full" v-model="selectedValue" :value="props.modelValue"
            @change="$emit('update:modelValue', $event.value)" optionLabel="full_name" :options="props.selectionValues" />
    </div>
</template>