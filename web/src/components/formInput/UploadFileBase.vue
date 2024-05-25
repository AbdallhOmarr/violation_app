<template>
  <div :class="`col-${props.col}`" class="q-pa-sm q-mb-sm">
    <div v-if="props.label" class="text-subtitle2 text-weight-regular">
      <span
        v-if="props.isValid"
        style="padding: 0.3rem; font-weight: bold; color: var(--q-negative)"
      >
        *
      </span>
      {{ props.label }}
    </div>
    <q-file
      name="cover_files"
      v-model="value"
      filled
      :multiple="props.multiple"
      use-chips
      :label="props.placeholder ? props.placeholder : 'plase select file '"
      @update:model-value="$emit('update:text', value)"
      :rules="
        props.isValid
          ? [(val) => (val && val.length > 0) || 'This field must be entered']
          : []
      "
    >
      <template v-slot:prepend>
        <q-icon name="attach_file" />
      </template>
    </q-file>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref, computed } from 'vue';

const emit = defineEmits(['update:text']);

const props = defineProps({
  placeholder: {
    type: String,
    default: '',
  },
  col: {
    type: String,
    default: '12',
  },
  label: {
    type: String,
    default: 'file',
    required: false,
  },
  default: { default: '' },
  isValid: {
    type: Boolean,
    default: false,
  },
  multiple: {
    type: Boolean,
    default: false,
  },
});
const value = ref(props.default);
</script>
