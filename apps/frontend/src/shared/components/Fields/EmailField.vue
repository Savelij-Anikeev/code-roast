<script setup lang="ts">
import TextField from './TextField.vue';
import { ref } from 'vue';

const props = defineProps<{
  modelValue: string;
  placeholder?: string;
  label?: string;
  disabled?: boolean;
  fullWidth?:boolean;
}>();

const emits = defineEmits<{
  (e: 'update:modelValue', value: string): void;
}>();

const value = ref(props.modelValue);

const onUpdate = (val: string) => {
  value.value = val;
  emits('update:modelValue', val);
};
</script>

<template>
  <TextField
    v-model="value"
    :type="'email'"
    :placeholder="props.placeholder"
    :label="props.label"
    :disabled="props.disabled"
    :fullWidth="props.fullWidth"
    @update:modelValue="onUpdate"
  />
</template>