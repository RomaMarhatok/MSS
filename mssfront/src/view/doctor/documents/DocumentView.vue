<script setup>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'
import { ref, computed } from 'vue';
import ContextMenu from 'primevue/contextmenu';
import baseLink from '@/components/common/Links/Base/BaseLink.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import DoctorTabMenu from '@/components/ui/Menu/DoctorTabMenu.vue'
import ChangeDocumentForm from '@/components/ui/Forms/documentForms/ChangeDocumentForm.vue';
const store = useStore()
const router = useRouter()
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
    // {
    //     label: 'Delete',
    //     icon: 'pi pi-fw pi-trash',
    //     command: () => {
    //         console.log("DELETE")
    //     }
    // }
]);
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
                        <div class="header-container">
                            <p>{{ document.document_type.name }}</p>
                            <p>{{ document.name }}</p>
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
                <baseLink :text="'Back'" :href="redirectHref" />
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