<template>
    <q-dialog :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" :model-value="props.modelValue" full-width>
        <form-component :titel="props.edit ? 'تعديل بيانات المتدرب' : 'اضافة متدرب'" @clear:data="clear" @update:data="save"
            :loading="loading.type == 'change' ? loading.value : false">
            <template #content>
                <InputText v-if="!props.file" label="رقم الاكاديمي" :default="request?.academic_number"
                    @update:text="setNumber" type="number" col="6" :isValid="props.edit ? false : true"></InputText>
                <InputText v-if="!props.file" label="اسم المتدرب " :default="request?.full_name" @update:text="setName"
                    col="6" :isValid="props.edit ? false : true"></InputText>
                <InputText v-if="!props.file" label=" رقم الجوال" :default="request?.mobile_number" type="number"
                    @update:text="setPhone" col="6" :isValid="props.edit ? false : true"></InputText>
                <input-select v-if="!props.file" label=" القسم" @update:text="setDep" col="6"
                    :isValid="props.edit ? false : true" :default="request?.department" :options="listDep"
                    optionLabel="department_name"
                    :loading="loadingDep.type == 'list' ? loadingDep.value : false"></input-select>
                <div v-if="props.file" class="q-pa-sm q-mb-sm col-12">
                    <div class="text-subtitle2 text-weight-regular">
                        <span style="
                padding: 0.3rem;
                font-weight: bold;
                color: var(--q-negative);
              ">
                            *
                        </span>
                        ملف معلومات المتدربون
                    </div>
                    <q-file name="cover_files" v-model="files" filled use-chips label="رجاء ادخل ملف excel ">
                        <template v-slot:prepend>
                            <q-icon name="attach_file" />
                        </template>
                    </q-file>
                </div>
            </template>
        </form-component>
    </q-dialog>
</template>
  
<script setup>
import { ref, defineEmits } from 'vue';
import { storeToRefs } from 'pinia';
import * as XLSX from 'xlsx';
import ExcelJS from 'exceljs'
//component
import FormComponent from 'src/components/form/FormComponent.vue';
import InputSelect from 'src/components/formInput/InputSelect.vue';
import InputText from 'src/components/formInput/InputText.vue';
//store
import { useTraineeStore } from 'src/stores/trainees';
import { useDepartmentsStore } from 'src/stores/departments';

const emit = defineEmits(['update:modelValue']);
const props = defineProps({
    modelValue: {
        type: String,
    },
    edit: {
        type: Boolean,
        default: false
    },
    file: {
        type: Boolean,
        default: false
    }
});

const traineesStore = useTraineeStore()
const { request, loading } = storeToRefs(traineesStore)

const departmentsStore = useDepartmentsStore()
const { list: listDep, loading: loadingDep } = storeToRefs(departmentsStore)

const files = ref()

const setName = (val) => {
    request.value.full_name = val
}
const setNumber = (val) => {
    request.value.academic_number = val
}
const setPhone = (val) => {
    request.value.mobile_number = val
}
const setDep = (val) => {
    request.value.department = val?.id || val
}

const save = async () => {
    if (!props.file) {
        !props?.edit ? await traineesStore.addTrainees() : await traineesStore.editTrainees(request.value.id)
    }
    else {
        let fileReader = new FileReader();
        await fileReader.readAsBinaryString(files.value);
        fileReader.onload = async (event) => {
            let fileData = event.target.result;
            let workbook = XLSX.read(
                fileData,
                { type: "binary" }
            );
            workbook.SheetNames.forEach(async (sheet) => {
                const result = await XLSX.utils.sheet_to_json(workbook.Sheets[sheet], {
                    raw: false,
                });
                let fieldNames = Object.keys(result[0]);
                result.shift();
                const jsonObjects = [];
                result.forEach((row) => {
                    const jsonObject = {};
                    fieldNames.forEach((field) => {
                        const key = field.trim().replace(/ /g, '').toLowerCase();
                        jsonObject[key] = row[field];
                    });
                    jsonObjects.push(jsonObject);
                });
                jsonObjects.forEach(async (el) => {
                    request.value = el
                    await traineesStore.addTrainees()
                })
            });
        };
    }
    emit('update:modelValue', false);
    traineesStore.resetRequest()
};

const clear = async () => {
    traineesStore.resetRequest()
    emit('update:modelValue', false);
};
;
</script>
  