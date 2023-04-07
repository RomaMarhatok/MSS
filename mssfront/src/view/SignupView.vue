<script setup>
// libraries
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { reactive, onMounted, ref } from 'vue'

// services
import RegistrationService from '@/../services/RegistrationService'

// components
import UserForm from '@/components/ui/Forms/registration/UserForm.vue';
import UserPersonalInfoForm from '@/components/ui/Forms/registration/UserPersonalInfoForm.vue';
import UserLocationForm from '@/components/ui/Forms/registration/UserLocationForm.vue';
// store
const store = useStore()

// router
const router = useRouter()

// refs
const step = ref(1)
const user = reactive({})
const userPersonalInfo = reactive({})
const userLocation = reactive({})
const registrationService = new RegistrationService()

// hooks
onMounted(() => store.commit("registration/clearErrors"))


// methods

const submitUserForm = async (data) => {
    Object.assign(user, data)
    await registrationService.validateUser(user).then(response => {
        if (response.status == 200) {
            store.commit("registration/clearErrors")
            step.value++
        }
    }).catch(error => {
        const errorsObj = error.response.data
        for (const key in errorsObj) {
            store.commit("registration/addError", errorsObj[key][0])
        }
        // store.commit("registration/addError", error.response.data.description)
    })
}
const submitUserPersonalInfoForm = async (data) => {
    Object.assign(userPersonalInfo, data)
    await registrationService.validateUserPersonalInfo(userPersonalInfo).then(response => {
        if (response.status == 200) {
            store.commit("registration/clearErrors")
            step.value++
        }
    }).catch(error => {
        console.log(error.response)
        const errorsObj = error.response.data
        for (const key in errorsObj) {
            store.commit("registration/addError", errorsObj[key][0])
        }
        store.commit("registration/addError", error.response.data.description)
    })
}

const submitUserLocationForm = async (data) => {
    Object.assign(userLocation, data)
    const requestData = {}
    Object.assign(requestData, user, userPersonalInfo, userLocation)
    await registrationService.registrate(requestData).then(response => {
        if (response.status == 200) {
            router.push("/")
        }
    })
}


</script>
<template>
    <main class="flex flex-col justify-center items-center min-h-3/4 w-full">
        <header class="flex flex-col gap-3 mb-5">
            <div class="text-5xl font-black underline decoration-2">MSS</div>
            <div class="text-lg font-black">Nice to meet you in our medical system! {{ step }}/3</div>
        </header>

        <section class="w-4/5">
            <UserForm @SubmitUserForm="submitUserForm" v-if="step == 1" />
            <UserPersonalInfoForm @SubmitUserPersonalInfoForm="submitUserPersonalInfoForm" v-if="step == 2" />
            <UserLocationForm @SubmitUserLocationForm="submitUserLocationForm" v-if="step == 3" />
        </section>
    </main>
</template>