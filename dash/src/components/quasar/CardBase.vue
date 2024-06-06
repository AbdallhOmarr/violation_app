<template>
  <q-card
    style="overflow-x: hidden; border-radius: 8px"
    :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'"
  >
    <q-card-section v-if="props.istabs">
      <slot name="header"></slot>
      <q-separator />
    </q-card-section>
    <q-card-section
      v-if="!props.istabs"
      class="flex justify-between items-center w-full"
    >
      <div class="flex items-center">
        <q-avatar
          v-if="props.isIcon"
          :color="!$q.dark.isActive ? `primary` : 'primary'"
          :text-color="props.textColor"
          :icon="props.icon"
          size="3rem"
        ></q-avatar>
        <div>
          <div
            class="text-h6 text-weight-bold q-mx-md"
            :class="!$q.dark.isActive ? `text-primary` : 'text-white'"
          >
            {{ props.titel }}
          </div>
          <div v-if="props.subtitle" class="text-subtitle2 q-mx-md text-grey-6">
            {{ props.subtitle }}
          </div>
        </div>
      </div>
      <div>
        <slot name="btn"></slot>
      </div>
    </q-card-section>
    <q-card-section>
      <slot name="content"></slot>
    </q-card-section>
    <slot name="another"></slot>
  </q-card>
</template>

<script setup lang="ts">
import { watch, ref } from 'vue';
import { storeToRefs } from 'pinia';

const props = defineProps({
  color: {
    type: String,
    default: 'primary',
  },
  textColor: {
    type: String,
    default: 'white',
  },
  icon: {
    type: String,
    default: 'rebase_edit',
  },
  titel: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: false,
  },
  isIcon: {
    type: Boolean,
    default: true,
  },
  width: {
    type: String,
    default: '7vw',
  },
  height: {
    type: String,
    default: '80vh',
  },
  istabs: {
    type: Boolean,
    default: false,
  },
});
</script>
