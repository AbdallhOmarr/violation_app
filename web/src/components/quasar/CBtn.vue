<template>
  <q-btn dense :data-test="props.color" :class="props.mode === 'light' ? `text-primary` : ''" :size="props.size"
    unelevated :color="props.color" padding=".45rem 1.25rem" :outline="props.mode === 'outline'" :disable="props.disable">
    <q-icon v-if="props.icon" :name="props.icon" :class="props.label && !$q.dark.isActive ? 'q-px-sm' : 'q-px-sm   text-white'
      "></q-icon>
    <div v-if="props.label" style="font-size: 0.8rem" class="text-weight-medium"
      :class="!$q.dark.isActive ? '' : 'text-capitalize  text-white'">
      {{ props.label }}
    </div>

    <q-tooltip v-if="props.tooltip" :class="`bg-${props.color}`" :offset="[10, 10]">{{ props.tooltip }}</q-tooltip>
    <slot></slot>
  </q-btn>
</template>

<script setup lang="ts">
const props = defineProps({
  mode: {
    type: String,
    default: 'normal',
  },
  size: {
    type: String,
    default: '1rem',
  },
  icon: {
    type: String,
    required: false,
  },
  label: {
    type: String,
    required: false,
  },
  color: {
    type: String,
    default: 'secondary',
  },
  uppercase: {
    type: Boolean,
    default: false,
  },
  tooltip: {
    type: String,
    default: '',
  },
  disable: {
    type: Boolean,
    default: false,
  },
});
</script>
