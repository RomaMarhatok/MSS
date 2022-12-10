<script setup>
import documentsPageHeader from '@/components/headers/documentsPageHeader.vue';
import documentsListSection from '@/components/sections/documentPage/documentsListSection.vue';
</script>
<template>
    <documentsPageHeader />
    <main class="flex justify-center flex-row gap-3 p-5">
        <documentsListSection />
        <section></section>
    </main>
</template>