<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const appointments = computed(() => store.getters["appointments/getAllAppointmentsForCalendar"])
</script>
<template>
    <div class="text-center section">
        <v-calendar class="custom-calendar max-w-full" :attributes="appointments" disable-page-swipe is-expanded
            locale="en">
            <template v-slot:day-content="{ day, attributes }">
                <div class="vc-day flex flex-col h-full z-10 overflow-hidden">
                    <span class="day-label text-sm text-gray-900">{{ day.day }}</span>
                    <div class="flex-grow overflow-y-auto overflow-x-auto">
                        <button v-for="attr in attributes" :key="attr.key" onclick="alert(1)"
                            class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1 w-full" :class="attr.customData.class">
                            {{ attr.customData.title }}
                        </button>
                    </div>
                </div>
            </template>
        </v-calendar>
    </div>
</template>
<style lang="css" scoped>
.vc-day {
    padding: 0 5px 3px 5px;
    text-align: left;
    height: 90px;
    min-width: var(90px);
    background-color: #f8fafc;
    border: 1px solid #eaeaea;
    padding: 5px 0;
}
</style>