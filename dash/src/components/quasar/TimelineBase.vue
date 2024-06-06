<template>
  <q-timeline
    v-if="props?.data"
    layout="dense"
    class="q-pa-md"
    :side="$i18n.locale == 'en' ? ' right' : 'left'"
  >
    <q-timeline-entry
      v-for="(item, index) in props?.data"
      :key="index"
      :subtitle="moment(item?.create_date).format('MMMM D , YYYY')"
      :icon="item?.icon"
      :color="item?.color"
      side="right"
    >
      <q-card
        class="card-law"
        :style="`border-left : 10px ${item?.color} solid  ;margin-left:${
          $i18n.locale == 'en' ? '40px' : '0px'
        } `"
        ><q-card-section>
          <div class="row items-center no-wrap">
            <div class="col">
              <div class="text-h6">
                {{ props?.name?.[$i18n.locale] }}
              </div>
            </div>
            <div class="col-auto">
              <q-chip
                v-for="(tag, index) in item.data"
                :key="index"
                square
                :color="tag?.color"
                text-color="white"
              >
                {{ tag?.data }}
              </q-chip>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </q-timeline-entry>
  </q-timeline>
  <empty-base v-else></empty-base>
</template>

<script setup>
import { ref } from 'vue';
import moment from 'moment';
import EmptyBase from './EmptyBase.vue';

const props = defineProps({
  data: {
    type: Array,
  },
  name: {
    type: Object,
  },
});
</script>

<style scoped>
.card-law:hover {
  cursor: pointer;
  transform: translateY(-0.35em);
  box-shadow: 0 0.5em 0.5em -0.4em #000;
}
</style>
<style>
.q-timeline__subtitle {
  margin-left: 40px !important;
}
</style>
