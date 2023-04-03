<script setup>
//vue
import { computed, ref, onBeforeMount } from 'vue';
import { useStore } from 'vuex'
//layouts
import PageHeader from '@/components/ui/Headers/PageHeader.vue'
import BodyLayout from '@/components/layout/BodyLayout.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
//primevue
import Panel from 'primevue/panel'
import Timeline from 'primevue/timeline'
import Card from 'primevue/card';
import DataTable from 'primevue/datatable'
import Column from 'primevue/column';
import SelectButton from 'primevue/selectbutton'
import ScrollPanel from 'primevue/scrollpanel';
import ScrollTop from 'primevue/scrolltop';
import Menu from 'primevue/menu';
import Avatar from 'primevue/avatar'
//primevue styles
import "primevue/resources/themes/saga-blue/theme.css"
import "primevue/resources/primevue.min.css"
//before init
onBeforeMount(() => {
    store.dispatch("treatments/fetchTreatments",
        {
            patientSlug: store.state.appointment.selectedAppointment.patient.user.slug,
            doctorSpecializationSlug: store.state.appointment.selectedAppointment.doctor_specialization.slug
        }
    )
})

//init
const store = useStore()
const treatmentHistories = computed(() => {
    return store.getters["treatments/getTreatmentsHistories"]
})
const patientInfo = computed(() => {
    return store.getters["treatments/getPatientInfo"]
})
const selectButtonValue = ref('list')
const selectButtonValues = ref(['list', 'timeline'])
const items = ref([
    {
        label: 'Actions',
        items: [
            {
                label: 'Update',
                icon: 'pi pi-refresh',
                command: () => {
                    console.log("Update")

                }
            },
            {
                label: 'Delete',
                icon: 'pi pi-times',
                command: () => {
                    console.log("Delete")
                }
            },
            {
                label: 'Add',
                icon: 'pi pi-times',
                command: () => {
                    console.log("Delete")
                }
            }
        ]
    },
])
const menu = ref()
const toggle = (event) => {
    menu.value.toggle(event);
};
</script>
<template>
    <HeaderLayout>
        <PageHeader />
    </HeaderLayout>
    <BodyLayout :class="'flex w-full p-6 flex-row justify-center'">
        <main class="flex w-full p-6 flex-col">
            <section v-if="selectButtonValue == 'timeline'">
                <p>Treatment histories</p>
                <ScrollPanel class="w-full m-3 border-y-3 pt-2 scroll-panel">
                    <SelectButton v-model="selectButtonValue" :options="selectButtonValues" />
                    <Timeline :value="treatmentHistories" :align="'alternate'">
                        <template #opposite="slotProps">
                            <small class="p-text-secondary">{{ slotProps.item.created_at }}</small>
                        </template>
                        <template #content="slotProps">
                            <Card>
                                <template #title>
                                    <p class="font-bold text-base text-left">
                                        {{ slotProps.item.title }}
                                    </p>
                                </template>
                                <template #content>
                                    <p class="text-left">
                                        {{ slotProps.item.short_description }}
                                    </p>
                                </template>
                            </Card>
                        </template>
                    </Timeline>
                    <ScrollTop target="parent" :threshold="100" class="custom-scroll-top" icon="pi pi-arrow-up" />
                </ScrollPanel>
            </section>

            <section v-if="selectButtonValue == 'list'">
                <DataTable :value="treatmentHistories" :rows="10" :paginator="true">
                    <template #empty>
                        No treatment histories found found.
                    </template>
                    <template #loading>
                        Loading patient data. Please wait.
                    </template>
                    <Column>
                        <template #header>
                            <div class="flex flex-row justify-between w-full items-center">
                                <p>Treatment histories</p>
                                <SelectButton v-model="selectButtonValue" :options="selectButtonValues" />
                            </div>

                        </template>
                        <template #body="{ data }">
                            <Panel toggleable>
                                <template #header>
                                    <div class="flex items-center gap-3">
                                        <Avatar :image=patientInfo.image shape="circle" />
                                        <div class="flex flex-col">
                                            <p>{{ data.date }}</p>
                                            <p>{{ data.title }}</p>
                                        </div>
                                    </div>
                                </template>
                                <template #icons>
                                    <button class="p-panel-header-icon p-link mr-2" @click="toggle">
                                        <span class="pi pi-cog"></span>
                                    </button>
                                    <Menu ref="menu" id="config_menu" :model="items" popup />
                                </template>
                                <Card>
                                    <template #content>
                                        <p class="text-left">
                                            {{ data.short_description }}
                                        </p>
                                    </template>
                                </Card>
                            </Panel>
                        </template>
                    </Column>
                </DataTable>
            </section>
        </main>
    </BodyLayout>
</template>
<style lang="css">
.p-scrollpanel .p-scrollpanel-bar {
    background-color: #3B82F6;
    opacity: 1;
    transition: background-color .2s;


}

.p-scrollpanel-bar:hover {
    background-color: #007ad9;
}

.scroll-panel {
    height: 550px;
    max-height: 550px;
}

.p-scrolltop.p-link {
    background-color: #3B82F6;

}

.p-scrolltop.p-link:hover {
    background-color: #007ad9;

}
</style>