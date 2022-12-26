<script setup>
import documentListPageCard from '@/components/cards/documentListPageCard.vue';
import { ref, defineProps, computed } from 'vue';
const props = defineProps({
    documents: {
        type: Array,
        default: () => [],
    }
})
const searchString = ref("")
const getDocuments = computed(() => { return props.documents.filter(el => el.name.toLowerCase().includes(searchString.value.toLowerCase())) })
</script>
<template>
    <main class="flex justify-center flex-col mt-4 items-center">
        <div class="flex flex-row justify-center mb-2">
            <div class="search-box">
                <button class="btn-search">
                    <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                </button>
                <input type="text" class="input-search" v-model="searchString" placeholder="Type to Search...">
            </div>
        </div>
        <div class="container">
            <div class="document-list" v-if="props.documents">
                <documentListPageCard v-for="document in getDocuments" :key="document.slug" :document="document" />
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

.btn-search:hover {
    color: white;
    background-color: rgb(19, 48, 94);
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

.container {
    display: flex;
    justify-content: center;
    padding-top: 10px;
    background-color: rgb(38, 77, 141);
    width: 100%;
    border-radius: 10px;
}

.document-list {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-auto-flow: row dense;
    gap: 10px;
    justify-items: center;
}

@media screen and (max-width: 1300px) {
    .document-list {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-auto-flow: row dense;
        justify-items: center;
        width: 80%;
    }

}

@media screen and (max-width: 900px) {
    .document-list {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-auto-flow: row dense;
        justify-items: center;
        width: 80%;
    }

}

@media screen and (max-width: 600px) {
    .document-list {
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        grid-auto-flow: row dense;
        justify-items: center;
        width: 80%;
    }

}
</style>