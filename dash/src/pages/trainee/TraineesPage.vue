<template>
    <tab-base title="المتدربون" icon="perm_identity" @add:data="Add()"><template #btn>
            <c-btn label="اسنيراد الاسماء" @click="() => {
                file = true
                AddTraineeToggel = true
                edit = false
            }"></c-btn>
            <c-btn label="تصدير " class="q-mx-sm" icon="file_upload" @click="exportToExcel"></c-btn>
        </template></tab-base>
    <filter-component @apply:data="filter" @clear:data="clear">
        <template #input>
            <input-select label=" القسم" @update:text="setDep" col="6" :options="listDep" optionLabel="department_name"
                :loading="loadingDep.type == 'list' ? loadingDep.value : false"></input-select>
        </template>
    </filter-component>
    <!--table data-->
    <table-base :columns="columns" :rows="list" :items="items"
        :loading-table="loading.type == 'list' ? loading.value : false" :page="false">
    </table-base>
    <AddTrainee v-model="AddTraineeToggel" @hide="() => {
        AddTraineeToggel = false;
    }" :edit="edit" :file="file"></AddTrainee>
</template>
  
<script setup>
import { storeToRefs } from 'pinia';
import { onMounted, computed, ref } from 'vue';
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';
//store'
import { useTraineeStore } from 'src/stores/trainees';
import { useDepartmentsStore } from 'src/stores/departments';
//component
import TabBase from 'src/components/quasar/TabBase.vue';
import TableBase from 'src/components/quasar/TableBase.vue';
import CBtn from 'src/components/quasar/CBtn.vue';
import FilterComponent from 'src/components/filter/FilterComponent.vue';
import InputSelect from 'src/components/formInput/InputSelect.vue';
import AddTrainee from './AddTrainee.vue';

const edit = ref(false)
const file = ref(false)
const AddTraineeToggel = ref(false)
const department = ref('')

const traineesStore = useTraineeStore()
const { loading, list, request } = storeToRefs(traineesStore)

const departmentsStore = useDepartmentsStore()
const { list: listDep, loading: loadingDep } = storeToRefs(departmentsStore)

const setDep = (val) => {
    department.value = val?.id || val
}

const filter = async () => {
    await traineesStore.index()
    list.value = list.value.filter((el) => el.department == department.value)
};

const clear = async () => {
    department.value = null
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
            name: 'academic_number',
            align: 'center',
            label: 'رقم الاكاديمي',
            field: 'academic_number',
        },
        {
            name: 'full_name',
            align: 'center',
            label: 'المتدرب',
            field: 'full_name',
        },
        {
            name: 'department_name',
            align: 'center',
            label: 'القسم',
            field: 'department_name',
        },
        {
            name: 'mobile_number',
            align: 'center',
            label: 'رقم الجوال',
            field: 'mobile_number',
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
                await departmentsStore.index()
                request.value = data
                edit.value = true
                file.value = false
                AddTraineeToggel.value = true
            },
        },
        {
            icon: 'delete',
            color: 'negative',
            tooltip: 'حذف',
            click: (data) => {
                traineesStore.destroy(data.id)
            },
        },
    ];
});

const Add = async () => {
    traineesStore.resetRequest()
    await departmentsStore.index()
    edit.value = false
    file.value = false
    AddTraineeToggel.value = true
}

onMounted(async () => {
    traineesStore.index()
    departmentsStore.index()

})

const exportToExcel = async () => {
    const listData = list.value.map((el) => {
        return {
            م: el.id,
            اسم: el.full_name,
            الاكاديمي_الرقم: el.academic_number,
            القسم: el.department_name,
            الجوال: el.mobile_number,
        }
    })
    const worksheet = XLSX.utils.json_to_sheet(listData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');

    const excelBuffer = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
    const data = new Blob([excelBuffer], {
        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    });
    saveAs(data, `Trainees.xlsx`);
};
</script>
  