<script setup lang="ts">
const props = defineProps<{
  // eslint-disable-next-line @typescript-eslint/no-unsafe-function-type
  onClick?: Function;
}>();
</script>

<template>
<button class='btn' @click.prevent='props.onClick'>
  <slot />
</button>
</template>

<style scoped lang="scss">
  .btn {
    height: 32px;
    border: 1px solid $opposite;
    color: $opposite;
    border-radius: $radius;
    box-shadow: none;
    background-color: $dark;
    cursor: pointer;

    &:hover {
      background-color: $primary;
      transition: 0.2s;
    }
  }
</style>