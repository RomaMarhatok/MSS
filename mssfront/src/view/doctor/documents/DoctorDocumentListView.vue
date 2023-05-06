<script setup>
import "primeflex/primeflex.css";
import "primevue/resources/themes/lara-light-blue/theme.css";
import "primevue/resources/primevue.min.css";

import { useRoute, useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { onMounted, computed, ref } from 'vue';
import { Field } from "vee-validate";

import RadioButton from 'primevue/radiobutton';
import ContextMenu from 'primevue/contextmenu';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import DoctorTabMenu from '@/components/ui/Menu/DoctorTabMenu.vue'
import PrimaryCheckBox from "@/components/ui/CheckBoxes/PrimaryCheckBox.vue";
import DocumentService from "@/../services/DocumentService";
const documentService = new DocumentService()
const store = useStore()
const route = useRoute()
const router = useRouter()
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)
const activeDocumentSlug = ref("")
const contextMenu = ref()
const contextMenuOptions = ref([
    {
        label: 'Изменить',
        icon: 'pi pi-fw pi-file-edit',
        command: () => {
            router.push("/doctor/change/document/")
        }
    },
    {
        label: 'Удалить',
        icon: 'pi pi-fw pi-trash',
        command: () => {
            deleteDocument()
        }
    }
]);
const DOCUMENT_TYPE_FILTER = ref([])
const DOCUMENT_DATE_FILTER = ref(null)
const DOCUMENT_NAME_FILTER = ref("")
const DOCUMENT_ORDER_FILTER = ref("")

const documentsTypes = computed(() => store.getters["doctorDocuments/getDocumentTypes"])
const filterDocuments = computed(() => {
    let documents = store.getters["doctorDocuments/getDocuments"]

    if (DOCUMENT_TYPE_FILTER.value.length) {
        documents = documents.filter((document) => DOCUMENT_TYPE_FILTER.value.indexOf(document.document_type.slug) != -1)
    }

    if (DOCUMENT_DATE_FILTER.value != null && DOCUMENT_DATE_FILTER.value != "") {
        const compareDate = new Date(DOCUMENT_DATE_FILTER.value)
        documents = documents.filter((document) => {
            const documentDate = new Date(document.created_at)
            return compareDate.getDate() == documentDate.getDate()
                && compareDate.getFullYear() == documentDate.getFullYear()
                && compareDate.getMonth() == documentDate.getMonth()
        })
    }

    if (DOCUMENT_NAME_FILTER.value) {
        documents = documents.filter((document) => document.name.toLowerCase().includes(DOCUMENT_NAME_FILTER.value.toLowerCase()))
    }
    if (DOCUMENT_ORDER_FILTER.value != "") {
        if (DOCUMENT_ORDER_FILTER.value == "name") {
            documents.sort((a, b) => {
                return a.name.localeCompare(b.name)
            })
        }

        if (DOCUMENT_ORDER_FILTER.value == "date") {
            documents.sort((a, b) => {
                return new Date(b.created_at) - new Date(a.created_at);
            })
        }
    }
    return documents
})

const addDocumentTypeFilter = (value) => {
    if (DOCUMENT_TYPE_FILTER.value.indexOf(value[0]) === -1 && value[0]) {
        DOCUMENT_TYPE_FILTER.value.push(value[0])
    }
    else {
        DOCUMENT_TYPE_FILTER.value.splice(value[0], 1)
    }
}

const onDocumentRightClick = (event, documentSlug) => {
    if (activeDocumentSlug.value != documentSlug) {
        activeDocumentSlug.value = documentSlug
        store.dispatch("doctorDocuments/fetchActiveDocument", { slug: slug.value, documentSlug: activeDocumentSlug.value })
    }
    contextMenu.value.show(event);
};
const deleteDocument = async () => {
    const data = {
        creator_slug: slug.value,
        document_slug: activeDocumentSlug.value
    }
    console.log(data)
    await documentService.deleteDocument(data)
        .then(response => {
            store.commit("doctorDocuments/deleteDocument", response.data.deleted_document_slug)
        })
        .catch(error => console.log(error))
}
const addDocumentRedicrect = () => {
    router.push(`/doctor/add/document/`)
}
const showDocumentRedirect = (documentSlug) => {
    store.dispatch("doctorDocuments/fetchActiveDocument", { slug: slug.value, documentSlug: documentSlug }).then(
        () => router.push(`/doctor/document/`)
    )
}
onMounted(() => {
    store.dispatch("doctorDocuments/fetchDocuments", slug.value)
    store.dispatch("doctorDocuments/fetchDocumentsTypes")
    store.commit("doctorDocuments/clearActiveDocument")

})
</script>
<template>
    <HeaderLayout>
        <DoctorTabMenu />
    </HeaderLayout>
    <main class="flex gap-4">
        <aside class="sidebar-shadow h-screen w-1/6">
            <section class="p-4 border-b-1 border-b-black">
                <p class="font">Тип документа</p>
                <div v-for="(documentType, index) in documentsTypes" :key="index">
                    <PrimaryCheckBox :slug="documentType.slug" :name="documentType.name" @filter="addDocumentTypeFilter" />
                </div>
            </section>
            <section>
                <div class="p-2">
                    <p class="text-sm">Название документа</p>

                    <Field name="name" type='text' class="base" v-model="DOCUMENT_NAME_FILTER" />
                </div>
                <div class="p-2">
                    <div class="flex flex-col">
                        <p class="text-sm">Дата создания</p>
                        <Field type='date' class="base" name="created_date" v-model="DOCUMENT_DATE_FILTER" />
                    </div>
                </div>
                <div class="p-2 flex gap-2 justify-between">
                    <p class="text-sm">Сортировать по дате</p>
                    <RadioButton v-model="DOCUMENT_ORDER_FILTER" name="name_order" value="name" />
                </div>
                <div class="p-2 flex gap-2 justify-between">
                    <p class="text-sm">Сортировать по алфавиту</p>
                    <RadioButton v-model="DOCUMENT_ORDER_FILTER" name="date_order" value="date" />
                </div>
                <div class="p-2">
                    <button @click="addDocumentRedicrect" class="add-document-button">Добавить документ</button>
                </div>
            </section>
        </aside>
        <section class="w-full">
            <section v-if="filterDocuments.length" class="media-grid__section p-4 ">
                <div v-for="(document, index) in filterDocuments" :key="index"
                    @contextmenu="onDocumentRightClick($event, document.slug)" @click="showDocumentRedirect(document.slug)">
                    <div class="shadow-container border-container flex">
                        <div class="flex p-4">
                            <font-awesome-icon :icon="['fas', 'file-medical']" size="3x" style="color: #265fba;" />
                        </div>
                        <div class="flex flex-col p-1 w-full justify-around">
                            <div class="flex-col w-full">
                                <div class="flex justify-between">
                                    <p>{{ document.document_type.name }}</p>
                                    <p class="pr-1">
                                        {{ document.parsed_date.day +
                                            ' ' + document.parsed_date.mounth +
                                            ' ' + document.parsed_date.year
                                        }}
                                    </p>
                                </div>
                                <p class="text-sm">{{ document.name }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                <ContextMenu ref="contextMenu" :model="contextMenuOptions" />
            </section>
            <section v-else class="flex justify-center items-center h-full">
                <div class="flex gap-2">
                    <p class="text-3xl text-slate-400">Документов пока нет.</p>
                    <a class="create-document__link text-3xl text-slate-400" @click="addDocumentRedicrect">Создать ?</a>
                </div>
            </section>
        </section>
    </main>
</template>
<style lang="css" scoped>
.font {
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
}

.sidebar-shadow {
    box-shadow: 4px 0px 5px -5px rgba(34, 60, 80, 0.54);
}

.border-container {
    border: 1px solid rgb(185, 185, 185);
    border-radius: 5px;
}

.shadow-container {
    box-shadow: 8px 5px 20px 1px rgba(130, 138, 144, 0.12);
}

.media-grid__section {
    display: grid;
    gap: 1em;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    width: 100%;
}

.base {
    padding: 0.5rem;
    border: 1px solid #D1D5DB;
    border-radius: 0.75rem;
    font-size: 1rem;
    line-height: 1.5rem;
    margin-bottom: 0.25rem;
    appearance: none;
    margin: 0;
    width: 100%;
}

.base:focus {
    outline: none;
    border: 1px solid #93C5FD;
    box-shadow: rgba(23, 0, 0, 0.5) 3px;
}

@media screen and (max-width:1190px) {
    .media-grid__section {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media screen and (max-width:920px) {
    .media-grid__section {
        grid-template-columns: repeat(1, minmax(0, 1fr));
    }
}

.create-document__link {
    cursor: pointer;
    position: relative;
}

.create-document__link:visited {
    color: rgb(148 163 184);
}

.create-document__link:hover {
    transition: 0.2s;
    color: rgba(19, 48, 94, 1);
}

.add-document-button {
    appearance: none;
    background-color: #38cf63;
    border: 1px solid rgba(27, 31, 35, .15);
    border-radius: 6px;
    box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 14px;
    font-weight: 600;
    line-height: 20px;
    padding: 6px 16px;
    position: relative;
    text-align: center;
    text-decoration: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
    white-space: nowrap;
}

.add-document-button:focus:not(:focus-visible):not(.focus-visible) {
    box-shadow: none;
    outline: none;
}

.add-document-button:hover {
    background-color: #2c974b;
}

.add-document-button:focus {
    box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
    outline: none;
}

.add-document-button:disabled {
    background-color: #94d3a2;
    border-color: rgba(27, 31, 35, .1);
    color: rgba(255, 255, 255, .8);
    cursor: default;
}

.add-document-button:active {
    background-color: #298e46;
    box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;
}
</style>