import { defineStore, storeToRefs } from 'pinia';
import { api } from 'src/boot/axios';
import { sendNotify } from 'src/helper/notify';
import { computed, ref } from 'vue';
import { useDepartmentsStore } from './departments';

export const useTraineeStore = defineStore('trainees', () => {

    const departmentsStore = useDepartmentsStore()
    const { list: listDep, loading: loadingDep } = storeToRefs(departmentsStore)

    const list = ref([]);
    const loading = ref({ type: 'list', value: false });

    const request = ref({
        academic_number: undefined,
        full_name: undefined,
        mobile_number: undefined,
        department: undefined,
    });

    const resetRequest = () => {
        request.value = {
            academic_number: undefined,
            full_name: undefined,
            mobile_number: undefined,
            department: undefined,
        };
    };

    const requestInfo = computed(() => {
        return {
            academic_number: request.value.academic_number,
            full_name: request.value.full_name,
            mobile_number: request.value.mobile_number,
            department: request.value.department,
        };
    });

    const index = async () => {
        try {
            loading.value = { type: 'list', value: true };
            await departmentsStore.index()
            const res =
                await api.get(`trainees/`)
            list.value = res.data.map((el) => { return { ...el, department_name: listDep.value.filter((elf) => elf.id == el.department)[0].department_name } });
        } catch (err) {
        } finally {
            loading.value = { type: 'list', value: false };
        }
    };

    const addTrainees = async () => {
        try {
            loading.value = { type: 'change', value: true };
            await api.post('trainees/', requestInfo.value);

            index()
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const editTrainees = async (id) => {
        try {
            loading.value = { type: 'change', value: true };
            await api.put(`trainees/${id}/`, requestInfo.value);
            index();
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const destroy = async (id) => {
        try {
            loading.value = { type: 'delete', value: true };
            await api.delete(`trainees/${id}/`);
            index();
        } catch (err) {
        } finally {
            loading.value = { type: 'delete', value: false };
        }
    };

    return {
        loading, list, request, index, addTrainees, editTrainees, destroy, resetRequest
    };
});
