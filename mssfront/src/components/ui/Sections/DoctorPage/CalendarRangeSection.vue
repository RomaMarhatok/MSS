<script setup>
import { reactive } from 'vue'
const range = reactive({
    start: new Date(),
    end: new Date(),
})
</script>
<template>
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8" @submit.prevent>
        <div class="mb-4">
            <span class="block text-gray-600 text-sm text-left font-bold mb-2">Select Range</span>
            <v-date-picker v-model="range" mode="dateTime" :masks="'YYYY-MM-DD h:mm A'" is-range>
                <template v-slot="{ inputValue, inputEvents, isDragging }">
                    <div class="flex flex-col sm:flex-row justify-start items-center">
                        <div class="relative flex-grow">
                            <input class="flex-grow pl-8 pr-2 py-1 bg-gray-100 border rounded w-full"
                                :class="isDragging ? 'text-gray-600' : 'text-gray-900'" :value="inputValue.start"
                                v-on="inputEvents.start" />
                        </div>
                        <div class="relative flex-grow">
                            <input class="flex-grow pl-8 pr-2 py-1 bg-gray-100 border rounded w-full"
                                :class="isDragging ? 'text-gray-600' : 'text-gray-900'" :value="inputValue.end"
                                v-on="inputEvents.end" />
                        </div>
                    </div>
                </template>
            </v-date-picker>
        </div>
    </form>
</template>