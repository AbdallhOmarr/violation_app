<template>
    <q-layout>
        <div class="row">
            <div class="col-12 col-md-6 flex items-center justify-center"
                style="height: 100vh; background-image: linear-gradient(to right bottom, #3b7d98, #377f9cd3, #3b7e98be, #3b7e9857, #3b7e9836);">
                <div class="text-h6 text-primary text-italic">
                    <q-img src='logoImage.svg' class="q-ma-sm" style="height: 100px; width: 390px;" />
                    <br>
                    <p class="q-mx-xl">
                        الكلية التقنية بمحافظة طبرجل
                    </p>
                    <p>
                        قواعد تنظيم السلوك والمواظبةللمتدربين
                    </p>
                </div>
            </div>
            <div class=" col-12 col-md-6 flex items-center justify-center" style="height: 100vh;">
                <div class="width-half ">
                    <h4 class="text-h4 text-primary text-center q-my-md">تسجيل دخول</h4>
                    <q-form class="q-pt-md" @submit="submit">
                        <q-input v-model="username" filled label="المستخدم">
                            <template v-slot:prepend>
                                <q-icon name="person" />
                            </template>
                        </q-input>
                        <q-input v-model="password" filled :type="isPwd ? 'password' : 'text'" label="كلمة المرور"
                            class="q-my-md">
                            <template v-slot:prepend>
                                <q-icon name="lock" />
                            </template>
                            <template v-slot:append>
                                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                                    v-on:click="isPwd = !isPwd"></q-icon>
                            </template>
                        </q-input>
                        <q-btn label="دخول" type="submit" :loading="loading" unelevated size="lg" color="primary"
                            class="full-width text-white" @click="submit" />
                    </q-form>

                </div>
            </div>
        </div>
    </q-layout>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useQuasar } from 'quasar';
import { useRouter } from 'vue-router';
import { useAuthStore } from 'src/stores/login';

const router = useRouter()
const $q = useQuasar()

const AuthStore = useAuthStore();
const { authData } = storeToRefs(AuthStore);

const isPwd = ref(true)
const username = ref()
const password = ref()

const loading = ref(false);

const submit = async () => {
    try {
        loading.value = true;
        authData.value.username = username.value
        authData.value.password = password.value
        await AuthStore.login();
    } catch {
    } finally {
        loading.value = false;
    }
};

</script>
  