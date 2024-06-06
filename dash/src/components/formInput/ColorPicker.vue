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
    <q-input
      v-model="value"
      filled
      bottom-slots
      :label="props.placeholder ? props.placeholder : 'plase input '"
      @update:model-value="$emit('update:text', value)"
      lazy-rules
      :rules="
        props.isValid
          ? [(val) => (val && val.length > 0) || 'This field must be entered']
          : []
      "
    >
      <template v-slot:append>
        <q-icon name="colorize" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-color v-model="value" />
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, computed, PropType } from 'vue';
//model
import { Validation } from 'src/model/base/base';

const emit = defineEmits(['update:text']);

const props = defineProps({
  placeholder: {
    type: String,
    default: '',
  },
  col: {
    type: String,
    default: '6',
  },
  label: {
    type: String,
    default: '',
    required: false,
  },
  default: {
    type: String,
    default: '',
  },
  isValid: {
    type: Boolean,
    default: false,
  },
});
const value = ref(props.default);
</script>
