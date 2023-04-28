<script setup>
import { useStore } from 'vuex';
import { ref, computed } from 'vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import BodyLayout from '@/components/layout/BodyLayout.vue';
import TabMenu from '@/components/ui/Menu/TabMenu.vue'
const store = useStore()
const redirectHref = ref(`#/home/documents/`)
const document = computed(() => store.getters["documents/getActiveDocument"])
</script>
<template>
    <HeaderLayout>
        <TabMenu />
    </HeaderLayout>
    <BodyLayout>
        <div class="main">
            <div class="main-container">
                <div class="document-header">
                    <div class="content-container">
                        <div class="flex">
                            <div>
                                <a :href="redirectHref"><i class="pi pi-arrow-left"></i></a>
                            </div>
                            <div class="header-container">
                                <p>{{ document.document_type.name }}</p>
                                <p>{{ document.name }}</p>
                            </div>
                        </div>

                        <p>Cоздатель {{ document.creator.full_name }}</p>
                        <p>Создано
                            {{ document.parsed_date.day +
                                " " + document.parsed_date.mounth +
                                " " + document.parsed_date.year
                            }} в {{ document.parsed_date.hours + ":" + document.parsed_date.minutes }}</p>
                    </div>
                </div>
                <div class="main">
                    <p>{{ document.content }}</p>
                </div>
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