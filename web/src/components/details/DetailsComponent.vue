<template>
  <card-base :isIcon="false" icon="info">
    <template #btn>
      <c-btn label="طباعة تعهد " class="q-pa-sm  q-mx-sm" icon="print" :size="md" @click="$emit('print:data')"></c-btn>
      <c-btn label='الغاء المخالفة ' class="q-pa-sm  q-mx-sm" :size="md" @click="$emit('delete:data')"></c-btn>

    </template>
    <template #content>
      <div class="row">

        <q-list v-if="props?.Alldata" bordered separator class="col">
          <q-item v-for="(  data, index  ) in   props.name  " :key="index" v-ripple>
            <q-item-section>{{ data.val }} </q-item-section>
            <q-item-section><q-separator vertical style="height: 100%; margin: 0px; padding: 0px" />
              <span v-if="typeof props?.Alldata?.[data.key] === 'boolean'">
                <q-icon v-if="props?.Alldata?.[data.key]" name="check_circle_outline" color="green" size="md"></q-icon>
                <q-icon v-if="!props?.Alldata?.[data.key]" name="highlight_off" color="red" size="md"></q-icon>
              </span>
              <span v-else>
                {{
                  !props?.Alldata?.[data.key]
                  ? '---'
                  : data.key.includes('date')
                    ? date.formatDate(props?.Alldata?.[data.key], 'YYYY/MM/DD')
                    : props?.Alldata?.[data.key]?.[$i18n.locale]
                      ? props?.Alldata?.[data.key]?.[$i18n.locale]
                      : props?.Alldata?.[data.key]
                }}
              </span>
            </q-item-section>
          </q-item>

          <slot name="details"></slot>
        </q-list>
      </div>
    </template>
  </card-base>
</template>

<script setup>
import CardBase from '../quasar/CardBase.vue';
import CBtn from '../quasar/CBtn.vue';
import { date } from 'quasar';
import { ref } from 'vue';

const props = defineProps({
  titel: {
    type: String,
    required: true,
  },
  Alldata: {
    type: Object,
  },
  loading: {
    type: Object,
  },
  name: {
    type: Array,
  },
});
</script>
