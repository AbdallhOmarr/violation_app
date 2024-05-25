<template>
    <tab-base title="المخالفات" icon="warning" @add:data="Add()"><template #btn>
            <c-btn label="تصدير " icon="file_upload" @click="exportToExcel"></c-btn>
        </template></tab-base>
    <filter-component @apply:data="filter" @clear:data="clear">
        <template #input>
            <InputSelect label=" المتدرب " col="6" @update:text="setTrainee" :options="listTrainee" optionLabel="full_name"
                :loading="loadingTrainee.type == 'list' ? loadingTrainee.value : false"></InputSelect>
            <InputDate label=" تاريخ ارتكاب المخالفة" col="6" @update:text="setDate"></InputDate>
        </template>
    </filter-component>
    <!--table data-->
    <table-base :columns="columns" :rows="list" :items="items"
        :loading-table="loading.type == 'list' ? loading.value : false" :page="false">
    </table-base>
    <AddWaring v-model="AddWaringToggle" @hide="() => {
        AddWaringToggle = false;
    }" :edit="edit"></AddWaring>
    <DetailsWaringDialog v-model="DetailsWaringToggle" @hide="() => {
        DetailsWaringToggle = false;
    }
        "></DetailsWaringDialog>
</template>
  
<script setup>
import { storeToRefs } from 'pinia';
import { onMounted, computed, ref } from 'vue';
import { date } from 'quasar';
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';
//store'
import { useViolationStore } from 'src/stores/violations';
import { useTraineeStore } from 'src/stores/trainees';
//component
import TabBase from 'src/components/quasar/TabBase.vue';
import TableBase from 'src/components/quasar/TableBase.vue';
import CBtn from 'src/components/quasar/CBtn.vue';
import FilterComponent from 'src/components/filter/FilterComponent.vue';
import InputSelect from 'src/components/formInput/InputSelect.vue';
import DetailsWaringDialog from './DetailsWaringDialog.vue';
import AddWaring from './AddWaring.vue';
import InputDate from 'src/components/formInput/InputDate.vue';

const AddWaringToggle = ref(false)
const DetailsWaringToggle = ref(false)
const edit = ref(false)

const violationStore = useViolationStore()
const { loading, list, request, details } = storeToRefs(violationStore)

const traineesStore = useTraineeStore()
const { list: listTrainee, loading: loadingTrainee } = storeToRefs(traineesStore)

const dateTake = ref()
const trainee = ref()

const setDate = (val) => {
    dateTake.value = date.formatDate(val, 'YYYY-MM-DD')
}
const setTrainee = (val) => {
    trainee.value = val?.id || val
}

const filter = async () => {
    await violationStore.index()
    if (dateTake.value)
        list.value = list.value.filter((el) => el.date == dateTake.value)
    if (trainee.value)
        list.value = list.value.filter((el) => el.trainee == trainee.value)
};

const clear = async () => {
    trainee.value = null
    dateTake.value = null
    await traineesStore.index()
}

const columns = computed(() => {
    return [
        {
            name: 'id',
            align: 'center',
            label: 'م',
            field: 'id',
            sortable: true,
        },
        {
            name: 'trainee_name',
            align: 'center',
            label: 'اسم المتدرب',
            field: 'trainee_name',
        },
        {
            name: 'date',
            align: 'center',
            label: 'تاريخ المخالفة',
            field: 'date',
        },
        {
            name: 'trainer_name',
            align: 'center',
            label: 'معدالمخالفة',
            field: 'trainer_name',
        },
        {
            name: 'degree',
            align: 'center',
            label: 'الدرجة',
            field: 'degree',
        },
        {
            name: 'violation_type',
            align: 'center',
            label: 'النوع',
            field: 'violation_type',
        },

        {
            name: 'action',
            align: 'center',
            label: 'العمليات',
            field: 'action',
        },
    ];
});

const items = computed(() => {
    return [
        {
            icon: 'edit',
            color: 'secondary',
            tooltip: 'تعديل',
            click: async (data) => {
                request.value = { ...data, degree: data.degree, date: date.formatDate(data.date, 'YYYY-MM-DD') }
                await traineesStore.index()
                edit.value = true
                AddWaringToggle.value = true
            },
        },
        {
            icon: 'info',
            color: 'secondary',
            tooltip: 'تفاصيل',
            click: async (data) => {
                DetailsWaringToggle.value = true
                await violationStore.show(data.id)
                details.value = { ...details.value, trainee_name: data.trainee_name, trainer_name: data.trainer_name }
            },
        },
        {
            icon: 'delete',
            color: 'negative',
            tooltip: "حذف",
            click: (data) => {
                violationStore.destroy(data.id)
            },
        },
    ];
});

const Add = async () => {
    violationStore.resetRequest()
    await traineesStore.index()
    edit.value = false
    AddWaringToggle.value = true
}

const exportToExcel = async () => {
    const listData = list.value.map((el) => {
        return {
            المتدرب: el.trainee_name,
            نوع_المخالفة: el.violation_type,
            الدرجة: el.degree,
            معدالمخالفة: el.trainer_name,
            تاريخ: el.date,
            الاجراء_المتخذ: el.taken_procedure,
            تفاصيل_المخالفة: el.violation_details
        }
    })
    const worksheet = XLSX.utils.json_to_sheet(listData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');

    const excelBuffer = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
    const data = new Blob([excelBuffer], {
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    });
    saveAs(data, `Violation.xlsx`);
};

onMounted(() => {
    traineesStore.index()
    violationStore.index()
})
</script>
  