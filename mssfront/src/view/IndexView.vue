<script setup>
// import { ref } from "vue";
import HomePageNavBar from "@/components/layout/Navbars/HomePageNavBar.vue"
// import IndexViewCard from "@/components/common/Cards/IndexViewCard.vue"
// const title = ref("SOME TEXT")
// const text = ref("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
</script>
<template>
  <header class="">
    <div class="header-media pl-2">
      <div class="items-center self-center">
        <span class="font-black underline text-black text-4xl">MSS</span>
      </div>
      <HomePageNavBar></HomePageNavBar>
    </div>
  </header>
  <main>
    <div class="relative w-full h-full pt-1">
      <div class="absolute text-center font-black left-10 top-10">
        <div class="header-text">MEDICINE<br />SYSTEM STORAGE</div>
        <div class="body-text text-custom-dark-aqua">
          Lorem Ipsum is simply dummy<br />
          text of the<br />
          printing and<br />
          typesetting industry.
        </div>
      </div>
      <img class="object-cover max-w-full max-h-full" src="@/assets/frontPageDoctorImage.svg" alt="doctor image" />
    </div>
    <!-- <div class="card-container">
      <IndexViewCard :title="title" :text="text" />
      <IndexViewCard :title="title" :text="text" />
      <IndexViewCard :title="title" :text="text" />
    </div> -->
  </main>
  <footer>
    <div class="footer">
      <div class="footer__div"></div>
    </div>
  </footer>
</template>
<style scoped>
.header-media {
  display: flex;
  flex-direction: row;
}

.header-text {
  font-size: 3vw;
}

.card-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 1em;
  gap: 2em;
}

.body-text {
  font-size: 2.5vw;
}

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

@media screen and (max-width: 600px) {
  .card-container {
    display: flex;
    flex-direction: column;
    /* display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-auto-flow: row dense;
    justify-items: center;
    row-gap: 1rem; */
  }

  .header-media {
    display: flex;
    flex-direction: column;
    ;
  }
}
</style>