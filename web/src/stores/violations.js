import { defineStore, storeToRefs } from 'pinia';
import { api } from 'src/boot/axios';
import { sendNotify } from 'src/helper/notify';
import { computed, ref } from 'vue';
import { date } from 'quasar';
import { useAuthStore } from './login';
import { useTraineeStore } from './trainees';
import { useTrainerStore } from './trainers';

export const useViolationStore = defineStore('violation', () => {

    const authStore = useAuthStore()
    const { authMe } = storeToRefs(authStore)

    const traineesStore = useTraineeStore()
    const { list: listTrainee, loading: loadingTrainee } = storeToRefs(traineesStore)

    const trainersStore = useTrainerStore()
    const { list: listTrainer, loading: loadingTrainer } = storeToRefs(trainersStore)

    const list = ref([]);
    const details = ref()
    const loading = ref({ type: 'list', value: false });

    const request = ref({
        trainee: undefined,
        date: undefined,
        violation_type: undefined,
        violation_details: undefined,
        taken_procedure: undefined,
        degree: undefined,
    });

    const resetRequest = () => {
        request.value = {
            trainee: undefined,
            date: undefined,
            violation_type: undefined,
            violation_details: undefined,
            taken_procedure: undefined,
            degree: undefined,
        };
    };

    const requestInfo = computed(() => {
        return {
            trainee: request.value.trainee,
            trainer: authMe.value,
            date: date.formatDate(request.value.date, 'YYYY-MM-DD'),
            violation_type: request.value.violation_type,
            violation_details: request.value.violation_details,
            taken_procedure: request.value.taken_procedure,
            degree: request.value.degree,
        };
    });

    const index = async () => {
        try {
            loading.value = { type: 'list', value: true };
            const res =
                await api.get(`violations/`)
            await traineesStore.index()
            await trainersStore.index()
            list.value = res.data.map((el) => { return { ...el, trainer_name: listTrainer.value.filter((elf) => elf.id == el.trainer)[0].full_name, trainee_name: listTrainee.value.filter((elf) => elf.id == el.trainee)[0].full_name } });;
        } catch (err) {
        } finally {
            loading.value = { type: 'list', value: false };
        }
    };

    const show = async (id) => {
        try {
            loading.value = { type: 'details', value: true };
            const res =
                await api.get(`violations/${id}/`)
            details.value = res.data;
        } catch (err) {
        } finally {
            loading.value = { type: 'list', value: false };
        }
    };

    const addViolations = async () => {
        try {
            loading.value = { type: 'change', value: true };
            await api.post('violations/', requestInfo.value);

            index()
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const editViolations = async (id) => {
        try {
            loading.value = { type: 'change', value: true };
            await api.put(`violations/${id}/`, requestInfo.value);

            index();
        } catch (err) {
        } finally {
            loading.value = { type: 'change', value: false };
        }
    };

    const destroy = async (id) => {
        try {
            loading.value = { type: 'delete', value: true };
            await api.delete(`violations/${id}/`);

            index();
        } catch (err) {
        } finally {
            loading.value = { type: 'delete', value: false };
        }
    };

    return {
        loading, details, list, request, index, addViolations, editViolations, destroy, resetRequest, show
    };
});
