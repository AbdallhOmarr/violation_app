<template>
  <div :class="`col-${props.col}`" class="q-pa-sm q-mb-sm">
    <div v-if="props.label" class="text-subtitle2 text-weight-regular">
      <span v-if="props.isValid" style="padding: 0.3rem; font-weight: bold; color: var(--q-negative)">
        *
      </span>
      {{ props.label }}
    </div>
    <q-select v-model="value" filled use-input :loading="props.loading" :multiple="props.isMultiple"
      :label="props.placeholder ? props.placeholder : ''" :options="options" emit-value map-options
      :bg-color="props.color" :option-label="(item) =>
        item?.[props.optionLabel]?.[$i18n.locale]
          ? item?.[props.optionLabel]?.[$i18n.locale]
          : item?.[props.optionLabel]
        " :option-value="props.default ? 'id' : ''" @update:model-value=" $emit('update:text', value)" :rules="props.isValid ? [(val) => val || 'This field must be entered'] : []
    " :readonly="props.readonly">
      <template v-if="value" v-slot:append>
        <q-icon name="cancel" @click.stop.prevent="value = null" @click="$emit('update:text', value)"
          class="cursor-pointer" />
      </template>
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey"> No results </q-item-section>
        </q-item>
      </template>
    </q-select>
  </div>
</template>
<script setup lang="ts">
import { defineProps, defineEmits, ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';

const emit = defineEmits(['update:text']);
const { locale } = useI18n();

const props = defineProps({
  label: {
    type: String,
    required: false,
  },
  loading: {
    type: Boolean,
    default: false,
  },
  placeholder: {
    type: String,
    default: '',
  },
  color: {
    type: String,
    default: '',
  },
  col: {
    type: String,
    default: '6',
  },
  options: {
    type: Array,
    required: true,
  },
  isMultiple: {
    type: Boolean,
    default: false,
  },
  default: {
    type: String,
    default: '',
  },
  isValid: {
    type: Boolean,
    default: false,
  },
  optionLabel: {
    type: String,
    default: 'name',
  },

  readonly: {
    type: Boolean,
    default: false,
  },
});

const value = ref<string | null>(props.default);
const options = ref(props.options);


</script>
