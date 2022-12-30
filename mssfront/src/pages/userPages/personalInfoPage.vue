<script setup>
import { reactive, onBeforeMount, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useStore } from 'vuex'
import imageSection from '@/components/sections/userPages/personalInfoPage/imageSection.vue';
import dataSection from '@/components/sections/userPages/personalInfoPage/base/dataSection.vue';
import healthInfoSection from '@/components/sections/userPages/personalInfoPage/healthInfoSection.vue';
const store = useStore()
const route = useRoute()
console.log(store)
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)
onBeforeMount(() => {
    console.log("on mounted")
    store.dispatch("user/fetchUserPersonalInfo", slug.value)
})

const recentDocuments = reactive({
    header: "recent documents",
    data: []
})
const recentAppoitments = reactive({
    header: "recent appoitments",
    data: []
})
</script>
<template>
    <main>
        <section class="flex__section">
            <healthInfoSection />
            <imageSection />
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