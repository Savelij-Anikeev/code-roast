import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

import * as path from "node:path";

export default defineConfig({
  plugins: [vue()],
  base: '/',
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/shared/styles/variables.scss" as *;`
      }
    }
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 80,
    host: '0.0.0.0',
    strictPort: true,
    allowedHosts: ['localhost', 'code-roaster.ai']
  }
})
