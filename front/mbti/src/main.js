import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin, CarouselPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
{/* <script src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.1.10/vue.min.js"></script>
<script src="https://unpkg.com/survey-vue"></script>
<link href="https://unpkg.com/survey-vue/survey.min.css" type="text/css" rel="stylesheet"/> */}

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.use(CarouselPlugin)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin) 

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
