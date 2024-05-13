import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import {createPinia} from "pinia";
import router from "./router.js";
import axios from 'axios';

// axios.defaults.withCredentials = true;
// axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
//
window.axios = axios;
window.axios.defaults.baseURL = 'http://localhost:8000'



// axios.defaults.headers["Authorization"] = `Bearer ${localStorage.getItem('access_token')}`
//
// axios.interceptors.request.use((req) => {
//     axios.defaults.headers["Authorization"] = `Bearer ${localStorage.getItem('access_token')}`
//     return req
// })


const pinia = createPinia()
const app = createApp(App)

app
    .use(router)
    .use(pinia)
    .mount('#app')
