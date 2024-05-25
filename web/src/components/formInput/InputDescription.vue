<template>
  <div :class="`col-${props.col}`" class="q-pa-sm q-mb-sm">
    <div v-if="props.label" class="text-subtitle2 text-weight-regular">
      {{ props.label }}
    </div>
    <q-editor toolbar-text-color="white" toolbar-toggle-color="yellow-8" toolbar-bg="primary" class="q-mb-md w-full"
      v-model="value" @update:model-value="$emit('update:text', value)" :dense="$q.screen.lt.md" :toolbar="[
        [
          {
            label: $q.lang.editor.align,
            icon: $q.iconSet.editor.align,
            fixedLabel: true,
            options: ['left', 'center', 'right', 'justify'],
          },
        ],
        ['bold', 'italic', 'strike', 'underline', 'subscript', 'superscript'],
        [
          {
            label: $q.lang.editor.formatting,
            icon: $q.iconSet.editor.formatting,
            list: 'no-icons',
            options: ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code'],
          },
          {
            label: $q.lang.editor.fontSize,
            icon: $q.iconSet.editor.fontSize,
            fixedLabel: true,
            fixedIcon: true,
            list: 'no-icons',
            options: [
              'size-1',
              'size-2',
              'size-3',
              'size-4',
              'size-5',
              'size-6',
              'size-7',
            ],
          },
          {
            label: $q.lang.editor.defaultFont,
            icon: $q.iconSet.editor.font,
            fixedIcon: true,
            list: 'no-icons',
            options: [
              'default_font',
              'arial',
              'arial_black',
              'comic_sans',
              'courier_new',
              'impact',
              'lucida_grande',
              'times_new_roman',
              'verdana',
            ],
          },
          'removeFormat',
        ],
        ['quote', 'unordered', 'ordered', 'outdent', 'indent'],

        ['undo', 'redo'],
      ]" :fonts="{
  arial: 'Arial',
  arial_black: 'Arial Black',
  comic_sans: 'Comic Sans MS',
  courier_new: 'Courier New',
  impact: 'Impact',
  lucida_grande: 'Lucida Grande',
  times_new_roman: 'Times New Roman',
  verdana: 'Verdana',
}" />
  </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { defineProps, defineEmits, ref } from 'vue';

const emit = defineEmits(['update:text']);
const props = defineProps({
  col: {
    type: String,
    default: '6',
  },
  label: {
    type: String,
    required: false,
  },
  default: {
    type: String,
    default: '',
  },
});
const value = ref(props.default);
const $q = useQuasar();
</script>
