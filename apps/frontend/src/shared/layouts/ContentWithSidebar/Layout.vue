<script>
import {defineComponent} from "vue";

import Sidebar from './Sidebar.vue';

export default defineComponent({
  components: {Sidebar}
});
</script>

<template>
  <div class="layout">
    <Sidebar />
    <main class="content">
      <router-view />
    </main>
  </div>
</template>

<style lang="scss" scoped>
  .layout {
    display: flex;
    height: 100vh;
    width: 100vw;
    overflow: hidden;
  }

  .content {
    flex: 1;
    height: 100%;
    overflow-y: auto;
    padding: 16px;
  }
</style>