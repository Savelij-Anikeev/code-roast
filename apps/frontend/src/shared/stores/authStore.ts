import { defineStore } from 'pinia';
import { reactive } from 'vue';

export const useAuthStore = defineStore('authStore', () => {
	const values = reactive<Partial<AuthValues>>({});

	const setValue = <
		Key extends keyof AuthValues = keyof AuthValues,
	>(key: Key, value: AuthValues[Key]) => {
		values[key] = value;
	}

	return {
		// refs and reactives
		values,

		// actions
		setValue
	}
});

interface AuthValues {
	username: string;
	email: string;
	password: string;
	verificationCode: string;
}