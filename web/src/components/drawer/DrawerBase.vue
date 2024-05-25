<template>
  <q-drawer show-if-above :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-3'" class="shadow-2 rounded-borders"
    :mini="props.miniState" :side="$i18n.locale == 'en' ? 'left' : 'right'">
    <q-scroll-area style="height: calc(100% - 60px); margin-top: 60px">
      <q-list padding>
        <div style="position: relative">
          <q-item v-for="(list, index) in lists" :key="index" clickable v-ripple active-class="text-warning bg-primary"
            link :to="list?.path.includes('home') ? '/' : list.path">
            <div class="hover-overlay"></div>
            <q-tooltip v-if="props.miniState" transition-show="scale" transition-hide="scale" anchor="center left"
              self="center right" :offset="[10, 10]" class="bg-primary q-pa-sm text-caption">{{ list.label
              }}
            </q-tooltip>

            <q-item-section v-if="list.icon" avatar>
              <q-icon :name="list.icon" :color="(route.fullPath == '/' && list.path.includes('home')) ||
                route.fullPath.includes(list.path)
                ? 'warning' : 'primary'"></q-icon>
            </q-item-section>

            <q-item-section>
              <q-item-label style="margin: 10px">{{ list.label }}
              </q-item-label>
            </q-item-section>
          </q-item>
        </div>
      </q-list>
    </q-scroll-area>

    <div class="absolute-top" style="height: 60px">
      <div v-if="props.miniState" class="flex items-center">
        <q-avatar size="40px" class="q-mx-sm q-mt-sm">
          <q-img src='color__icon.svg' />
        </q-avatar>
      </div>
      <div v-if="!props.miniState" class="flex items-center">
        <div class="col text-h6 text-primary text-italic">
          <q-img src='logoImage.svg' class="q-ma-sm" style="height: 50px; width: 100px;" />
        </div>
        <div class="q-mx-md col-12 text-primary text-italic">
          الكلية التقنية بمحافظة طبرجل
        </div>
      </div>
      <q-separator class="q-mt-sm" />
    </div>
  </q-drawer>
</template>

<script setup lang="ts">
import { defineProps, PropType } from 'vue';
import { useQuasar } from 'quasar';
import { useRoute } from 'vue-router';

const $q = useQuasar();
const route = useRoute();

const props = defineProps({
  lists: {
    type: Array,
  },
  miniState: {
    type: Boolean,
  }
});
</script>

<style scoped>
.hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.hover-overlay:hover {
  background-color: #a3d09d;
  opacity: 0.25;
}
</style>