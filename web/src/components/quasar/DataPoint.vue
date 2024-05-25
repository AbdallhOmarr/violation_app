<template>
  <div v-if="props?.data" class="col-4 q-pa-md">
    <q-card class="q-pa-sm" style="height: 100%">
      <div class="flex no-wrap">
        <q-avatar :icon="props.icon" color="primary" size="2.5rem" class="text-white"></q-avatar>
        <div class="flex no-wrap column q-px-sm q-pt-sm">
          <div class="text-weight-bold text-h6" :class="!$q.dark.isActive ? `text-grey-9` : 'text-white'">
            {{ props?.nameDatapoint }}
          </div>
        </div>
      </div>
      <div class="flex justify-center">
        <div class="flex column items-center q-px-sm q-pt-sm">
          <div class="text-weight-bold text-h4" :class="`text-${color[0]}-5`">
            {{
              props?.data
            }}
          </div>
        </div>
      </div>
    </q-card>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { storeToRefs } from 'pinia';

const props = defineProps({
  data: {
    type: Number,
  },

  nameDatapoint: {
    type: String,
  },
  icon: {
    type: String,
    default: 'category',
  },
});
const color = ['red', 'blue', 'teal', 'green', 'orange'];
</script>
