<script setup>
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router'
import { ref, computed } from 'vue';
import DocumentService from '@/../services/DocumentService';
import ContextMenu from 'primevue/contextmenu';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import DoctorTabMenu from '@/components/ui/Menu/DoctorTabMenu.vue'
import ChangeDocumentForm from '@/components/ui/Forms/documentForms/ChangeDocumentForm.vue';
const store = useStore()
const router = useRouter()
const route = useRoute()
const documentService = new DocumentService()
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)
const redirectHref = ref(`#/doctor/documents/`)
const document = computed(() => store.getters["doctorDocuments/getActiveDocument"])
const contextMenu = ref()
const swapOnChangeForm = ref(false)
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
const deleteDocument = async () => {
    const data = {
        creator_slug: slug.value,
        document_slug: document.value.slug
    }
    await documentService.deleteDocument(data)
        .then(response => {
            store.commit("doctorDocuments/deleteDocument", response.data.deleted_document_slug)
        })
        .catch(error => console.log(error))
    router.push("/doctor/documents/")
}
const onDocumentRightClick = (event) => {
    contextMenu.value.show(event);
};
</script>
<template>
    <HeaderLayout>
        <DoctorTabMenu />
    </HeaderLayout>
    <main @contextmenu="onDocumentRightClick">
        <div v-if="!swapOnChangeForm" class="main">
            <div class="main-container">
                <div class="document-header">
                    <div class="content-container">
                        <div class="flex">
                            <div>
                                <a :href="redirectHref"><i class="pi pi-arrow-left"></i></a>
                            </div>
                            <div class="header-container">
                                <p>{{ document.document_type.name }}</p>
                                <p>{{ document.name }}</p>
                            </div>
                        </div>
                        <p>Создано
                            {{ document.parsed_date.day +
                                " " + document.parsed_date.mounth +
                                " " + document.parsed_date.year
                            }} в {{ document.parsed_date.hours + ":" + document.parsed_date.minutes }}</p>
                    </div>
                </div>
                <div class="main">
                    <p>{{ document.content }}</p>
                </div>
            </div>
        </div>
        <div v-else>
            <ChangeDocumentForm :document="document" />
        </div>
        <ContextMenu ref="contextMenu" :model="contextMenuOptions" />
    </main>
</template>
<style scoped>
.main {
    display: flex;
    justify-content: center;
    padding: 2rem;
}

.main-container {
    display: flex;
    flex-direction: column;
    box-shadow: 0px 0px 8px 0px rgba(34, 60, 80, 0.2);
    background-color: white;
    margin-top: 10px;
    margin-bottom: 10px;
    width: 80%;
}

.document-header {
    border-radius: 10px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    word-break: break-all;
    padding-top: 1rem;
}

.content-container {
    display: flex;
    flex-direction: column;
    padding-left: 20px;
    width: 100%;

}

.header-container {
    display: flex;
    width: 100%;
    justify-content: center;
    gap: 1rem;
}
</style>