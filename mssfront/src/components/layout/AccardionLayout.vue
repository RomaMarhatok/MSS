<script setup>
import Accordion from 'primevue/accordion';
import AccordionTab from 'primevue/accordiontab';
</script>
<template>
    <Accordion>
        <AccordionTab>
            <template #header>
                <slot name="header"></slot>
            </template>
            <slot></slot>
        </AccordionTab>
    </Accordion>
</template>