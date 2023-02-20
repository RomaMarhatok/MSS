<script setup>
import homePageHeader from "@/components/layout/Headers/HomePageHeader.vue";
import homePageDoctorImageSection from "@/components/ui/Sections/HomePage/DoctorImageSection.vue";
import homePageCardsSection from "@/components/ui/Sections/HomePage/CardsSection.vue";
</script>

<template>
  <homePageHeader />
  <homePageDoctorImageSection />
  <homePageCardsSection />
  <footer class="footer">
    <div class="footer__div"></div>
  </footer>
</template>


<style scoped>
.footer {
  margin-top: 3%;
  background: rgba(19, 48, 94, 1);
  height: 100px;
  width: 100%;
}

.footer__div {
  background: white;
  height: 15%;
  width: auto;
  border-radius: 0 0 100% 100%;
}
</style>