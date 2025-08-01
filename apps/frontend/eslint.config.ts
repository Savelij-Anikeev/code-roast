import js from '@eslint/js';
import vue from 'eslint-plugin-vue';
import vueParser from 'vue-eslint-parser';
import tseslint from 'typescript-eslint';

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ['**/*.vue'],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        parser: tseslint.parser,
        extraFileExtensions: ['.vue'],
      },
    },
    plugins: {
      vue,
    },
    rules: {
      ...vue.configs.base.rules,
      ...vue.configs.recommended.rules,
      'vue/comment-directive': 'off',
      'vue/multi-word-component-names': 'off',
      'vue/no-unused-components': 'warn',
      'vue/no-unused-vars': 'error',
      'no-console': 'error',
      'no-debugger': 'error',
      'max-len': ['error', {
        code: 100,
        ignoreComments: false,
        ignoreStrings: false,
        ignoreTemplateLiterals: false,
        ignoreRegExpLiterals: false,
      }],
      'vue/max-len': ['error', {
        code: 100,
        template: 100,
        tabWidth: 2,
        comments: 100,
        ignorePattern: '',
        ignoreComments: false,
        ignoreStrings: false,
        ignoreHTMLAttributeValues: false,
        ignoreHTMLTextContents: false,
      }]
    },
  },
  {
    files: ['**/*.ts'],
    ...tseslint.configs.recommended[0],
  },
];