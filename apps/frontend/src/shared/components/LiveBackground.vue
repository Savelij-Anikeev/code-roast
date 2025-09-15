<script setup lang="ts">
const props = defineProps<{
  image: string
  speed?: number
  inverse?: boolean
  direction?: {
    x?: boolean
    y?: boolean
    inverse?: boolean
  }
}>()

const duration = props.speed ?? 30
const dir = props.direction ?? {}
</script>

<template>
  <div
    class="moving-bg"
    :style="{
      backgroundImage: `url(${props.image})`,
      animationDuration: duration + 's',
      '--dir-x': !dir.x ? `${dir.inverse ? '' : '-'}500px` : '0',
      '--dir-y': !dir.y ? `${dir.inverse ? '' : '-'}500px` : '0',
    }"
  ></div>
</template>