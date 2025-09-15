import { defineStore } from 'pinia';
import { reactive, ref } from 'vue';

import { type UiStoreSettings } from '@/shared/types/stores/uiStore';

export const useUiStore = defineStore('uiStore', () => {
	const uiKey = ref<UiSectionKey>('main');

	const settings = reactive<UiStoreSettings>({
		main: {},
		layout_sidebar: {}
	});

	const setUiKey = (key: UiSectionKey) => {
		uiKey.value = key;
	};

	function getUiSetting<
		Section extends UiSectionKey = typeof uiKey['value'],
		Key extends keyof UiStoreSettings[Section] = keyof UiStoreSettings[Section]
	>(key: Key, section?: Section): UiStoreSettings[Section][Key] {
		const sectionKey = section || uiKey.value as Section;

		return settings[sectionKey][key];
	}

	function setUiSetting<
		Section extends UiSectionKey = typeof uiKey['value'],
		Key extends keyof UiStoreSettings[Section] = keyof UiStoreSettings[Section],
		Value extends UiStoreSettings[Section][Key] = UiStoreSettings[Section][Key]
	>(key: Key, value: Value, section?: Section): void {
		const sectionKey = section || uiKey.value as Section;

		settings[sectionKey][key] = value;
	}

	return {
		uiKey,
		settings,
		setUiKey,
		getUiSetting,
		setUiSetting
	};
}, {persist: true});

export type UiSectionKey = keyof UiStoreSettings;