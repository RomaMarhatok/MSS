<script setup>
import documentPageCard from '@/components/cards/documentPageCard.vue';
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore()
const searchString = ref("")
const selectedDocumentType = ref(null)
const documentTypes = computed(() => store.state.user.documentTypes)
const documents = computed(() => filter())
const filter = () => {
    let documentsBySearchString = store.getters["user/getDocumentByString"](searchString.value)
    if (selectedDocumentType.value) {
        let documentsBydocumentType = store.getters["user/getDocumentsByDocumentType"](selectedDocumentType.value)
        let result = documentsBySearchString.filter(d => documentsBydocumentType.some(document => document.document_type.name == d.document_type.name))
        return result
    }
    return documentsBySearchString
}
</script>
<template>
    <main class="flex justify-center flex-col mt-4 items-center">
        <section class="flex flex-row gap-7 mb-4">
            <div class="flex flex-row justify-center mb-2">
                <div class="search-box">
                    <button class="btn-search">
                        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
                    </button>
                    <input type="text" class="input-search" v-model="searchString" placeholder="Type to Search...">
                </div>
            </div>
            <div class="flex justify-center">
                <div class="w-96 h-full">
                    <select class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal 
                    text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded
                    transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 
                    focus:outline-none h-full" v-model="selectedDocumentType">
                        <option disabled value="" selected>Please select document type</option>
                        <option value=""></option>
                        <option v-for="documentType in documentTypes" :key="documentType.slug" :value="documentType">{{
                            documentType.name
                        }}
                        </option>
                    </select>
                </div>
            </div>
        </section>

        <div class="container">
            <div class="document-list" v-if="documents">
                <documentPageCard v-for="document in documents" :key="document.slug" :document="document" />
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
    padding-bottom: 1rem;
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