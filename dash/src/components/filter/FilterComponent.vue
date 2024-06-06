<template>
  <div class="row q-pa-md">
    <c-btn icon="cleaning_services" label="اعادة الضبط" class="q-pa-sm q-mx-sm" size="md" @click="$emit('clear:data')"
      outline></c-btn>
    <c-btn :icon="!openFilter ? 'filter_list_off' : 'filter_list'" :label="!openFilter ? 'فتح الفلتر' : 'اغلاق الفلتر'"
      class="q-pa-sm q-mx-sm" size="md" @click="openFilter = !openFilter"></c-btn>
    <q-space></q-space>
    <q-input v-if="props.search" v-model="value" dense @update:model-value="$emit('search:text', value)"
      input-class="text-right" class="q-ml-md col-4" label="البحث">
      <template v-slot:append>
        <q-icon v-if="value === ''" name="search" />
        <q-icon v-else name="clear" class="cursor-pointer" @click="value = ''" />
      </template>
    </q-input>
  </div>
  <Transition>
    <div v-if="openFilter" class="row q-pa-md">
      <q-expansion-item class="shadow-1 w-full overflow-hidden col" style="border-radius: 20px" icon="filter_alt"
        label="الفلتر" header-class="bg-primary text-white" expand-icon-class="text-white" default-opened>
        <q-card>
          <q-card-section class="row justify-start w-full" style="padding-bottom: 0px"
            :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'">
            <slot name="input"></slot>
          </q-card-section>
          <q-card-actions align="right" style="margin-left: 20px">
            <c-btn label="تطبيق" @click="$emit('apply:data')" :size="md"></c-btn>
          </q-card-actions>
        </q-card>
      </q-expansion-item>
    </div>
  </Transition>
</template>

<script setup>
import { defineProps, ref } from 'vue';
import CBtn from 'src/components/quasar/CBtn.vue';

const openFilter = ref(false);

const props = defineProps({
  default: {
    type: String,
    default: '',
  },
  search: {
    type: Boolean,
    default: false,
  },
});
const value = ref(props.default);
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
