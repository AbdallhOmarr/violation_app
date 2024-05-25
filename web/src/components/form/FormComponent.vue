<template>
  <HeaderCard :titel="props.titel">
    <template #btn>
      <slot name="btn"> </slot>
    </template>
    <template #content>
      <div>
        <q-form @submit.prevent.stop="$emit('update:data')" @reset="$emit('clear:data')" class="row q-mx-sm">
          <q-inner-loading v-if="props.loadingDetails" showing color="secondary" />
          <slot v-else name="content"> </slot>

          <div class="row">
            <q-separator style="
                max-width: 100vw;
                min-width: 100vw;
                padding: 0px;
                margin: 0px;
              " />
            <div>
              <q-btn v-if="props.showButton" label="حفظ" type="submit" color="secondary" :loading="props.loading"
                class="q-mx-sm q-my-sm" :disable="props.disable" />
              <q-btn label="الغاء" type="reset" color="secondary" flat class="q-mx-sm q-my-sm" v-close-popup />
            </div>
          </div>
        </q-form>
      </div>
    </template>
  </HeaderCard>
</template>

<script setup>
import { watch, ref } from 'vue';
import { storeToRefs } from 'pinia';
import HeaderCard from '../quasar/HeaderCard.vue';

const props = defineProps({
  titel: {
    type: String,
    required: true,
  },
  loading: {
    type: Boolean,
    default: false,
  },
  loadingDetails: {
    type: Boolean,
    default: false,
  },
  disable: {
    type: Boolean,
    default: false,
  },
  showButton: {
    type: Boolean,
    default: true,
  },
});
</script>
