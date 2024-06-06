<template>
    <div class="q-pa-md">
        <form-component titel="الاعدادت" :loadingDetails="loadingDetails" :showCanselButton="false" icon="settings"
            :loading="loading.type == 'change' ? loading.value : false" @update:data="save">
            <template #content>
                <InputText :readonly="true" label="رقم الحساب" type="number" @update:text="setNumber"
                    :default="request?.account_number" col="6" :isValid="true"></InputText>
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
            </template>
        </form-component>
    </div>
</template>
  
<script setup>
import { ref, defineEmits, onMounted } from 'vue';
import { storeToRefs } from 'pinia';
//store
import { useTrainerStore } from 'src/stores/trainers';
//component
import FormComponent from 'src/components/form/FormComponent.vue';
import InputText from 'src/components/formInput/InputText.vue';
import { useAuthStore } from 'src/stores/login';
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

const loadingDetails = ref(true)

const trainersStore = useTrainerStore()
const { loading, request, details } = storeToRefs(trainersStore)

const AuthStore = useAuthStore();
const { authMe } = storeToRefs(AuthStore)

const userType = [{ id: 1, name: 'Superuser' }, { id: 2, name: 'Trainer' }]
const data = {}
const setPhone = (val) => {
    request.value.mobile_number = val
    data.mobile_number = val
}
const setName = (val) => {
    request.value.full_name = val
    data.full_name = val
}
const setNumber = (val) => {
    request.value.account_number = val
    data.account_number = val
}
const setPass = (val) => {
    request.value.password = val
    data.password = val
}
const setEmail = (val) => {
    request.value.email = val
    data.email = val
}


const save = async () => {
    loadingDetails.value = true
    await trainersStore.editSetting(Number(authMe.value), data)
    await trainersStore.show(Number(authMe.value))
    request.value = { account_number: details.value?.account_number, mobile_number: details.value?.mobile_number, full_name: details.value?.full_name, email: details.value?.email, password: null }
    loadingDetails.value = false
};

onMounted(async () => {
    await AuthStore.getMe()
    await trainersStore.show(Number(authMe.value))
    request.value = { account_number: details.value?.account_number, mobile_number: details.value?.mobile_number, full_name: details.value?.full_name, email: details.value?.email, password: null }
    loadingDetails.value = false
})

</script>
  