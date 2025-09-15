<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{
  modelValue: string;
  placeholder?: string;
  label?: string;
  disabled?: boolean;
  type?: string;
  fullWidth?: boolean;
}>();

const emits = defineEmits<{
  (e: `update:${typeof props.modelValue}`, value: string): void;
}>();

const inputValue = ref(props.modelValue);

const onInput = (e: Event) => {
  const target = e.target as HTMLInputElement;
  inputValue.value = target.value;
  emits(`update:modelValue`, target.value);
};
</script>

<template>
  <div class="textfield-wrapper">
    <label v-if="props.label" class="textfield-label">{{ props.label }}</label>
    <input
      :type="props.type || 'text'"
      class="textfield"
      :placeholder="props.placeholder"
      :disabled="props.disabled"
      :value="inputValue"
      :style="{
        width: props.fullWidth ? '100%' : 'auto'
      }"
      @input="onInput"
    />
  </div>
</template>

<style lang="scss" scoped>
.textfield-wrapper {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.textfield {
  padding: 8px 12px;
  border: 1px solid $opposite;
  border-radius: 6px;
  font-size: 14px;
  background-color: $dark;
  outline: none;
  transition: border-color 0.2s;
  color: $opposite;

  &:focus {
    border-color: $sexy;
  }
}

.textfield-label {
  color: $opposite;
}
</style>