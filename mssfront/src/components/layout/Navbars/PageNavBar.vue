<script setup>
import { useStore } from 'vuex'
import { useRoute } from 'vue-router';
import { reactive, defineProps, computed } from 'vue'
import documentPageLink from '@/components/common/Links/DocumentPageLink.vue';
const route = useRoute()
const store = useStore()
const props = defineProps({
    activeLinks: {
        type: Array,
        default: () => [false, false, false]
    },
})
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)
const documentLink = reactive({
    link: `#/user/${slug.value}/documents/`,
    text: "Documents",
    active: props.activeLinks[0],
})
const appoitmentsLink = reactive({
    link: "#/",
    text: "Appoitments",
    active: props.activeLinks[1],

})
const doctorLink = reactive({
    link: "#/doctors/",
    text: "Doctors",
    active: props.activeLinks[2],

})
</script>
<template>
    <nav class="flex flex-row justify-evenly mt-3">
        <documentPageLink :href="documentLink.link" :text=documentLink.text :active="documentLink.active" />
        <documentPageLink :href="appoitmentsLink.link" :text="appoitmentsLink.text" :active="appoitmentsLink.active" />
        <documentPageLink :href="doctorLink.link" :text="doctorLink.text" :active="doctorLink.active" />
    </nav>
</template>