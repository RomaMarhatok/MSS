<script setup>
import { defineProps } from 'vue';
const props = defineProps({
    labelText: String,
    inputPlaceholder: String,
    inputType: String,
    labelFor: String,
});
</script>
<template>
    <div class="container">
        <label class="container__label" :for="props.labelFor">{{ props.labelText }}</label>
        <input :id="props.labelFor" class="container__input" :type="props.inputType"
            :placeholder="props.inputPlaceholder" @input="$emit('update:text', $event.target.value)">
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
</style>