<script setup>
import dataSection from '@/components/sections/userPages/personalInfoPage/dataSection.vue';
import imageSection from '@/components/sections/userPages/personalInfoPage/imageSection.vue';
import { reactive, onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';
import UserService from '../../../services/UserService';
import getBaseApi from '@/apis/baseApi';
const route = useRoute()
const getFullGenderName = (gender) => {
    switch (gender) {
        case "F":
            return "Female"
        case "M":
            return "Male"
        default:
            return "Other"
    }
}
onBeforeMount(() => {
    let userServive = ref(new UserService())
    userServive.value.getUserPersonalInfo(route.params.slug).then((response) => {
        personalInfoSection.data[0].text = response.data.email
        personalInfoSection.data[1].text = response.data.age
        personalInfoSection.data[2].text = getFullGenderName(response.data.gender)
        personalInfoSection.data[3].text = response.data.health_status

        imageSectionProps.personalInfo.full_name = response.data.first_name + " " + response.data.second_name + " " + response.data.patronymic
        imageSectionProps.imageSrc = getBaseApi.getUri() + response.data.image
        imageSectionProps.personalInfo.location = response.data.country + " " + response.data.city
        imageSectionProps.personalInfo.address = response.data.address
        console.log(response)
    }).catch((error) => {
        console.log(error)
    })
})

const personalInfoSection = reactive({
    header: "personal info",
    data: [
        {
            label: "Email",
            text: ""
        },
        {
            label: "Age",
            text: -1
        },
        {
            label: "Gender",
            text: ""
        },
        {
            label: "Health status",
            text: ""
        }
    ]
})
const recentDocuments = reactive({
    header: "recent documents",
    data: [
        //Example of data display
        // {
        //     label: "Age",
        //     text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        // },
    ]
})
const recentAppoitments = reactive({
    header: "recent appoitments",
    data: []
})
const imageSectionProps = reactive({
    imageSrc: "https://picsum.photos/262/187",
    links: {
        doctors: "#/",
        appoitments: "#/",
        documents: `#/user/${route.params.slug}/documents/`,
    },
    personalInfo: {
        full_name: "",
        location: "",
        address: ""
    }
})
</script>
<template>
    <main>
        <section class="flex__section">
            <dataSection :headerText="personalInfoSection.header" :data="personalInfoSection.data" />
            <imageSection :imageSrc="imageSectionProps.imageSrc" :links="imageSectionProps.links"
                :personalInfo="imageSectionProps.personalInfo" />
        </section>
        <section class="flex__section">
            <dataSection v-if="recentDocuments.data.length" :headerText="recentDocuments.header"
                :data="recentDocuments.data" />
            <dataSection v-if="recentAppoitments.data.length" :headerText="recentAppoitments.header"
                :data="recentAppoitments.data" />
        </section>
    </main>
</template>
<style scoped>
.flex__section {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 30px;
    margin-top: 10px;
    padding: 0px 40px 0px 40px;
}

@media screen and (max-width: 900px) {
    .flex__section {
        display: flex;
        flex-direction: column;
        gap: 30px;
        margin-top: 10px;
        padding: 0px 40px 0px 40px;
    }
}
</style>