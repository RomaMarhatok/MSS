<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex';
import Image from 'primevue/image'
const store = useStore()
const personalInfo = computed(() => store.getters["user/getPersonalInfo"])
</script>
<template>
    <section class="personal-image">
        <div class="img">
            <Image :src="'https://placehold.co/300x200/'" />
        </div>
        <div class="content">
            <p>{{ personalInfo.full_name }}</p>
            <p>{{ personalInfo.location }}</p>
            <p class="whitespace-pre text-center">{{ personalInfo.address }}</p>
        </div>
    </section>
</template>
<style scoped>
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
</style>