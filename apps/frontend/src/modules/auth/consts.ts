export enum Step {
	LOGIN = 0,
	REGISTER = 1,
	CONFIRMATION = 2
}

export const LABEL_BY_STEP = {
	[Step.LOGIN]: 'Login',
	[Step.REGISTER]: 'Registration',
	[Step.CONFIRMATION]: 'Confirmation'
};

export const NEXT_BUTTON_BY_STEP = {
	[Step.LOGIN]: 'login',
	[Step.REGISTER]: 'register account',
	[Step.CONFIRMATION]: 'confirm'
}