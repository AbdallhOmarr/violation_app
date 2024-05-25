import { defineStore, storeToRefs } from 'pinia';
import { api } from 'src/boot/axios';
import { sendNotify } from 'src/helper/notify';
import { computed, ref } from 'vue';

export const useTrainerStore = defineStore('trainer', () => {


    const list = ref([]);
    const details = ref();
    const loading = ref({ type: 'list', value: false });

    const request = ref({
        password: undefined,
        full_name: undefined,
        mobile_number: undefined,
        email: undefined,
        account_number: undefined,
        status: false,
        user_type: 2,
    });

    const resetRequest = () => {
        request.value = {
            password: undefined,
            full_name: undefined,
            mobile_number: undefined,
            email: undefined,
            account_number: undefined,
            status: false,
            user_type: 2
        };
    };

    const requestInfo = computed(() => {
        return {
            password: request.value.password,
            is_superuser: request.value.user_type == 1 ? true : false,
            full_name: request.value.full_name,
            mobile_number: request.value.mobile_number,
            email: request.value.email,
            account_number: request.value.account_number,
            status: request.value.status,
            user_type: request.value.user_type == 1 ? 'Superuser' : "Trainer",
            is_staff: true,
            is_trainer: true
        };
    });

    const index = async () => {
        try {
            loading.value = { type: 'list', value: true };
            const res =
                await api.get(`trainers/`)
            list.value = res.data;
        } catch (err) {
        } finally {
            loading.value = { type: 'list', value: false };
        }
    };

    const addTrainers = async () => {
        try {
            loading.value = { type: 'change', value: true };
            await api.post('trainers/', requestInfo.value);
            index()
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const editTrainers = async (id) => {
        try {
            loading.value = { type: 'change', value: true };
            await api.put(`trainers/${id}/`, requestInfo.value);

            index()
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const destroy = async (id) => {
        try {
            loading.value = { type: 'delete', value: true };
            await api.delete(`trainers/${id}/`);

            index()
        } catch (err) {
        } finally {
            loading.value = { type: 'delete', value: false };
        }
    };

    return {
        loading, list, details, request, index, addTrainers, editTrainers, destroy, resetRequest
    };
});
