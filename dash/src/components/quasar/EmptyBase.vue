<template>
  <q-card
    class="q-pa-xl flex column justify-center items-center"
    style="min-height: 350px"
  >
    <q-icon name="warning" size="5rem" class="q-mb-sm" color="primary"></q-icon>
    <div class="text-h6 q-mb-xs">Empty Data</div>
    <div class="text-grey text-center">{{ description }}</div>
  </q-card>
</template>

<script setup>
defineProps({
  description: {
    type: String,
    default: 'No data available',
  },
});
</script>
