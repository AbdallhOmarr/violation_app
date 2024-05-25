<template>
  <div :class="`col-${props.col}`" class="q-pa-sm q-mb-sm">
    <q-radio
      v-model="value"
      :val="value"
      :color="props.color"
      :label="props.label"
      @update:model-value="$emit('update:check', value)"
      :size="props.size"
    />
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, computed, PropType } from 'vue';
import { useI18n } from 'vue-i18n';

const emit = defineEmits(['update:check']);

const props = defineProps({
  col: {
    type: String,
    default: '6',
  },
  label: {
    type: String,
    default: '',
  },
  default: {
    type: String,
    default: '',
  },
  color: {
    type: String,
    default: 'primary',
  },
  size: {
    type: String,
    default: 'lg',
  },
});
const value = ref(props.default);
</script>
