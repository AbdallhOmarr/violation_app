<template>
  <q-item
    clickable
    v-ripple
    class="rounded-borders col-12 q-my-sm"
    :style="`border: 1px solid ${props.color}`"
    :class="`bg-${props.color}-1 text-grey-7`"
  >
    <q-item-section avatar>
      <q-avatar rounded>
        <q-icon name="warning" :color="props.color" size="lg" class="q-ml-xs" />
      </q-avatar>
    </q-item-section>

    <q-item-section>
      <q-item-label> {{ props.label }} </q-item-label>
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
import { defineProps, PropType } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: false,
  },
  color: {
    type: String,
    default: 'red',
  },
});
</script>
