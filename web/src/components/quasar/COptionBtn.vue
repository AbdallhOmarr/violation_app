<template>
  <c-btn
    :class="selected ? 'opacity-50' : 'opacity-100'"
    :size="size"
    :style="`height: ${heightValue}`"
  >
    <div class="flex column items-center">
      <q-icon :color="iconColor" :name="icon" :size="iconSize"></q-icon>
      <div
        v-if="label"
        class="text-subtitle1 text-weight-medium q-mt-xs"
        :class="
          size == 'md' ? 'text-subtitle1' : size == 'sm' ? 'text-caption' : ''
        "
      >
        {{ label }}
        <div class="q-mt-xs">
          <slot name="subtitle"></slot>
        </div>
      </div>
    </div>
    <q-tooltip v-if="tooltip">{{ tooltip }}</q-tooltip>
    <div
      v-if="selected && selectedType == 'check'"
      class="option-btn-selected flex column justify-center items-center"
    >
      <q-avatar color="grey-6" icon="check"></q-avatar>
    </div>
  </c-btn>
</template>

<script setup>
import CBtn from './CBtn.vue';

defineProps({
  selected: {
    type: Boolean,
    default: false,
  },
  selectedType: {
    type: String,
    default: 'normal',
  },
  label: {
    type: String,
    default: '',
  },
  icon: {
    type: String,
    default: '',
  },
  size: {
    type: String,
    default: 'sm',
  },
  iconSize: {
    type: String,
    default: 'sm',
  },
  iconColor: {
    type: String,
    default: 'white',
  },
  heightValue: {
    type: String,
    default: '7rem',
  },
  tooltip: {
    type: String,
    required: false,
  },
  verticle: {
    type: Boolean,
    default: true,
  },
});
</script>

<style scoped>
.option-btn-selected {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
