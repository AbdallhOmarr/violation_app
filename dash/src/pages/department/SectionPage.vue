<template>
    <tab-base title="الاقسام" icon="account_balance" @add:data="Add()">
    </tab-base>
    <!--table data-->
    <table-base :columns="columns" :rows="list" :items="items"
        :loading-table="loading.type == 'list' ? loading.value : false" :page="false">
    </table-base>
    <AddSection v-model="AddDepartment" :edit="edit" @hide="() => {
        AddDepartment = false;
    }
        "></AddSection>
</template>
  
<script setup>
import { useRouter } from 'vue-router';
import { storeToRefs } from 'pinia';
import { onMounted, computed, ref } from 'vue';
import { useI18n } from 'vue-i18n';
//store'
import { useDepartmentsStore } from 'src/stores/departments';
//component
import TabBase from 'src/components/quasar/TabBase.vue';
import TableBase from 'src/components/quasar/TableBase.vue';
import AddSection from './AddSection.vue';

const router = useRouter();
const { t } = useI18n();
const AddDepartment = ref(false)
const edit = ref(false)

const departmentsStore = useDepartmentsStore()
const { list, loading, request } = storeToRefs(departmentsStore)

const columns = computed(() => {
    return [
        {
            name: 'id',
            align: 'center',
            label: 'م',
            field: 'id',
        },
        {
            name: 'department_name',
            align: 'center',
            label: 'القسم',
            field: 'department_name',
        },
        {
            name: 'department_major',
            align: 'center',
            label: 'تخصص',
            field: 'department_major',
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
                request.value = data
                edit.value = true
                AddDepartment.value = true
            },
        },
        {
            icon: 'delete',
            color: 'negative',
            tooltip: t('delete'),
            click: (data) => {
                departmentsStore.destroy(data.id)
            },
        },
    ];
});

const Add = () => {
    departmentsStore.resetRequest()
    AddDepartment.value = true
    edit.value = false
}

onMounted(() => {
    departmentsStore.index()
})
</script>
  