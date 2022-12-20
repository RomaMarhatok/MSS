<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    headerText: String,
    data: {
        type: Array,
        default: () => []
    }
})
</script>
<template>
    <section class="table-display-section">
        <header class="section-header">
            {{ props.headerText }}
        </header>
        <div v-if="props.data">
            <div class="table-wrapper" v-for="(el, index) in props.data" :key="index">
                <p class="label">{{ el.label }}</p>
                <p class="label-text">{{ el.text }}</p>
            </div>
        </div>
    </section>
</template>
<style>
.table-display-section {
    background-color: #ffffff;
    border-radius: 5px;
    padding: 10px;
    width: 60%;
    border: 1px solid rgb(218, 218, 218);
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
    box-sizing: border-box;
}

@media screen and (max-width: 900px) {
    .table-display-section {
        width: 100%;
    }
}

.section-header {
    font-size: 2em;
    text-transform: uppercase;
    word-break: break-all;
}

.table-wrapper {
    display: flex;
    flex-direction: row;
    border-bottom: 2px solid rgb(195, 191, 191);
    gap: 2em;
}

.label {
    width: 10%;
    display: flex;
    justify-content: flex-start;
    font-weight: 900;
}

.label-text {
    width: 100%;
    word-break: break-all;
    color: rgb(145, 143, 143);
}

.table-wrapper:hover .label-text {
    color: skyblue;
}

.table-wrapper:hover .label {
    color: skyblue;

}
</style>