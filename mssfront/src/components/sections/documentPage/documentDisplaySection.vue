<script setup>
import documentListPageCard from '@/components/cards/documentListPageCard.vue';
import { defineProps } from 'vue';
const props = defineProps({
    documents: Object
})
</script>
<template>
    <main class="mt-4 w-full">
        <div class="flex flex-row justify-center">
            <div class="search-box">
                <button class="btn-search">
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                </button>
                <input type="text" class="input-search" placeholder="Type to Search...">
            </div>
            <div class="flex flex-row justify-evenly gap-8">
                <button class="display-button">
                    <font-awesome-icon icon="fa-solid fa-table-cells" class="text-4xl" />
                </button>
                <button class="display-button">
                    <font-awesome-icon icon="fa-solid fa-table-cells-large" class="text-4xl" />
                </button>
                <button class="display-button">
                    <font-awesome-icon icon="fa-solid fa-list" class="text-4xl" />
                </button>
            </div>
        </div>
        <div
            class="grid-cols-5 grid-flow-row-dense gap-3 justify-center w-4/5 max-[600px]:grid-cols-1 max-[900px]:grid-cols-2 max-[1300px]:grid-cols-3">
            <div v-if="props.documents">
                <documentListPageCard v-for="(document, index) in props.documents" :key="index" :document="document" />
            </div>
        </div>
    </main>
</template>
<style scoped>
.display-button {
    display: flex;
    padding: 5px;
    font-size: 2em;
    background: none;
    border: none;
    cursor: pointer;
}

.display-button:hover {
    border-radius: 10px;
    background-color: skyblue;
}

.search-box {
    width: fit-content;
    height: fit-content;
    position: relative;
}

.input-search {
    height: 50px;
    width: 50px;
    border-style: none;
    padding: 10px;
    font-size: 18px;
    letter-spacing: 2px;
    outline: none;
    border-radius: 25px;
    transition: all .5s ease-in-out;
    background-color: white;
    padding-right: 40px;
    color: black;
}

.input-search::placeholder {
    color: rgba(255, 255, 255, .5);
    font-size: 18px;
    letter-spacing: 2px;
    font-weight: 100;
}

.btn-search {
    width: 50px;
    height: 50px;
    border-style: none;
    font-size: 20px;
    font-weight: bold;
    outline: none;
    cursor: pointer;
    border-radius: 50%;
    position: absolute;
    right: 0px;
    color: black;
    background-color: transparent;
    pointer-events: painted;
}

.btn-search:focus~.input-search {
    width: 300px;
    border-radius: 0px;
    background-color: transparent;
    border-bottom: 1px solid rgba(11, 11, 11, 0.5);
    transition: all 500ms cubic-bezier(0, 0.110, 0.35, 2);
}

.input-search:focus {
    width: 300px;
    border-radius: 0px;
    background-color: transparent;
    border-bottom: 1px solid rgba(11, 11, 11, 0.5);
    transition: all 500ms cubic-bezier(0, 0.110, 0.35, 2);
}
</style>