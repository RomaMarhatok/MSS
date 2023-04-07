<script setup>
import { useStore } from 'vuex';
import { ref, computed } from 'vue';
import baseLink from '@/components/common/Links/Base/BaseLink.vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import PageHeader from '@/components/ui/Headers/PageHeader.vue';
import BodyLayout from '@/components/layout/BodyLayout.vue';
const store = useStore()
const redirectHref = ref(`#/home/documents/`)
const document = computed(() => store.getters["documents/getActiveDocument"])
</script>
<template>
    <HeaderLayout>
        <PageHeader />
        <TabMenu />
    </HeaderLayout>
    <BodyLayout>
        <div class="main">
            <div class="main-container">
                <div class="document-header">
                    <div class="content-container">
                        <div class="header-container">
                            <p>{{ document.document_type.name }}</p>
                            <p>{{ document.name }}</p>
                        </div>
                        <p>{{ document.creator.full_name }}</p>
                        <p>{{ document.updated_at }}</p>
                        <p>{{ document.created_at }}</p>
                    </div>
                </div>
                <div class="main">
                    <p>{{ document.content }}</p>
                </div>
                <baseLink :text="'Back'" :href="redirectHref" />
            </div>
        </div>
    </BodyLayout>
</template>
<style scoped>
.main {
    display: flex;
    justify-content: center;
    padding: 2rem;
}

.main-container {
    display: flex;
    flex-direction: column;
    box-shadow: 0px 0px 8px 0px rgba(34, 60, 80, 0.2);
    background-color: white;
    margin-top: 10px;
    margin-bottom: 10px;
    width: 80%;
}

.document-header {
    border-radius: 10px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    word-break: break-all;
    padding-top: 1rem;
}

.content-container {
    display: flex;
    flex-direction: column;
    padding-left: 20px;
    width: 100%;

}

.header-container {
    display: flex;
    width: 100%;
    justify-content: center;
    gap: 1rem;
}

.content {
    border-radius: 10px;
    padding: 20px;
    margin-top: 10px;
    text-align: justify;
}
</style>