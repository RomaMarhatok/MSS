<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    imageSrc: String,
    links: Object,
    personalInfo: Object
})
</script>
<template>
    <section class="personal-image">
        <img class="img" :src="props.imageSrc" />
        <div class="content">
            <p>{{ props.personalInfo.full_name }}</p>
            <p>{{ props.personalInfo.location }}</p>
            <p class="whitespace-pre text-center">{{ props.personalInfo.address }}</p>
            <section class="href__section">
                <a :href="props.links.doctors">Doctors</a>
                <a :href="props.links.appoitments">Appoitments</a>
                <a :href="props.links.documents">Documents</a>
            </section>
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

.href__section {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 10px;
    color: black;
}

.href__section>a {
    text-transform: uppercase;
    text-decoration: none;
    letter-spacing: 0.15em;
    color: inherit;
}

.href__section>a:hover {
    transition: 100ms;
    text-decoration: underline;
    text-decoration-thickness: 1px;

}

@media screen and (max-width: 600px) {
    .href__section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
        color: black;
    }

}
</style>