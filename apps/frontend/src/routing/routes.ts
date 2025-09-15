import { createRouter, createWebHistory } from 'vue-router';

import ContentWithSidebar from '@/shared/layouts/ContentWithSidebar/Layout.vue';

import Home from './pages/Home.vue';
import Review from './pages/Review.vue';
import Profile from './pages/Profile.vue';

import { ROUTES } from './consts';

export const router = createRouter({
	history: createWebHistory(),
	routes: [
		{
			path: '/',
			component: ContentWithSidebar,
			children: [
				{
					path: '',
					name: ROUTES.ROOT.HOME,
					component: Home
				},
				{
					path: 'auth',
					name: ROUTES.ROOT.AUTH,
					component: () => import('@/modules/auth/page.vue'),
				},
				{
					path: 'reviews',
					children: [
						{
							path: '',
							name: ROUTES.ROOT.REVIEWS.LIST,
							component: Review
						},
						{
							path: ':id',
							name: ROUTES.ROOT.REVIEWS.SINGLE,
							component: Review
						},
					]
				},
				{
					path: 'profile/:id',
					name: ROUTES.ROOT.PROFILE,
					component: Profile
				},
			]
		}
	]
})
