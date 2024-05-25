<template>
    <q-dialog :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" :model-value="props.modelValue">
        <form-component titel="أضافة قسم" @clear:data="clear" @update:data="save"
            :loading="loading.type == 'change' ? loading.value : false">
            <template #content>
                <InputText label="اسم القسم" @update:text="setName" col="12" :isValid="true"></InputText>
            </template>
        </form-component>
    </q-dialog>
</template>
  
<script setup>
import { defineEmits } from 'vue';
import { storeToRefs } from 'pinia';
//component
import FormComponent from 'src/components/form/FormComponent.vue';
import InputText from 'src/components/formInput/InputText.vue';
//store
import { useDepartmentsStore } from 'src/stores/departments';

const emit = defineEmits(['update:modelValue']);
const props = defineProps({
    modelValue: {
        type: String,
    },
});

const departmentsStore = useDepartmentsStore()
const { request, loading } = storeToRefs(departmentsStore)

const setName = (val) => {
    request.value.department_name = val
}

const save = async () => {
    await departmentsStore.addDepartments()
    emit('update:modelValue', false);
    departmentsStore.resetRequest()
};

const clear = async () => {
    departmentsStore.resetRequest()
    emit('update:modelValue', false);
};
;
</script>
  