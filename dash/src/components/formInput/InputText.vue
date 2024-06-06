<template>
  <div :class="`col-${props.col}`" class="q-pa-sm q-mb-sm">
    <div v-if="props.label" class="text-subtitle2 text-weight-regular">
      <span v-if="props.isValid" style="padding: 0.3rem; font-weight: bold; color: var(--q-negative)">
        *
      </span>
      {{ props.label }}
    </div>
    <q-input v-model="value" filled :mask="props.mask" :hint="props.hint" bottom-slots
      :type="props?.type ? props?.type : 'text'" :label="props.placeholder ? props.placeholder : ' '"
      @update:model-value="$emit('update:text', value)" :rules="props.isValid
        ? [(val) => (val && val.length > 0) || 'This field must be entered']
        : []
        " :readonly="props.readonly">
      <template v-if="props.isIcon" v-slot:prepend>
        <q-icon :name="props.icon" />
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
  isIcon: {
    type: Boolean,
    default: false,
  },
  icon: {
    type: String,
    default: '',
  },
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
  type: {
    type: String,
    default: 'text',
  },
  mask: {
    type: String,
    default: '',
  },
  hint: {
    type: String,
    default: '',
  },
  isValid: {
    type: Boolean,
    default: false,
  },
  readonly: {
    type: Boolean,
    default: false,
  },
});
const value = ref(props.default);
</script>
