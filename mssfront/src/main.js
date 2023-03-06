import { createApp } from 'vue'
import App from './App.vue'
import router from "../router.js"
import PrimeVue from "primevue/config"
import './index.css'
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import store from "./store"
import 'v-calendar/dist/style.css';
import VCalendar from 'v-calendar';
import Tooltip from 'primevue/tooltip'; 
library.add(fas)
const app = createApp(App)
app.use(PrimeVue)
app.use(router)
app.use(store)
app.use(VCalendar,{})
app.component('font-awesome-icon', FontAwesomeIcon).mount('#app')
app.directive('tooltip',Tooltip)

