import 'normalize.css'

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';

import '@/shared/styles/main.scss';
import { router } from '@/routing';

import App from './App.vue';

createApp(App)
	.use(router)
	.use(createPinia().use(piniaPluginPersistedstate))
	.mount('#app')
