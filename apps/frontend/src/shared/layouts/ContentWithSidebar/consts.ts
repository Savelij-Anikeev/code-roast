import { ROUTES } from "@/routing/consts";

import cube from '@/assets/icons/cube-96.svg';

export const NAV_POINTS = [
	{
		label: 'home',
		img: cube,
		to: ROUTES.ROOT.HOME
	},
	{
		label: 'auth',
		img: cube,
		to: ROUTES.ROOT.AUTH
	},
	{
		label: 'reviews',
		img: cube,
		to: ROUTES.ROOT.REVIEWS.LIST
	}
] as const;