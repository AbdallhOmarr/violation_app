import { defineStore, storeToRefs } from 'pinia';
import { api } from 'src/boot/axios';
import { sendNotify } from 'src/helper/notify';
import { computed, ref } from 'vue';

export const useDepartmentsStore = defineStore('departments', () => {


    const list = ref([]);
    const loading = ref({ type: 'list', value: false });

    const request = ref({ department_name: undefined });

    const resetRequest = () => {
        request.value = { department_name: undefined };
    };

    const requestInfo = computed(() => {
        return { department_name: request.value.department_name };
    });

    const index = async () => {
        try {
            loading.value = { type: 'list', value: true };
            const res =
                await api.get(`departments/`)
            list.value = res.data;
        } catch (err) {
        } finally {
            loading.value = { type: 'list', value: false };
        }
    };

    const addDepartments = async () => {
        try {
            loading.value = { type: 'change', value: true };
            await api.post('departments/', requestInfo.value);

            index()
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const destroy = async (id) => {
        try {
            loading.value = { type: 'delete', value: true };
            await api.delete(`departments/${id}/`);

            index();
        } catch (err) {
        } finally {
            loading.value = { type: 'delete', value: false };
        }
    };

    return {
        loading, list, request, index, addDepartments, destroy, resetRequest
    };
});
