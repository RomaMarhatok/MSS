<script setup>
import { defineProps, computed } from 'vue';
import getBaseApi from '@/apis/baseApi';
import baseLink from '@/components/common/Links/Base/BaseLink.vue';
const props = defineProps({
    fullName: String,
    image: String
})

const getImageSrc = computed(() => {
    return getBaseApi.getUri() + props.image
})
</script>
<template>
    <section class="personal-image">
        <img class="img" :src="getImageSrc">
        <div class="content">
            <p>{{ fullName }}</p>
        </div>
        <baseLink class="w-full" :href="'#/doctors/'" :text="'back'" />
    </section>
</template>
<style scoped>
.personal-image {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    padding: 1rem;
    border-radius: 1rem;
    box-shadow: 1px 0px 8px 0px rgba(34, 60, 80, 0.2);
}

.content {
    word-break: break-all;
}

.img {
    width: 100%;
    height: auto;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

@media screen and (max-width: 1100px) {
    .personal-image {
        width: 70%;
    }
}
</style>
