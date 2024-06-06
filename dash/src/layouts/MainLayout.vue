<template>
  <q-layout view="lHr Lpr lFf" :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" class="shadow-2 rounded-borders"
    :class="$q.dark.isActive ? 'bg-dark' : 'bg-info'">
    <!-- navebar -->
    <q-header elevated>
      <q-toolbar>
        <q-btn flat @click="miniState = !miniState" round dense icon="menu" />
        <q-space></q-space>
        <q-btn class="q-mr-xs" flat round @click="() => {
          $q.dark.toggle();
        }
          " :icon="$q.dark.isActive ? 'wb_sunny' : 'nights_stay'" />

        <!-- start user logout -->
        <div>
          <q-btn icon="logout" size="md" flat class="w-full" @click="logout()"></q-btn>
        </div>
        <!-- end user logout -->
      </q-toolbar>
    </q-header>

    <!-- drawer -->
    <DrawerBase v-if="list.filter(
      (el) =>
        el.permission == 'all' ||
        details?.user_type == el.permission)?.length > 0
      " :lists="list.filter(
    (el) =>
      el.permission == 'all' ||
      details?.user_type == el.permission
  )
    " :miniState="miniState"></DrawerBase>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { list } from './drawerList';
import { ref, onMounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { useAuthStore } from 'src/stores/login';
import { useTrainerStore } from 'src/stores/trainers';
import { storeToRefs } from 'pinia';
import { useRoute, useRouter } from 'vue-router';
//component
import DrawerBase from 'src/components/drawer/DrawerBase.vue';
import { Cookies } from 'quasar';

const AuthStore = useAuthStore();
const { authMe } = storeToRefs(AuthStore)

const trainersStore = useTrainerStore()
const { details, loading: loadingTrainee } = storeToRefs(trainersStore)

const { locale } = useI18n();
const router = useRouter();

const miniState = ref(true);

const logout = () => {
  router.push('/login');
  Cookies.remove('access_token')
  Cookies.remove('me');
};

onMounted(async () => {
  await AuthStore.getMe()
  trainersStore.show(Number(authMe.value))
})

</script>

<style>
body {
  background-color: var(--q-info) !important;
  font-family: 'Poppins', 'Almarai', 'sans-serif';
}
</style>
