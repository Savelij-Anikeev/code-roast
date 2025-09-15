<script setup lang="ts">
import TextField from './TextField.vue';
import { ref } from 'vue';

const props = defineProps<{
  modelValue: string;
  placeholder?: string;
  label?: string;
  disabled?: boolean;
  fullWidth?: boolean;
}>();

const emits = defineEmits<{
  (e: 'update:modelValue', value: string): void;
}>();

const value = ref(props.modelValue);
const showPassword = ref(false);

const onUpdate = (val: string) => {
  value.value = val;
  emits('update:modelValue', val);
};

const toggleVisibility = () => {
  showPassword.value = !showPassword.value;
};
</script>

<template>
  <div class="password-field">
    <TextField
      v-model="value"
      :type="showPassword ? 'text' : 'password'"
      :placeholder="props.placeholder"
      :label="props.label"
      :disabled="props.disabled"
      :fullWidth="props.fullWidth"
      @update:modelValue="onUpdate"
    />
    <button type="button" class="toggle-btn" @click="toggleVisibility">
      {{ showPassword ? 'Hide' : 'Show' }}
    </button>
  </div>
</template>

<style scoped>
.password-field {
  position: relative;

  .toggle-btn {
    position: absolute;
    right: 10px;
    bottom: 36px;
    background: transparent;
    border: none;
    cursor: pointer;
    font-size: 12px;
    color: #555;
  }
}
</style>