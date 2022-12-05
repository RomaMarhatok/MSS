<script setup>
</script>
<template>
  <div class="main__container">
    <div class="container__description">
      <div class="description__header">MEDICINE<br />SYSTEM STORAGE</div>
      <div class="description__body">
        Lorem Ipsum is simply dummy<br />
        text of the<br />
        printing and<br />
        typesetting industry.
      </div>
    </div>
    <img class="container__img" src="@/assets/frontPageDoctorImage.svg" alt="doctor image" />
  </div>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans&display=swap');

.main__container {
  position: relative;
  width: 100%;
  height: 100%;
}

.container__description {
  position: absolute;
  text-align: center;
  font-weight: bolder;
  font-family: "Fira Sans";
  top: 15%;
  left: 5%;
  display: flex;
  flex-direction: column;
}

.description__header {
  font-size: 3vw;
}

.description__body {
  color: #ab8645;
  font-size: 2.5vw;
}

.container__img {
  object-fit: cover;
  max-width: 100%;
  max-height: 100%;
}
</style>