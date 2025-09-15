<script setup lang="ts">
import LiveBackground from "@/shared/components/LiveBackground.vue";
import cubeIcon from '@/assets/icons/cube-96.svg';

import Card from './components/Card.vue';
</script>

<template>
  <div class="page">
    <Card />
    <LiveBackground :image="cubeIcon" :direction="{inverse: true}" />
  </div>
</template>

<style lang="scss" scoped>
.page {
  display: flex;
}
</style>