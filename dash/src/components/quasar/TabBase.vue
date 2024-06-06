<template>
  <div class="q-my-md">
    <q-toolbar :class="!$q.dark.isActive ? `text-${props.textColor}` : 'text-white'">
      <q-toolbar-title>
        <q-img v-if="props.icon && props?.isImage" :src="!$q.dark.isActive
          ? `icon/${props.icon}.png`
          : `/icon/${props.icon + 'Dark'}.png`
          " style="height: 40px; max-width: 40px" />
        <q-icon v-if="props.icon && !props?.isImage" :name="props.icon" size="3rem"></q-icon>
        {{ props.title }}
      </q-toolbar-title>
      <c-btn v-if="props.refresh" label="تحديث" icon="loop" class="q-pa-sm q-mx-sm" :size="md"
        @click="refreshPage"></c-btn>
      <q-separator v-if="props.isAdd" vertical inset />

      <slot name="btn"></slot>
      <c-btn v-if="props.isAdd" icon="add" label="اضافة" class="q-pa-sm q-mx-sm" :size="md"
        @click="$emit('add:data')"></c-btn>
    </q-toolbar>
    <q-separator spaced />
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
import CBtn from './CBtn.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const refreshPage = () => {
  router.go(0);
};

const props = defineProps({
  textColor: {
    type: String,
    default: 'secondary',
  },
  isImage: {
    type: Boolean,
    default: false,
  },
  icon: {
    type: String,
    default: 'rebase_edit',
  },
  title: {
    type: String,
  },
  isAdd: {
    type: Boolean,
    default: true,
  },
  refresh: {
    type: Boolean,
    default: true,
  },
});
</script>

<style scoped>
.q-toolbar__title {
  font-size: 30px;
}
</style>
