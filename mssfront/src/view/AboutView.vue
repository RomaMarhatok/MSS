<script setup>
import HomePageNavBar from "@/components/layout/Navbars/HomePageNavBar.vue"
// import TabView from 'primevue/tabview';
// import TabPanel from 'primevue/tabpanel';
</script>
<template>
    <main>
        <header class="bg-white">
            <div class="header-media pl-2">
                <div class="items-center self-center">
                    <span class="font-black underline text-black text-4xl">MSS</span>
                </div>
                <HomePageNavBar></HomePageNavBar>
            </div>
        </header>
        <section class="p-4 body">
            <div class="bg-white rounded">
                <div>
                    <div class="pt-4">
                        <p class="text-center">
                            Для того чтобы войти в в данное веб-приложение как пациент пользователь требуется выполнить
                            несколько шагов:
                        </p>
                    </div>
                    <div class="flex flex-row mt-4 gap-2 p-4">
                        <div>
                            <div>
                                <p class="text-center text-xl">Шаг 1 Регистрация</p>
                                <p class="text-center text-lg">Перейдете на вкладку Регистрация и введине все
                                    необходимые данные
                                    в форму регситрации
                                </p>
                                <img class="object-cover max-w-full max-h-full" src="@/assets/registrationFormImage.png"
                                    alt="doctor image" />
                            </div>
                            <div>
                                <p class="text-center text-lg">После чего на вашу почту будет отправлено сообщение об
                                    верификации пример сообщения</p>
                                <img class="object-cover max-w-full max-h-full" src="@/assets/emailMassageImage.png"
                                    alt="doctor image" />
                            </div>
                        </div>
                        <div>
                            <p class="text-center text-xl">Шаг 2 Вход</p>
                            <p class="text-center text-lg">Перейдете на вкладку Войти и введине все
                                необходимые данные
                                в форму авторизации
                            </p>
                            <img class="object-cover max-w-full max-h-full" src="@/assets/authForm.png" />
                        </div>
                    </div>
                    <div class="flex flex-col">
                        <div class="flex flex-row gap-4">
                            <div class="flex flex-col">
                                <p class="text-center text-xl mt-4">Личный кабинет пользователя</p>
                                <p>На данной странице вы можете увидеть навигационное меню в верхней чатси экрана.Так же
                                    пользователь на этой странице может просмотреть все свои записи к врачам.</p>
                                <img class="object-cover max-w-full max-h-full" src="@/assets/personalInfoImage.png" />
                            </div>

                            <div class="flex flex-col">
                                <p class="text-center text-xl mt-4">Документы пользователя</p>
                                <p>На данной странице пользователь может просмотреть свои документы</p>
                                <img class="object-cover max-w-full max-h-full" src="@/assets/documentPatientPage.png" />
                            </div>
                        </div>
                        <div class="flex flex-row gap-4">
                            <div class="flex flex-col">
                                <p class="text-center text-xl mt-4">История лечения пользователя</p>
                                <p>На данной странице пользователь может просмотреть свою историю лечения.</p>
                                <img class="object-cover max-w-full max-h-full"
                                    src="@/assets/treatmentHistoryPatientPage.png" />
                            </div>
                            <div class="flex flex-col">
                                <p class="text-center text-xl mt-4">История лечения пользователя</p>
                                <p>При нажатии на
                                    пункты
                                    меню списков документов и изображений откроется модальное окно</p>
                                <img class="object-cover max-w-full max-h-full"
                                    src="@/assets/treatmentHistortyPatientModalPage.png" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>
<style lang="css" scoped>
.body {
    background-color: rgba(110, 131, 165, 0.103);
}

.header-media {
    display: flex;
    flex-direction: row;
}

@media screen and (max-width: 600px) {
    .header-media {
        display: flex;
        flex-direction: column;
        ;
    }
}
</style>