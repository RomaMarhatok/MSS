<script setup>
import { defineProps } from 'vue';
import InputText from "primevue/inputtext";
const props = defineProps({
    labelText: String,
    inputPlaceholder: String,
    inputType: String,
    labelFor: String,
    errors: Object,
})
</script>
<template>
    <div class="field flex flex-col gap-1 w-full">
        <label class="font-black text-lg" :for=props.labelFor>{{ props.labelText }}</label>
        <InputText :placeholder=props.inputPlaceholder :id=props.labelFor :type=props.inputType
            :aria-describedby=props.labelFor class="bg-white border-2 border-solid border-gray-300 rounded-xl text-base p-3 
            focus:outline-none focus:shadow-outline focus:border-blue-300" required />
        <div v-if="props.errors" class="flex flex-col mb-5">
            <small class="p-error" v-for="error in props.errors" :key="error" :id=props.labelFor>
                {{ error }}
            </small>
        </div>
    </div>
</template>