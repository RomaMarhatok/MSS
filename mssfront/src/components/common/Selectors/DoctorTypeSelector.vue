<script setup>
import { defineProps } from 'vue';
import BaseSelector from './Base/BaseSelector.vue';
const props = defineProps({
    doctorTypes: {
        type: Array,
        default: () => []
    },
    modelValue: String

})
</script>
<template>
    <BaseSelector :value="props.modelValue" @change="$emit('update:modelValue', $event.target.value)"
        :select-placeholder="'select doctor type'">
        <option v-for="doctorType in props.doctorTypes" :key="doctorType.slug" :value="doctorType.slug">{{
            doctorType.name
        }}
        </option>
    </BaseSelector>
</template>