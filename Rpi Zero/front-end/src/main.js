import { createApp } from 'vue'
import router from './router/router'
import store from './store'
import App from './App.vue'
import VueApexCharts from "vue3-apexcharts";

import './css/style.css'

const app = createApp(App)
app.use(router)
app.use(store)
app.use(VueApexCharts);
app.mount('#app')

app.config.errorHandler = (err, vm, info) => {
    console.error("Error:", err);
    console.error("Vue component:", vm);
    console.error("Additional info:", info);
};

app.config.warnHandler = (err, vm, info) => {
console.error("Error:", err);
console.error("Vue component:", vm);
console.error("Additional info:", info);
};

app.config.performance = true;
app.config.silent = true;