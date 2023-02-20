<script setup>
import { defineProps, computed, ref } from 'vue';
import { useStore } from 'vuex'
import getBaseApi from '@/apis/baseApi';
import baseLink from '@/components/common/Links/Base/BaseLink.vue';
import AppointmentForm from '@/components/ui/Forms/AppointmentForm.vue';
const store = useStore()
const props = defineProps({
    fullName: String,
    image: String
})
const show = ref(false)
const getImageSrc = computed(() => {
    return getBaseApi.getUri() + props.image
})
function showAppintmentForm() {
    show.value = !show.value
    store.dispatch('response/resetErrors')
}
</script>
<template>
    <section class="personal-image">
        <img class="img" :src="getImageSrc">
        <div class="content">
            <p>{{ fullName }}</p>
        </div>
        <div class="flex flex-col gap-4">

            <button class="btn w-full border-1 border-black p-1" @click="showAppintmentForm">create appointment</button>
            <baseLink class="w-full" :href="'#/doctors/'" :text="'back'" />
        </div>
    </section>
    <transition name="slide-fade">
        <div class="m-4" v-if="show">
            <AppointmentForm></AppointmentForm>
        </div>
    </transition>
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

.btn:hover {
    transition: 300ms;
    border-radius: 10px;
    background-color: rgba(19, 48, 94, 1);
    color: white;
}

.slide-fade-enter-active {
    transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
    transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
    transform: translateY(-20px);
    opacity: 0;
}
</style>
