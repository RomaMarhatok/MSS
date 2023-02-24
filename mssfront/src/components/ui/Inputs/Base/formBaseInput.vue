<script setup>
import { defineProps, ref, computed } from 'vue';
import InputText from "primevue/inputtext";
const props = defineProps({
    labelText: String,
    inputPlaceholder: String,
    inputType: String,
    labelFor: String,
    errors: {
        type: Array,
        default: () => []
    }
})
const baseStyle = ref("bg-white border-2 border-solid border-gray-300 rounded-xl text-base p-3 focus:outline-none focus:shadow-outline focus:border-blue-300")
const withErrors = ref("bg-white border-2 border-solid border-gray-300 rounded-xl text-base p-3 focus:outline-none focus:shadow-outline border-red-500")
const inputStyle = computed(() => {
    return props.errors.length ? withErrors.value : baseStyle.value
})

</script>
<template>
    <div class="field flex flex-col gap-1 w-full">
        <label class="font-black text-lg" :for=props.labelFor>{{ props.labelText }}</label>
        <InputText :placeholder=props.inputPlaceholder :id=props.labelFor :type=props.inputType
            :aria-describedby=props.labelFor :class=inputStyle required />
        <div v-if="props.errors" class="flex flex-col mb-5">
            <small class="text-red-500" v-for="error in props.errors" :key="error" :id=props.labelFor>
                {{ error }}
            </small>
        </div>
    </div>
</template>