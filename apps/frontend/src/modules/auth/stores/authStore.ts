import { defineStore } from 'pinia';
import { reactive, ref } from 'vue';

import { SEX } from '@/shared/enums/auth';

import { Step } from '../consts.ts';

export const useAuthStore = defineStore('authStore', () => {
	const values = reactive<Partial<AllValues>>({
		email: '',
		password: ''
	});
	const step = ref<Step>(Step.LOGIN);

	const setValue = <
		K extends keyof AllValues,
		V extends AllValues[K]
	>(key: K, val: V) => {
		values[key] = val;
	}

	const setStep = (newStep: Step) => {
		step.value = newStep;
	}

	return {
		// observable
		values,
		step,

		// actions
		setValue,
		setStep
	}
});

type LoginValues = {
	email: string;
	password: string;
};

type RegistrationValues = LoginValues & {
	username: string;
	repeatedPassword: string;
	sex: SEX;
};

type AllValues = LoginValues | RegistrationValues;