<template>
  <div class="row justify-center q-mt-sm q-mb-md">
    <q-pagination
      v-model="paginationParama"
      @update:model-value="$emit('update:page', paginationParama)"
      color="grey"
      active-color="primary"
      :max="props.pagesNumber"
      boundary-numbers
      size="sm"
    />
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, computed, PropType } from 'vue';

const emit = defineEmits(['update:page']);

const props = defineProps({
  pageNo: {
    type: Number,
    default: 1,
  },
  pagesNumber: {
    type: Number,
    default: 2,
  },
});
const paginationParama = ref(props.pageNo);
</script>
