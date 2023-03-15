<script setup>
import { useStore } from 'vuex'
import { useRoute } from 'vue-router';
import { onBeforeMount, computed } from 'vue';
import Image from 'primevue/image';
import TabMenu from '@/components/ui/Menu/TabMenu.vue';
import DataSection from '@/components/layout/DataTableLayout.vue';
import PageHeader from '@/components/ui/Headers/PageHeader.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import BodyLayout from '@/components/layout/BodyLayout.vue';
const store = useStore()
const route = useRoute()

const personalInfo = computed(() => store.getters["user/getPersonalInfo"])
const healthInfo = computed(() => store.getters["user/getHealthInfo"])
const appointments = computed(() => store.getters["appointments/getAllAppointmentsForCalendar"])
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)

onBeforeMount(() => {
    console.log("on mounted")
    store.dispatch("user/fetchUserPersonalInfo", slug.value)
    store.dispatch("appointments/fetchAppointments", slug.value)
})
</script>
<template>
    <HeaderLayout>
        <PageHeader />
        <TabMenu />
    </HeaderLayout>
    <BodyLayout>
        <main>
            <section class="flex__section flex-row">
                <section class="personal-image">
                    <div class="img">
                        <Image :src="personalInfo.image" />
                    </div>
                    <div class="content">
                        <p>Email: {{ personalInfo.email }}</p>
                        <p>{{ personalInfo.full_name }}</p>
                        <p>{{ personalInfo.location }}</p>
                        <p class="whitespace-pre text-center">{{ personalInfo.address }}</p>
                    </div>
                </section>
                <DataSection :header-text="'Health info'" :data="healthInfo" />
            </section>
            <section class="flex__section flex-col">
                <div class="text-center section">
                    <v-calendar class="custom-calendar max-w-full" :attributes="appointments" disable-page-swipe is-expanded
                        locale="en">
                        <template v-slot:day-content="{ day, attributes }">
                            <div class="vc-day flex flex-col h-full z-10 overflow-hidden">
                                <span class="day-label text-sm text-gray-900">{{ day.day }}</span>
                                <div class="flex-grow overflow-y-auto overflow-x-auto">
                                    <button v-for="attr in attributes" :key="attr.key" onclick="alert(1)"
                                        class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1 w-full"
                                        :class="attr.customData.class">
                                        {{ attr.customData.title }}
                                    </button>
                                </div>
                            </div>
                        </template>
                    </v-calendar>
                </div>
            </section>
        </main>
    </BodyLayout>
</template>
<style scoped>
/** base */
.flex__section {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 10px;
    padding: 0px 40px 0px 40px;
}

@media screen and (max-width: 900px) {
    .flex__section {
        display: flex;
        flex-direction: column;
        gap: 30px;
        margin-top: 10px;
        padding: 0px 40px 0px 40px;
    }
}

/** base */

/** calendar */
.vc-day {
    padding: 0 5px 3px 5px;
    text-align: left;
    height: 90px;
    min-width: var(90px);
    background-color: #f8fafc;
    border: 1px solid #eaeaea;
    padding: 5px 0;
}

/**calendar */

/** personal info image section */
.personal-image {
    display: flex;
    flex-direction: column;
    padding: 5px;
    border: 1px solid rgb(218, 218, 218);
    background-color: #ffffff;
    border-radius: 5px;
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
}

.content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;
}

.content>p {
    margin-bottom: 2px;
    margin-top: 2px;
}


.img {
    width: 100%;
    height: auto;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

@media screen and (max-width: 900px) {
    .personal-image {
        flex-direction: row;
    }

    .content {
        width: 100%;
        text-align: center;
    }
}

@media screen and (max-width: 630px) {
    .personal-image {
        flex-direction: column;
    }

    .content {
        width: 100%;
        text-align: center;
    }

    .img {
        display: flex;
        justify-content: center;
    }
}

/** personal info image section */
</style>