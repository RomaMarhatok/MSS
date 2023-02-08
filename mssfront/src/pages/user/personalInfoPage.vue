<script setup>
import { useStore } from 'vuex'
import { useRoute } from 'vue-router';
import { reactive, onBeforeMount, computed } from 'vue';
import imageSection from '@/components/ui/Sections/UserPages/PersonalInfoPage/ImageSection.vue'
import dataSection from '@/components/ui/Sections/UserPages/PersonalInfoPage/Base/DataSection.vue';
import healthInfoSection from '@/components/ui/Sections/UserPages/PersonalInfoPage/HealthInfoSection.vue';
const store = useStore()
const route = useRoute()
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)
onBeforeMount(() => {
    console.log("on mounted")
    store.dispatch("user/fetchUserPersonalInfo", slug.value)
})

const recentDocuments = reactive({
    header: "recent documents",
    data: [],
})
const recentAppoitments = reactive({
    header: "recent appoitments",
    data: [],
})
const imageSectionProps = reactive({
    links: {
        doctors: "#/doctors/",
        appoitments: `#/user/${slug.value}/appointments/`,
        documents: `#/user/${slug.value}/documents/`,
    },
})
</script>
<template>
    <main>
        <section class="flex__section">
            <healthInfoSection />
            <imageSection :links="imageSectionProps.links" />
        </section>
        <section class="flex__section">
            <dataSection v-if="recentDocuments.data.length" :headerText="recentDocuments.header"
                :data="recentDocuments.data" />
            <dataSection v-if="recentAppoitments.data.length" :headerText="recentAppoitments.header"
                :data="recentAppoitments.data" />
        </section>
    </main>
</template>
<style scoped>
.flex__section {
    display: flex;
    flex-direction: row;
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
</style>