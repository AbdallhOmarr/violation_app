<template>
  <q-card style="overflow-x: hidden; border-radius: 8px">
    <!--header-->
    <div class="flex justify-between items-center w-full q-pa-sm">
      <div class="flex items-center">
        <q-avatar v-if="props.isIcon" color="secondary" :text-color="props.textColor" :icon="props.icon"
          size="3rem"></q-avatar>
        <div>
          <div :class="`${props?.titel ? 'text-h6' : 'text-subtitle2'} ${!$q.dark.isActive ? 'text-secondary' : 'text-white'
            }`" class="text-weight-bold q-mx-md">
            {{ props.titel ? props.titel : props.titel2 }}
          </div>
          <div v-if="props.subtitle" class="text-subtitle2 q-mx-md text-grey-6">
            {{ props.subtitle }}
          </div>
        </div>
      </div>
      <div>
        <slot name="btn"></slot>
      </div>
    </div>

    <q-separator style="max-width: 100vw; min-width: 75vw; padding: 0px; margin: 0px" />
    <!--end header-->
    <slot name="content"></slot>
  </q-card>
</template>

<script setup lang="ts">
import { watch, ref } from 'vue';
import { storeToRefs } from 'pinia';

const props = defineProps({
  color: {
    type: String,
    default: 'secondary',
  },
  textColor: {
    type: String,
    default: 'white',
  },
  icon: {
    type: String,
    default: 'edit',
  },
  titel: {
    type: String,
    required: false,
  },
  subtitle: {
    type: String,
    required: false,
  },
  isIcon: {
    type: Boolean,
    default: true,
  },
  titel2: {
    type: String,
    required: false,
  },
});
</script>
