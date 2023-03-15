<script setup>
import HeaderLayout from '@/components/layout/HeaderLayout.vue'
import BodyLayout from '@/components/layout/BodyLayout.vue';
import PageHeader from '@/components/ui/Headers/PageHeader.vue';
import DataView from 'primevue/dataview'
import AccardionLayout from '@/components/layout/AccardionLayout.vue';
import Panel from 'primevue/panel'
import Button from 'primevue/button'
import { onBeforeMount, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
const store = useStore()
const router = useRouter()
const appointments = computed(() => store.getters["doctorAppointments/getAppointments"])
const onclick = (appointment) => {
    store.commit("appointment/setSelectedAppointment", appointment)
    router.push("/appointment/")
}
onBeforeMount(() => {
    store.dispatch("doctorAppointments/fetchAppointments", store.state.user.slug)
})

</script>
<template>
    <HeaderLayout>
        <PageHeader></PageHeader>
    </HeaderLayout>
    <BodyLayout>
        <DataView :value="appointments" :paginator="true" :rows="10" :layout="'list'">
            <template #list="slotProps">
                <AccardionLayout>
                    <template #header>
                        <div class="accordion-tab-header">
                            <p class="pt-2">Patient {{ slotProps.data.patient.user.full_name }}</p>
                        </div>
                    </template>
                    <Panel header="Persnal info" :toggleable="true">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                            tempor
                            incididunt ut labore et dolore magna aliqua.
                            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
                            aliquip
                            ex ea commodo consequat.
                            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
                            eu
                            fugiat nulla pariatur. Excepteur sint occaecat
                            cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
                            est
                            laborum.</p>
                    </Panel>
                    <Button label="Open appointment" class="p-button-text w-fit font-medium m-4"
                        @click="onclick(slotProps.data)"></Button>
                </AccardionLayout>
            </template>
        </DataView>
    </BodyLayout>
</template>
<style lang="css" scoped>
.accordion-tab-header {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: space-between;
}

@media screen and (max-width: 460px) {
    .accordion-tab-header {
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }

}
</style>