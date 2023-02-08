<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    sectionTitle: String,
    sectionText: String
})
</script>
<template>
    <section class="resume-section">
        <header class="header__section">
            {{ props.sectionTitle }}
        </header>
        <div class="table-wrapper">
            <p class="label-text">
                {{ props.sectionText }}
            </p>
        </div>
    </section>
</template>
<style scoped>
.resume-section {
    display: flex;
    flex-direction: column;
    width: 70%;
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
    padding: 1rem;
}

.header__section {
    text-align: center;
}

.table-wrapper {
    display: flex;
    justify-content: center;
}

.label-text {
    width: 80%;
}
</style>
