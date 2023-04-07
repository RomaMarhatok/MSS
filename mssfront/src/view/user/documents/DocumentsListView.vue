<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { onMounted, computed, ref } from 'vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue';
import Column from 'primevue/column'
import DataTable from 'primevue/datatable'
import InputText from 'primevue/inputtext'
import { FilterMatchMode } from 'primevue/api'
import BodyLayout from '@/components/layout/BodyLayout.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import PageHeader from '@/components/ui/Headers/PageHeader.vue';
const store = useStore()
const route = useRoute()
const router = useRouter()
const selected = ref()
const filter = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'name': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'document_type.name': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'created_at': { value: null, matchMode: FilterMatchMode.CONTAINS },
})

const documents = computed(() => store.state.documents.documents)
const slug = computed(() => route.params.userSlug ? route.params.userSlug : store.state.user.slug)

const redirect = (document_slug) => {
    store.dispatch("documents/fetchDocument", {
        slug: slug.value,
        document_slug: document_slug
    })
    router.push(`/home/document/${document_slug}/`)
}

onMounted(() => {
    store.dispatch("documents/fetchDocuments", slug.value)
    store.dispatch("documents/fetchDocumentsTypes")
})
</script>
<template>
    <HeaderLayout>
        <PageHeader />
        <TabMenu />
    </HeaderLayout>
    <BodyLayout :class="'flex justify-center flex-col mt-8 items-center'">
        <DataTable class="w-full" @row-click="redirect($event.data.slug)" :value="documents" :paginator="true" :rows="10"
            v-model:filters="filter" v-model:selection="selected" data-key="slug" filter-display="row"
            :global-filter-fields="['name', 'document_type.name', 'created_at']" removableSort sortMode="multiple"
            responsive-layout="scroll" showGridlines>
            <template #header>
                <span class="p-input-icon-left">
                    <i class="pi pi-search"></i>
                    <InputText v-model="filter['global'].value" placeholder="Search"></InputText>
                </span>
            </template>
            <template #empty>
                No documents found
            </template>
            <template #loading>
                Loading documents data. Please wait.
            </template>
            <Column field="name" header="Name" :sortable="true">
                <template #body="{ data }">
                    {{ data.name }}
                </template>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search by name"
                        v-tooltip.top.focus="'Hit enter key to filter'" />
                </template>
            </Column>
            <Column field="document_type.name" header="Document Type" :sortable="true">
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search by document type"
                        v-tooltip.top.focus="'Hit enter key to filter'" />
                </template>
            </Column>
            <Column field="created_at" header="Created at">
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search by date"
                        v-tooltip.top.focus="'Hit enter key to filter'" />
                </template>
            </Column>
        </DataTable>
    </BodyLayout>
</template>