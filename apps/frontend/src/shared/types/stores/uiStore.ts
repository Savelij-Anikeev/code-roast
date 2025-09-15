export interface UiStoreSettings {
	main: Partial<{
		theme?: 'light' | 'dark'
	}>,
	layout_sidebar: Partial<{
		isCollapsed: boolean;
	}>
}