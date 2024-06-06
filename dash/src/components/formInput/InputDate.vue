<template>
  <div :class="`col-${props.col}`" class="q-pa-md q-m-sm">
    <div v-if="props.label" class="text-subtitle2 text-weight-regular">
      {{ props.label }}
    </div>
    <q-input filled v-model="value" @update:model-value="$emit('update:text', value)"
      :label="props.placeholder ? props.placeholder : ''">
      <template v-if="props.isDate" v-slot:prepend>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-date v-model="value" :mask="props.format" :locale="myLocale"
              @update:model-value="$emit('update:text', value)">
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref } from 'vue';

const myLocale = {
  /* starting with Sunday */
  months:
    'محرم - صفر - ربيع الأول - ربيع الثاني - جمادى الأولى - جمادى الثانية - رجب - شعبان - رمضان - شوال - ذو القعدة - ذو الحجة'.split(
      '-'
    ),
  monthsShort:
    'محرم - صفر - ربيع الأول - ربيع الثاني - جمادى الأولى - جمادى الثانية - رجب - شعبان - رمضان - شوال - ذو القعدة - ذو الحجة'.split(
      '-'
    ),
  firstDayOfWeek: 1, // 0-6, 0 - Sunday, 1 Monday, ...
  format24h: true,
  pluralDay: 'dias',
};


const emit = defineEmits(['update:text']);
const props = defineProps({
  isTime: {
    type: Boolean,
    default: false,
  },
  isDate: {
    type: Boolean,
    default: true,
  },
  col: {
    type: String,
    default: '6',
  },
  format: {
    type: String,
    default: 'YYYY-MM-DD',
  },
  label: {
    type: String,
    required: false,
  },
  placeholder: {
    type: String,
    default: '',
  },
  default: {
    type: String,
    default: '',
  },
});

const value = ref(props.default);
</script>
