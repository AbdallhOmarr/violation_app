<template>
  <tab-base title="المدربون" icon="work_outline" @add:data="Add()"> <template #btn><c-btn label="تصدير " class="q-mx-sm"
        icon="file_upload" @click="exportToExcel"></c-btn></template></tab-base>
  <!--table data-->
  <table-base :columns="columns" :rows="list" :items="items"
    :loading-table="loading.type == 'list' ? loading.value : false" :page="false">
  </table-base>
  <AddTech v-model="AddTechTodell" :edit="edit" @hide="() => {
    AddTechTodell = false;
  }
    "></AddTech>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { onMounted, computed, ref } from 'vue';
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';
//store'
import { useTrainerStore } from 'src/stores/trainers';
//component
import TabBase from 'src/components/quasar/TabBase.vue';
import TableBase from 'src/components/quasar/TableBase.vue';
import AddTech from './AddTech.vue';
import CBtn from 'src/components/quasar/CBtn.vue';
;
const AddTechTodell = ref(false)
const edit = ref(false)

const trainersStore = useTrainerStore()
const { loading, list, request } = storeToRefs(trainersStore)

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
      name: 'account_number',
      align: 'center',
      label: 'رقم الحساب',
      field: 'account_number',
    },
    {
      name: 'full_name',
      align: 'center',
      label: 'المدرب',
      field: 'full_name',
    },
    {
      name: 'mobile_number',
      align: 'center',
      label: 'الجوال',
      field: 'mobile_number',
    },
    {
      name: 'status',
      align: 'center',
      label: 'الحالة',
      field: 'status',
      status: true
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
        request.value = {
          id: data.id,
          password: undefined,
          full_name: data?.full_name,
          mobile_number: data?.mobile_number,
          email: data?.email,
          account_number: data?.account_number,
          status: data?.status,
          user_type: data?.user_type == 'Trainer' ? 2 : 1
        }
        edit.value = true
        AddTechTodell.value = true
      },
    },
    {
      icon: 'delete',
      color: 'negative',
      tooltip: 'حذف',
      click: (data) => {
        trainersStore.destroy(data.id)
      },
    },
  ];
});

const Add = () => {
  trainersStore.resetRequest()
  edit.value = false
  AddTechTodell.value = true
}

const exportToExcel = async () => {
  const listData = list.value.map((el) => {
    return {
      م: el.id,
      اسم: el.full_name,
      رقم_الحساب: el.account_number,
      الحالة: el.status,
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
  saveAs(data, `Trainers.xlsx`);
};

onMounted(() => {
  trainersStore.index()
})

</script>
