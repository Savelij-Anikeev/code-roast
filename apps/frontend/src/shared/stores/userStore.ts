import { defineStore } from 'pinia';
import { reactive } from 'vue';

import { type User } from '@/shared/types/stores/userStore';

export const useUserStore = defineStore('userStore', () => {
	const user = reactive<User>({
		username: 'anonymouse',
		email: 'xxx@xxx.xx',
		avatar: ''
	});

	const setUser = ({username, email, avatar}: User) => {
		user.username = username;
		user.email = email;
		user.avatar = avatar;
	}

	return {
		// refs
		user,

		// actions
		setUser
	}
});