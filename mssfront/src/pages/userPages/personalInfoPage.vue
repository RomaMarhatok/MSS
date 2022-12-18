<script setup>
import dataSection from '@/components/sections/userPages/personalInfoPage/dataSection.vue';
import imageSection from '@/components/sections/userPages/personalInfoPage/imageSection.vue';
import { reactive } from 'vue';
const personalInfoSection = reactive({
    header: "personal info",
    data: [
        {
            label: "Email",
            text: "maldonadoandrea@example.net"
        },
        {
            label: "Age",
            text: 26
        },
        {
            label: "Gender",
            text: "Male"
        },
        {
            label: "Health status",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        }
    ]
})
const recentDocuments = reactive({
    header: "recent documents",
    data: [
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
    ]
})
const recentAppoitments = reactive({
    header: "recent appoitments",
    data: [
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
        {
            label: "Age",
            text: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa sit ea molestias qui quae odit reprehenderit animi id, corporis tempora facilis debitis, cum placeat. Velit quo inventore maiores eius consectetur!"
        },
    ]
})
const imageSectionProps = reactive({
    imageSrc: "https://picsum.photos/262/187",
    links: {
        doctors: "#/",
        appoitments: "#/",
        documents: "#/",
    },
    personalInfo: {
        full_name: "First Name Second name patronymic",
        location: "location"
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
            <dataSection v-if="recentDocuments.data" :headerText="recentDocuments.header"
                :data="recentDocuments.data" />
            <dataSection v-if="recentAppoitments.data" :headerText="recentAppoitments.header"
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