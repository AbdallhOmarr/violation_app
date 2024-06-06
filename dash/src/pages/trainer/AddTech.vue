<template>
    <q-dialog :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" :model-value="props.modelValue" full-width>
        <form-component :titel="props.edit ? 'تعديل بيانات المدرب' : 'اضافة مدرب'" @clear:data="clear" @update:data="save"
            :loading="loading.type == 'change' ? loading.value : false">
            <template #content>
                <InputText label="رقم الحساب" type="number" @update:text="setNumber" :default="request?.account_number"
                    col="6" :isValid="true"></InputText>
                <InputText label="اسم المدرب " @update:text="setName" col="6" :default="request?.full_name" :isValid="true">
                </InputText>
                <InputText label="رقم الجوال" type="number" @update:text="setPhone" :default="request?.mobile_number"
                    col="6" :isValid="true"></InputText>
                <InputText label=" كلمة المرور" type="password" @update:text="setPass" :default="request?.password" col="6"
                    :isValid="true">
                </InputText>
                <InputText label="  البريد الالكتروني" type="email" @update:text="setEmail" :default="request?.email"
                    col="6" :isValid="true">
                </InputText>
                <input-select label=" الصلاحيات" @update:text="setUserType" :default="request?.user_type" col="6"
                    :isValid="true" :options="userType" optionLabel="name"></input-select>
                <CheckBox :default="request?.status" label="حالة المدرب" @update:check="setStatus" col="4"
                    style="margin-top: 20px"></CheckBox>
            </template>
        </form-component>
    </q-dialog>
</template>
  
<script setup>
import { ref, defineEmits } from 'vue';
import { storeToRefs } from 'pinia';
//store
import { useTrainerStore } from 'src/stores/trainers';
//component
import FormComponent from 'src/components/form/FormComponent.vue';
import InputSelect from 'src/components/formInput/InputSelect.vue';
import InputText from 'src/components/formInput/InputText.vue';
import CheckBox from 'src/components/formInput/CheckBox.vue';
//const

const emit = defineEmits(['update:modelValue']);
const props = defineProps({
    modelValue: {
        type: String,
    },
    edit: {
        type: Boolean,
        default: false
    }
});

const trainersStore = useTrainerStore()
const { loading, request } = storeToRefs(trainersStore)

const userType = [{ id: 1, name: 'Superuser' }, { id: 2, name: 'Trainer' }]

const setPhone = (val) => {
    request.value.mobile_number = val
}
const setName = (val) => {
    request.value.full_name = val
}
const setNumber = (val) => {
    request.value.account_number = val
}
const setStatus = (val) => {
    request.value.status = val
}
const setPass = (val) => {
    request.value.password = val
}
const setEmail = (val) => {
    request.value.email = val
}
const setUserType = (val) => {
    request.value.user_type = val?.id || val
}

const save = async () => {
    props?.edit ? await trainersStore.editTrainers(request.value.id) : await trainersStore.addTrainers()
    emit('update:modelValue', false);
    trainersStore.resetRequest()
};

const clear = async () => {
    trainersStore.resetRequest()
    emit('update:modelValue', false);
};
;
</script>
  