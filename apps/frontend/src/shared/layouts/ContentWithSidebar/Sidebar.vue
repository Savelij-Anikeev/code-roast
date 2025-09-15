<script setup lang="ts">
import { useRoute } from 'vue-router';
import { ref, computed } from 'vue';

import logoIcon from '@/assets/icons/logo-100.svg';
import userIcon from '@/assets/icons/user-100.svg';

import { ROUTES } from '@/routing';
import { useUiStore, useUserStore } from '@/shared/stores';

import { NAV_POINTS } from './consts';

const SIDEBAR_WIDTH = {
  MIN: 60,
  MAX: 220
} as const;

const route = useRoute();
const uiStore = useUiStore();
const userStore = useUserStore();

uiStore.setUiKey('layout_sidebar');

const isCollapsed = ref<boolean>(uiStore.getUiSetting<'layout_sidebar'>('isCollapsed') || false);
const sidebarWidth = computed(() => isCollapsed.value ? SIDEBAR_WIDTH.MIN : SIDEBAR_WIDTH.MAX);

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value;
  uiStore.setUiSetting<'layout_sidebar'>('isCollapsed', isCollapsed.value);
}
</script>

<template>
  <div
    class="sidebar"
    :style="{ width: sidebarWidth + 'px' }"
  >
    <div class="header">
      <img :src="logoIcon" alt="Logo" class="logo" />
      <h4 v-if="!isCollapsed">ROAST_MY_CODE</h4>
    </div>

    <div class="points">
      <router-link
        v-for="item in NAV_POINTS"
        :key="item.to"
        :to="{ name: item.to }"
        class="item"
        :class="{ active: route.name === item.to }"
      >
        <img :src="item.img" :alt="item.label" class="item-icon">
        <span v-if="!isCollapsed">{{ item.label }}</span>
      </router-link>
    </div>

    <div class="profile" v-if="!isCollapsed">
      <img
        :src="userStore.user.avatar || userIcon"
        class="avatar"
        alt="profile image"
      />
      <div class="info">
        <span class="nickname">{{ userStore.user.username }}</span>
        <span class="role">{{ userStore.user.email }}</span>
      </div>
    </div>
    <router-link
      v-else :to="ROUTES.ROOT.HOME"
      class="minimized-profile"
    >
      <img
        :src="userStore.user.avatar || userIcon"
        class="avatar"
        alt="profile image"
      />
    </router-link>

    <div
      class="resizer"
      aria-label="Resize sidebar"
      role="button"
      @dblclick="toggleSidebar"
    ></div>
  </div>
</template>

<style lang="scss" scoped>
@import '@/shared/styles/animations.scss';

.sidebar {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: $gap;
  height: 100%;
  background-color: $dark;
  color: $opposite;
  padding: $gap;
  transition: width 0.2s ease;
  overflow: hidden;

  .header {
    width: 100%;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: start;
    padding: $padding;
    gap: $gap;
    white-space: nowrap;

    .logo {
      height: 24px;
      min-width: 24px;
    }
  }

  .points {
    display: flex;
    flex-direction: column;
    padding: $padding;

    .item {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      height: 40px;
      width: 100%;
      gap: calc($gap + 12px);
      white-space: nowrap;

      .item-icon {
        display: flex;
        height: 14px;
        aspect-ratio: 1;
      }

      &.active:before {
        position: absolute;
        content: '';
        margin-left: -20px;
        background-color: $additional;
        width: 4px;
        height: 100%;
        transform: scaleY(0);
        transform-origin: center;
        animation: anim-expand-from-center 0.3s ease-out forwards;
      }
    }
  }

  .profile {
    display: flex;
    gap: $gap;
    height: 60px;
    width: 100%;
    margin-top: auto;
    padding: $padding;
    white-space: nowrap;

    .avatar {
      height: 100%;
      min-width: 40px;
      aspect-ratio: 1;
      background-color: $opposite;
    }

    .info {
      display: flex;
      flex-direction: column;

      :last-child {
        color: $grey;
      }
    }
  }

  .minimized-profile {
    display: flex;
    align-items: flex-end;
    justify-content: center;
    margin-top: auto;

    img {
      height: 40px;
    }
  }

  .resizer {
    position: absolute;
    top: 0;
    right: -5px;
    width: 10px;
    height: 100%;
    cursor: ew-resize;
    z-index: 10;
    background-color: transparent;

    &:hover {
      background-color: rgba(255, 255, 255, 0.1);
    }
  }
}
</style>