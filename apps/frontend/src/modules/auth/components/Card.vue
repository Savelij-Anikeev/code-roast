<script setup lang="ts">
import { EmailField, PasswordField } from '@/shared/components/Fields';
import Button from '@/shared/components/Button.vue';

import { useAuthStore } from '../stores/authStore';
import {
  LABEL_BY_STEP,
  NEXT_BUTTON_BY_STEP,
  Step
} from '../consts';

const authStore = useAuthStore();

</script>

<template lang="html">
  <div class="container">
    <div class="header">
      {{ LABEL_BY_STEP[authStore.step] }}
    </div>
    <form class="form">
      <EmailField
        v-model='authStore.values.email'
        label='E-Mail'
        placeholder='example@some.site'
        class="field"
        :fullWidth="true"
      />
      <PasswordField
        v-model='authStore.values.password'
        label='Password'
        placeholder='example@some.site'
        class="field"
        :fullWidth="true"
      />
      <PasswordField
        v-if='authStore.step === Step.REGISTER'
        v-model='authStore.values.password'
        label='Repeat password'
        placeholder='example@some.site'
        class="field"
        :fullWidth="true"
      />
      <Button>
        {{ NEXT_BUTTON_BY_STEP[authStore.step] }}
      </Button>
    </form>

    <div>
      {{
        authStore.step === Step.LOGIN ?
          'Do not have a account yet? ' :
          'Already have a account?? '
      }}
      <span
        @click="authStore.setStep(authStore.step === Step.LOGIN ? Step.REGISTER : Step.LOGIN)"
        class="clickable"
      >
        {{ authStore.step === Step.LOGIN ? 'register' : 'login'}}
      </span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use '@/shared/styles/misc.scss' as *;

.container {
  display: flex;
  flex-direction: column;
  width: 400px;
  min-height: 400px;
  background: $dark;
  margin: auto;
  color: $opposite;
  gap: $gap;

  .header {
    display: flex;
    width: 100%;
    height: 75px;
    align-items: center;
    justify-content: center;
    font-weight: lighter;
    padding: $padding;
    font-size: 24px;
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: $gap;
    padding: 0 $gap;
  }
}
</style>