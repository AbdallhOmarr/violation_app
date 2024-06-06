<template>
    <tab-base title="نظام مخالفات المتدربين" icon="warning" :isAdd="false"><template #btn>
            <c-btn label="تصدير " icon="file_upload" @click="exportToExcel"></c-btn>
        </template></tab-base>
    <div class="row q-pa-md">
        <q-expansion-item class="shadow-1 w-full overflow-hidden col" style="border-radius: 20px" icon="filter_alt" label=""
            header-class="bg-primary text-white" expand-icon-class="text-white" default-opened>
            <div class="row bg-white">
                <div class="col-6">
                    <q-list dense bordered class="rounded-borders q-ma-md" style="height: 300px;">
                        <q-item-label header>ادارة</q-item-label>
                        <q-item>
                            <q-item-section>
                                <InputText label="رقم الاكاديمي" @update:text="setTrainee" type="number" col="6">
                                </InputText>
                            </q-item-section>
                        </q-item>
                        <q-item class="q-ma-md">
                            <q-item-section>
                                <c-btn class="q-mx-md" label="استعلام" @click="filter('filter')" :size="md"></c-btn>
                            </q-item-section><q-item-section>
                                <c-btn v-if="detailsTrainer?.is_superuser" label="ادخال مخالفة" @click="filter('add')"
                                    :size="md"></c-btn>
                            </q-item-section>
                        </q-item>
                    </q-list>
                </div>
                <div class="col-6">
                    <q-list dense bordered class="rounded-borders q-ma-md" style="height: 300px;">
                        <q-item-label header>بيانات المتدرب المختار</q-item-label>
                        <q-item>
                            <q-item-section>
                                <div class="q-pa-sm q-mb-sm">
                                    <div class="text-subtitle2 text-weight-regular">
                                        اسم المتدرب
                                    </div>
                                    <div
                                        style="border: 1px dashed black; padding: 15px; background: rgb(240, 239, 239);text">
                                        {{ trainee?.full_name }}
                                    </div>
                                </div>
                            </q-item-section>
                        </q-item>
                        <q-item>
                            <q-item-section>
                                <div class="q-pa-sm q-mb-sm">
                                    <div class="text-subtitle2 text-weight-regular">
                                        القسم
                                    </div>
                                    <div
                                        style="border: 1px dashed black; padding: 15px; background: rgb(240, 239, 239);text">
                                        {{ trainee?.department_name }}
                                    </div>
                                </div>
                            </q-item-section>
                        </q-item>

                    </q-list>
                </div>
            </div>
        </q-expansion-item>
    </div>
    <!--table data-->
    <table-base v-if="show" :columns="columns" :rows="list" :items="detailsTrainer?.is_superuser ? items : itemsTraner"
        :loading-table="loading.type == 'change' ? loading.value : false" :page="false">
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
import { Loading } from 'quasar';
//store'
import { useViolationStore } from 'src/stores/violations';
import { useTraineeStore } from 'src/stores/trainees';
//component
import TabBase from 'src/components/quasar/TabBase.vue';
import TableBase from 'src/components/quasar/TableBase.vue';
import CBtn from 'src/components/quasar/CBtn.vue';
import DetailsWaringDialog from './DetailsWaringDialog.vue';
import AddWaring from './AddWaring.vue';
import InputText from 'src/components/formInput/InputText.vue';
import { useAuthStore } from 'src/stores/login';
import { useTrainerStore } from 'src/stores/trainers';

const AddWaringToggle = ref(false)
const DetailsWaringToggle = ref(false)
const edit = ref(false)
const show = ref(false)

const violationStore = useViolationStore()
const { loading, list, request, details } = storeToRefs(violationStore)

const traineesStore = useTraineeStore()
const { list: listTrainee, loading: loadingTrainee, details: detailsTrainee } = storeToRefs(traineesStore)

const AuthStore = useAuthStore()
const { authMe } = storeToRefs(AuthStore)

const trainersStore = useTrainerStore()
const { details: detailsTrainer } = storeToRefs(trainersStore)

const hijriDateFormatter = new Intl.DateTimeFormat('en-US-u-ca-islamic', {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric'
});

const trainee = ref()
const academicNumber = ref

const setTrainee = (val) => {
    academicNumber.value = val
}

const filter = async (add) => {
    Loading.show();
    await violationStore.index()
    if (academicNumber.value) {
        await traineesStore.index()
        listTrainee.value = listTrainee.value.filter((el) => el.academic_number == academicNumber.value)
        trainee.value = listTrainee.value?.length > 0 ? listTrainee.value[0] : null
        list.value = listTrainee.value?.length > 0 ? list.value.filter((el) => el.trainee == trainee.value?.id) : []
        list.value?.length > 0 ? show.value = true : show.value = false
    }
    else { show.value = false }
    if (add == "add") {
        violationStore.resetRequest()
        const currentDate = new Date();
        const hijriDate = hijriDateFormatter.format(currentDate).substring(6, 10) + '-' + hijriDateFormatter.format(currentDate).substring(0, 2) + '-' + hijriDateFormatter.format(currentDate).substring(3, 5);
        console.log(hijriDate.fullYear)
        request.value.date = hijriDate
        await traineesStore.index()
        edit.value = false
        request.value.trainee = trainee.value?.id
        AddWaringToggle.value = true
        show.value = true
    }

    Loading.hide();
};


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
            name: 'violation_type',
            align: 'center',
            label: 'المخالفة',
            field: 'violation_type',
        },
        {
            name: 'degree',
            align: 'center',
            label: 'الدرجة',
            field: 'degree',
            sortable: true,
        },
        {
            name: 'date',
            align: 'center',
            label: 'تاريخ المخالفة',
            field: 'date',
            sortable: true,
        },
        {
            name: 'trainer_name',
            align: 'center',
            label: 'مدخل المخالفة',
            field: 'trainer_name',
        },
        {
            name: 'action',
            align: 'center',
            label: 'تحديث البيانات',
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
                violationStore.destroy(data.id, trainee.value?.id)
            },
        },
    ];
});

const itemsTraner = computed(() => {
    return [
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
    ];
});


const exportToExcel = async () => {
    const listData = list.value.map((el) => {
        return {
            المتدرب: el.trainee_name,
            نوع_المخالفة: el.violation_type,
            الدرجة: el.degree,
            معدالمخالفة: el.trainer_name,
            تاريخ: el.date,
            ملاحظات_المخالفة: el.violation_details
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

onMounted(async () => {
    Loading.show()
    await AuthStore.getMe()
    await trainersStore.show(Number(authMe.value))
    traineesStore.index()
    violationStore.index()
    Loading.hide()
})
</script>
  