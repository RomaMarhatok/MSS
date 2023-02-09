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
                <div class="label">
                    <p>{{ el.label }}</p>
                </div>
                <div class="label-text">
                    <p>{{ el.text }}</p>
                </div>
            </div>
        </div>
    </section>
</template>
<style scoped>
.table-display-section {
    background-color: #ffffff;
    border-radius: 5px;
    padding: 10px;
    width: 60%;
    border: 1px solid rgb(218, 218, 218);
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
    box-sizing: border-box;
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
}

.label {
    display: flex;
    justify-content: flex-start;
    font-weight: 900;
    padding-right: 2rem;
    min-width: 20%;
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

@media screen and (max-width: 1350px) {
    .table-display-section {
        align-items: center;
        gap: 0.5rem;
    }

    .table-wrapper {
        display: flex;
        flex-direction: column;
    }

    .label {
        padding: 0;
        width: 100%;
        text-align: center;
    }

}

@media screen and (max-width: 900px) {
    .table-display-section {
        width: 100%;
        gap: 0.5rem;
    }
}
</style>