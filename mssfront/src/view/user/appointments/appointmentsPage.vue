<script setup>
import { onBeforeMount, computed, ref } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import HeaderLayout from '@/components/layout/HeaderLayout.vue'
import BodyLayout from '@/components/layout/BodyLayout.vue'
import PageHeader from '@/components/ui/Headers/PageHeader.vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import { FilterMatchMode } from 'primevue/api'
const store = useStore()
const route = useRoute()
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)
const appointments = computed(() => store.getters["appointments/getAppointments"])
onBeforeMount(() => {
    store.dispatch("appointments/fetchAppointments", slug.value)
    store.dispatch("doctors/fetchAllDoctors")
    store.dispatch("doctors/fetchAllDoctorTypes")

})
const filter = ref({
    'global': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'label': { value: null, matchMode: FilterMatchMode.CONTAINS },
    'text': { value: null, matchMode: FilterMatchMode.CONTAINS },
})
const selected = ref()
</script>
<template>
    <HeaderLayout>
        <PageHeader />
        <TabMenu />
    </HeaderLayout>
    <BodyLayout>
        <DataTable class="w-full" :value="appointments" :paginator="true" :rows="10" v-model:filters="filter"
            v-model:selection="selected" data-key="slug" filter-display="row" :global-filter-fields="['label', 'text']"
            removableSort sortMode="multiple" responsive-layout="scroll" showGridlines>
            <template #header>
                <span class="p-input-icon-left">
                    <i class="pi pi-search"></i>
                    <InputText v-model="filter['global'].value" placeholder="Search"></InputText>
                </span>
            </template>
            <template #empty>
                No appointments found
            </template>
            <template #loading>
                Loading appointments data. Please wait.
            </template>
            <Column field="label" header="Date" :sortable="true">
                <template #body="{ data }">
                    {{ data.label }}
                </template>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search by date"
                        v-tooltip.top.focus="'Hit enter key to filter'" />
                </template>
            </Column>
            <Column field="text" header="Content" :sortable="true">
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search by content"
                        v-tooltip.top.focus="'Hit enter key to filter'" />
                </template>
            </Column>
        </DataTable>
    </BodyLayout>
</template>
<style scoped>
.appointment-list {
    padding: 1rem;
    background-color: #f8f9fa;
}

.appointment-item {
    display: flex;
    flex-direction: row;
}
</style>