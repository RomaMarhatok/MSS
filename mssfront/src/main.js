import { createApp } from 'vue'
import App from './App.vue'
import router from "../router.js"
import PrimeVue from "primevue/config"
import './index.css'
import "primevue/resources/primevue.min.css"
import "primeicons/primeicons.css"
import "primevue/resources/themes/saga-blue/theme.css"

const app = createApp(App)
app.use(PrimeVue)
app.use(router).mount('#app')

