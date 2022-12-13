import { createApp } from 'vue'
import App from './App.vue'
import router from "../router.js"
import PrimeVue from "primevue/config"
import './index.css'
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
library.add(faUserSecret)
const app = createApp(App)
app.use(PrimeVue)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon).mount('#app')


