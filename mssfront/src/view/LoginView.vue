<script setup>
import "primeflex/primeflex.css";
// libraries
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { onBeforeMount } from "vue";
//services
import AuthenticationService from "@/../services/AuthenticationService";
// components
import LoginAsAdminLink from '@/components/common/Links/LoginAsAdminLink.vue';
import ChangePasswordLink from "@/components/common/Links/ChangePasswordLink.vue";
import AuthenticationFrom from '@/components/ui/Forms/authentication/AuthenticationForm.vue'
import Divider from 'primevue/divider'

import ROLES from "@/../roles/roles"

// stores
const store = useStore()

// router
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
            if (response.data.role == ROLES.Patient) {
                router.push("/home/")
            }
            if (response.data.role == ROLES.Doctor) {
                router.push("/doctor/")
            }
        }
    }).catch(errors => {
        console.log(errors)
        const errorsObj = errors.response.data
        for (const key in errorsObj) {
            store.commit("authentication/addError", errorsObj[key])
        }
    })
}
const signUpRedirect = () => router.push("/registration/")
// hooks
onBeforeMount(async () => {
    store.commit("authentication/clearErrors")
})
</script>
<template>
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <section class="pt-3">
            <header class="flex flex-col gap-3 mb-5">
                <div class="text-5xl font-black underline decoration-2">MSS</div>
                <div class="text-lg font-black">Log in to improve your medical experience!</div>
            </header>
        </section>
        <main class="content__wrapper">
            <div class="inner__wrapper">
                <AuthenticationFrom @SubmitLoginFrom="submit"></AuthenticationFrom>
                <footer>
                    <ChangePasswordLink />
                    <LoginAsAdminLink />
                </footer>
            </div>
            <Divider layout="vertical" class="hidden md:flex"><b>ИЛИ</b></Divider>
            <Divider layout="horizontal" class="flex sm:hidden" align="center"><b>ИЛИ</b></Divider>
            <div class="inner__wrapper">
                <button class="button__sign_up" @click="signUpRedirect">Регистрация</button>
            </div>
        </main>
    </main>
</template>
<style lang="css" scoped>
.content__wrapper {
    display: flex;
    width: 100%;
    justify-content: space-evenly;
}

.inner__wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
}

.button__sign_up {
    appearance: none;
    background-color: #2ea44f;
    border: 1px solid rgba(27, 31, 35, .15);
    border-radius: 6px;
    box-shadow: rgba(27, 31, 35, .1) 0 1px 0;
    box-sizing: border-box;
    color: #fff;
    cursor: pointer;
    display: inline-block;
    font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
    font-size: 1em;
    font-weight: 600;
    line-height: 20px;
    padding: 6px 16px;
    position: relative;
    text-align: center;
    text-decoration: none;
    user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
    white-space: nowrap;
}

.button__sign_up:focus:not(:focus-visible):not(.focus-visible) {
    box-shadow: none;
    outline: none;
}

.button__sign_up:hover {
    background-color: #2c974b;
}

.button__sign_up:focus {
    box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;
    outline: none;
}



@media screen and (max-width:650px) {
    .content__wrapper {
        flex-direction: column;
    }
}
</style>
