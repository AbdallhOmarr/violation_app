import { defineStore, storeToRefs } from 'pinia';
import { api } from 'src/boot/axios';
import { ref } from 'vue';
import { Cookies } from 'quasar';
import { useRouter } from 'vue-router';
import { useTrainerStore } from './trainers';

export const useAuthStore = defineStore('auth', () => {

    const trainerStore = useTrainerStore()
    const { list } = storeToRefs(trainerStore)

    const authData = ref({
        username: null,
        password: null,
    });
    const authMe = ref()

    const router = useRouter()

    const login = async () => {
        try {
            const res = await api.post('token/', authData.value);

            if (res?.data) {
                const token = res?.data?.token;
                await trainerStore.index()
                const me = list.value.filter((el) => el.account_number == authData.value.username)?.[0]?.id
                Cookies.set('access_token', token);
                Cookies.set('me', me);
                api.defaults.headers.common['Authorization'] = `Token ${token}`;
                router.push('/');
            }
        } catch (err) {
            Cookies.remove('access_token');
            Cookies.remove('me');
        }
    };

    const getMe = () => {
        authMe.value = Cookies.get('me');
    }


    return {
        login,
        authData,
        getMe, authMe
    };
});
