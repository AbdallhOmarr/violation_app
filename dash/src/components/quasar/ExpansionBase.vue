<template>
  <div class="q-pa-md">
    <!--time line -->
    <q-expansion-item
      @click="active = !active"
      class="shadow-1 overflow-hidden"
      :label="props.label"
      :default-opened="props.default"
      :header-class="
        !active
          ? 'bg-white text-primary text-h6 text-weight-bold'
          : 'bg-primary text-white text-h6 text-weight-bold'
      "
      :expand-icon-class="!active ? 'text-black' : 'text-white'"
    >
      <slot name="Data"></slot>
    </q-expansion-item>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: false,
  },
  default: {
    type: Boolean,
    default: false,
  },
});
const active = ref(props.default);
</script>
