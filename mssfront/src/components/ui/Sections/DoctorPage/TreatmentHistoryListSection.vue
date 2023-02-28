<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const treatmentHistories = computed(() => store.getters["treatments/getTreatmentsHistories"])
</script>
<template>
    <main class="treatment-container">
        <p>Treatment history</p>
        <div class="treatment-item">
            <div v-for="(treatmentHistory, i) in treatmentHistories" :key="i">
                <div class="patient">
                    created_at {{ treatmentHistory.created_at }}
                </div>
            </div>
        </div>
    </main>
</template>
<style lang="css">
.treatment-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
    padding: 1rem;
}


.treatment-item {
    display: flex;
    flex-direction: row;
    padding: 1rem;
    transition: 100ms;

}

.treatment-item:hover {
    transition: 1000ms;
    box-shadow: 1px 0px 8px 0px rgba(90, 244, 105, 0.8);
    border-radius: 20px;
}
</style>
