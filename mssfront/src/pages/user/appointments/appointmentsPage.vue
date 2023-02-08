<script setup>
import { onBeforeMount, computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';
import appointemntsListSection from '@/components/ui/Sections/UserPages/AppointmentsPage/ListSection.vue';
const store = useStore()
const route = useRoute()
const slug = computed(() => store.state.user.slug ? store.state.user.slug : route.params.userSlug)

console.log(store)
onBeforeMount(() => {
    store.dispatch("user/fetchAppointments", slug.value)
})
</script>
<template>
    <appointemntsListSection></appointemntsListSection>
</template>