<template>
  <q-btn
    dense
    :data-test="props.color"
    :class="props.mode === 'light' ? `text-primary` : ''"
    :size="props.size"
    unelevated
    :color="props.color"
    padding=".45rem 1.25rem"
    :outline="props.mode === 'outline'"
    icon="more_vert"
    transition-show="scale"
    transition-hide="scale"
  >
    <div
      v-if="props.label"
      style="font-size: 0.8rem"
      class="text-weight-medium text-uppercase"
    >
      {{ props.label }}
    </div>
    <q-menu anchor="bottom left" self="top left" :offset="[0, 5]">
      <q-list>
        <q-item
          v-for="(item, index) in props.items"
          :key="index"
          clickable
          v-ripple
          @click="click(item)"
        >
          <q-item-section avatar>
            <q-icon :name="item?.icon" :color="item.color" />
          </q-item-section>
          <q-item-section>{{ item?.title }}</q-item-section>
        </q-item>
      </q-list>
    </q-menu>
  </q-btn>
</template>
<script setup lang="ts">
import { title } from 'process';
import { defineProps, PropType } from 'vue';

const props = defineProps({
  items: {
    type: Array as PropType<any>,
  },
  data: {
    require: false,
    default: '',
  },
  mode: {
    type: String,
    default: 'normal',
  },
  size: {
    type: String,
    default: '1rem',
  },
  label: {
    type: String,
    required: false,
  },
  color: {
    type: String,
    default: 'primary',
  },
});

const click = (item: any) => {
  item.click(props?.data);
};
</script>
