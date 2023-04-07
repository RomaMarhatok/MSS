<script setup>
// libraries
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { onBeforeMount } from "vue";
//services
import AuthenticationService from "@/../services/AuthenticationService";
// components
import BodyLayout from '@/components/layout/BodyLayout.vue';
import HeaderLayout from '@/components/layout/HeaderLayout.vue';
import FooterLayout from '@/components/layout/FooterLayout.vue';
import LoginAsAdminLink from '@/components/common/Links/LoginAsAdminLink.vue';
import AuthenticationFrom from '@/components/ui/Forms/authentication/AuthenticationForm.vue'
// //stores
const store = useStore()

// // router
const router = useRouter()

// services
const authenticationService = new AuthenticationService()


// methods
const submit = async (data) => {
    console.log(data)
    authenticationService.authenticate(data).then(response => {
        if (response.status == 200) {
            store.commit("user/setRole", response.data.role)
            store.commit("user/setSlug", response.data.slug)
            router.push("/home/")
        }
    }).catch(errors => {
        const errorsObj = errors.response.data
        for (const key in errorsObj) {
            store.commit("authentication/addError", errorsObj[key][0])
        }

        // store.commit("authentication/addError", errors.response.data.description)
    })
}

// hooks
onBeforeMount(() => {
    store.commit("authentication/clearErrors")
})
</script>
<template>
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <HeaderLayout :class="'pt-3'">
            <header class="flex flex-col gap-3 mb-5">
                <div class="text-5xl font-black underline decoration-2">MSS</div>
                <div class="text-lg font-black">Log in to improve your medical experience!</div>
            </header>
        </HeaderLayout>
        <BodyLayout :class="'w-4/5'">
            <AuthenticationFrom @SubmitLoginFrom="submit"></AuthenticationFrom>
        </BodyLayout>
        <FooterLayout>
            <LoginAsAdminLink />
        </FooterLayout>
    </main>
</template>