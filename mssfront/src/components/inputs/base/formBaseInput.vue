<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    labelText: String,
    inputPlaceholder: String,
    inputType: String,
    labelFor: String,
    errors: Object,
})
</script>
<template>
    <div class="container">
        <label class="container__label" :for="props.labelFor">{{ props.labelText }}</label>
        <ul v-if="props.errors" class="form__ul">
            <li v-for="(error, index) in props.errors" :key="index">{{ error }}</li>
        </ul>
        <input :id="props.labelFor" class="container__input" :type="props.inputType"
            :placeholder="props.inputPlaceholder">
    </div>
</template>
<style scoped>
.container {
    display: flex;
    flex-direction: column;
    gap: 5px
}

.container__label {
    font-weight: bolder;
    font-size: 1.1em;
}


.container__input {
    margin-top: 5px;
    font-family: 'Fira Sans';
    margin-bottom: 20px;
    background: #FFFFFF;
    border: 2px solid rgba(209, 209, 209, 1);
    border-radius: 10px;
    padding: 10px;
    font-size: 1em;
}

.form__ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.form__ul>li {
    border-radius: 10px;
    padding: 5px;
    color: rgb(114, 75, 75);
    background-color: pink;
    margin-bottom: 5px;
}
</style>