<script setup>
import HomePageNavBar from "@/components/layout/Navbars/HomePageNavBar.vue"
</script>
<template>
    <main class="body">
        <header class="bg-white">
            <div class="header-media pl-2">
                <div class="items-center self-center">
                    <span class="font-black underline text-black text-4xl">MSS</span>
                </div>
                <HomePageNavBar></HomePageNavBar>
            </div>
        </header>
        <section class="p-4">
            <div class="bg-white header-border">
                <p class="text-center text-3xl pb-4">О веб-приложении Медицинская карта</p>
            </div>
            <div class="bg-white body-border">
                <p class="text-center text-xl">
                    Данное веб-приложение было разработано сцелью автоматизации работы медицнского персонала.
                </p>
                <p class="text-center text-lg">
                    веб-приложение было создано с помощью таки библиотек(фреймворков) как:
                </p>
                <div class="flex flex-col gap-4">
                    <div class="item">
                        <div class="header">
                            <p class="item-header-text">Vue</p>
                            <p class="item-body-text">
                                Прогрессивный веб–фреймворк для создания пользовательских интерфейсов.
                                В отличие от фреймворков–монолитов, Vue создавался пригодным для постепенного внедрения.
                                Его ядро в первую очередь решает задачи уровня представления, упрощая интеграцию с другими
                                библиотеками
                                и
                                существующими проектами.
                                Благодаря системе компонентов представленной во многих современных frontend фреймворках
                                облегчает
                                создание
                                страниц благодаря их переиспользованию в коде.
                                Основным достоинством данного фреймворка является его реактивность, что выражается
                                динамическим
                                изменением
                                компонентов.
                            </p>
                        </div>
                    </div>
                    <div class="item">
                        <div class="header">
                            <p class="item-header-text">Vuex</p>
                        </div>
                        <p class="item-body-text">
                            Библиотека для приложений на Vue.js. Он служит централизованным хранилищем данных для всех
                            компонентов приложения с правилами, гарантирующими, что состояние может быть изменено только
                            предсказуемым
                            образом.
                        </p>
                    </div>
                    <div class="item">
                        <div class="header">
                            <p class="item-header-text">Vue-router</p>
                        </div>
                        <p class="item-body-text">
                            Официальная библиотека маршрутизации для Vue. Она глубоко интегрируется с Vue.js и
                            позволяет
                            легко создавать SPA-приложения
                        </p>
                    </div>
                    <div class="item">
                        <div class="header">
                            <p class="item-header-text">Django</p>
                        </div>
                        <p class="item-body-text">
                            Это высокоуровневый Python веб–фреймворк, который позволяет быстро создавать безопасные и
                            поддерживаемые веб–сайты. Созданный опытными разработчиками, Django берёт на себя большую часть
                            хлопот
                            веб–разработки, поэтому вы можете сосредоточиться на написании своего веб-приложения без
                            необходимости
                            изобретать велосипед. Он бесплатный и с открытым исходным кодом, имеет растущее и активное
                            сообщество,
                            отличную документацию и множество вариантов как бесплатной, так и платной поддержки.
                        </p>
                    </div>
                    <div class="item">
                        <div class="header">
                            <p class="item-header-text">Django REST Framework</p>
                        </div>
                        <p class="item-body-text">
                            Это мощный и гибкий фреймворк, предназначенный для ускорения разработки backend
                            составляющей приложение, благодаря предлагаемым средствам и структурам входящих в состав этого
                            фреймворка.
                        </p>
                    </div>
                    <div class="item mb-4">
                        <div class="header">
                            <p class="item-header-text">PyTest</p>
                        </div>
                        <p class="item-body-text">
                            Для написания тестирования была использована библиотека PyTest – библиотека предлагает
                            возможность
                            легко
                            писать небольшие читаемые тесты и может масштабироваться для поддержки сложного функционального
                            тестирования
                            приложений и библиотек.
                        </p>
                    </div>
                </div>
            </div>
        </section>

    </main>
</template>
<style scoped lang="css">
.body {
    background-color: rgba(110, 131, 165, 0.103);
}

.header-border {
    border: 1px solid rgb(218, 218, 218);
    border-radius: 5px 5px 0 0;
    border-width: 1px 1px 0px 1px;
}

.body-border {
    border: 1px solid rgb(218, 218, 218);
    border-radius: 0 0 5px 5px;
    border-width: 0px 1px 1px 1px;

}

.header-media {
    display: flex;
    flex-direction: row;
}

.item {
    background-color: rgba(142, 249, 243, 0.4);
    border-radius: 5px;
    margin: 1rem 1rem 0 1rem;
}

.item-header-text {
    font-size: 1.5rem;
    line-height: 2rem;
    text-align: center;
}

.item-body-text {
    padding: 1rem;
}

@media screen and (max-width: 600px) {
    .header-media {
        display: flex;
        flex-direction: column;
        ;
    }
}
</style>