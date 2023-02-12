<script setup>
import { defineProps } from 'vue';
import BaseSelector from './Base/BaseSelector.vue';
const props = defineProps({
    doctors: {
        type: Array,
        default: () => [],
    },
    modelValue: String
})
</script>
<template>
    <BaseSelector :value="props.modelVale" @change="$emit('update:modelValue', $event.target.value)"
        :selectPlaceholder="'select doctor'">
        <option v-for="doctor in props.doctors" :key="doctor.doctor_slug" :value="doctor.doctor_slug">{{
            doctor.personal_info.full_name
        }}
        </option>
    </BaseSelector>
</template>