<template>
    <q-dialog :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" :model-value="props.modelValue" full-width>
        <form-component :titel="props.edit ? 'تعديل بيانات المخالفة ' : 'اضافة مخالفة'" @clear:data="clear"
            @update:data="save" :loading="loading.type == 'change' ? loading.value : false">
            <template #content>
                <InputSelect label=" المتدرب " col="6" :isValid="true" @update:text="setTrainee" :default="request?.trainee"
                    :options="listTrainee" optionLabel="full_name"
                    :loading="loadingTrainee.type == 'list' ? loadingTrainee.value : false"></InputSelect>
                <InputDate label=" تاريخ ارتكاب المخالفة" col="6" :isValid="true" @update:text="setDate"
                    :default="request?.date"></InputDate>
                <InputSelect label="نوع المخالفة" col="6" @update:text="setType" :default="request?.violation_type"
                    :options="type" optionLabel="id">
                </InputSelect>
                <InputText label="تفاصيل المخالفة " col="12" @update:text="setDetails" :default="request?.violation_details"
                    type="textarea">
                </InputText>
                <InputText label="  الاجراء المتخذ من قبل المدرب   " col="12" @update:text="setProcess"
                    :default="request?.taken_procedure" type="textarea"></InputText>
            </template>
        </form-component>
    </q-dialog>
</template>
  
<script setup>
import { defineEmits } from 'vue';
import { storeToRefs } from 'pinia';
//store
import { useViolationStore } from 'src/stores/violations';
import { useTraineeStore } from 'src/stores/trainees';
//component
import FormComponent from 'src/components/form/FormComponent.vue';
import InputSelect from 'src/components/formInput/InputSelect.vue';
import InputText from 'src/components/formInput/InputText.vue';
import InputDate from 'src/components/formInput/InputDate.vue';
import InputDescription from 'src/components/formInput/InputDescription.vue';

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

const violationStore = useViolationStore()
const { loading, request } = storeToRefs(violationStore)

const traineesStore = useTraineeStore()
const { list: listTrainee, loading: loadingTrainee } = storeToRefs(traineesStore)

const setDate = (val) => {
    request.value.date = val
}

const setTrainee = (val) => {
    request.value.trainee = val?.id || val
}
const setType = (val) => {
    request.value.degree = type.filter((el) => el.id == val)?.[0].degree
    request.value.violation_type = val?.id || val
}
const setDetails = (val) => {
    request.value.violation_details = val
}
const setProcess = (val) => {
    request.value.taken_procedure = val
}

const save = async () => {
    props.edit ? await violationStore.editViolations(request.value.id) : await violationStore.addViolations()
    emit('update:modelValue', false);
    violationStore.resetRequest()
};

const type = [{ id: 'تناول الأطعمة والمشروبات أثناء التدري', degree: 1 },
{ id: 'اعاقة سير التدريب بالحديث الجانبي والمقاطعة المستمرة غير الهادفة', degree: 1 },
{ id: 'النوم داخل مكان التدريب', degree: 1 },
{ id: 'الدخول والخروج من القاعة التدريبية دون استئذان', degree: 1 }
    , { id: 'عدم إحضار الحقائب والأدوات التدريبية', degree: 1 }
    , { id: 'استخدام اجهزة الاتصال الشخصية اثناء التدريب', degree: 1 }
    , { id: 'إطالة الشعر والقصات المخالفة للقيم الاسلامية او السلامة المهنية', degree: 1 }
    , { id: 'عدم التقيد بالزي الرسمي', degree: 1 }
    , { id: 'امتهان الحقائب التدريبية', degree: 1 }
    , { id: 'رمي النفايات داخل الوحدة التدريبية', degree: 1 }
    , { id: 'حمل الدخان او ما في حكمه', degree: 1 }
    , { id: 'إثارة الفوضى داخل محيط الوحدة التدريبية', degree: 2 }
    , { id: 'إساءة استخدام الممتلكات وأجهزة الوحدة التدريبية والعبث بها.', degree: 2 }
    , { id: 'المخالفة ةالمرورية داخل الوحدة التدريبية.', degree: 2 }
    , { id: 'التلفظ على المتدربين بألفاظ سيئة', degree: 2 }
    , { id: 'التشبة بالجنس الاخر', degree: 2 }
    , { id: 'محاولة الغش في الاختبار او التقيم او المساعدة في ذلك ( نظري – عملي. )', degree: 2 },
{ id: 'الحاق الضرر المتعمد بممتلكات المتدربين او احد منسوبي الوحدة التدريبية او مزودي الخدمة.', degree: 3 },
{ id: 'الغش في الاختبار او التقيم ( نظري – عملي)', degree: 3 },
{ id: 'التدخين او ما حكمه داخل محيط الوحدة التدريبية', degree: 3 },
{ id: 'تهديد منسوبي ومدربي ومزودي الخدمة في  الوحدة التدريبية او محاولة الإيذاء او التلفظ عليهم بكلمات مسيئة', degree: 4 },
{ id: 'احضار المواد الخطرة داخل الوحدة التدريبية', degree: 4 },
{ id: 'التحرشات السلوكية الشاذة', degree: 4 },
{ id: 'استخدام المخدرات او الممنوعات', degree: 4 },
{ id: 'عرض الاشياء المنافية للأخلاق في الوحدة التدريبية', degree: 4 },
{ id: 'ممارسة السرقة', degree: 4 },
{ id: 'تعمد اتلاف او تخريب شيء من تجهيزات الوحدة التدريبية المهنية', degree: 4 },
{ id: 'اقامة وتنظيم التجمعات الغير نظامية التب تمس الأمن الفكري واللحمة الوطنية وما يبنى عليها من جمع الأموال وخلافه', degree: 4 },
{ id: 'الاستهانة بشيء من شعائر الإسلام او العمل على نشر الأفكار والمذاهب الهدامة', degree: 5 },
{ id: 'ترويج المخدرات ىما في حكمها', degree: 5 },
{ id: 'ممارسة السلوك الشاذ', degree: 5 },
{ id: 'تعمد ترك اداء الصلاة', degree: 5 },
{ id: 'حيازة او استخدام الأسلحة وما في حكمها', degree: 5 },
{ id: 'تزوير الوثائق الرسمية او انتحال الشخصية', degree: 5 },
{ id: 'الاعتداء على منسوبي او متدربي الوحدة التدريبية او مزودي الخدمة', degree: 5 },
{ id: 'استخدام المواد او الأدوات الخطرة للوحدة التدريبية', degree: 5 },
{ id: 'توزيع المواد الاعلامية المؤثرة على القيم الدينية والفكر والأخلاق الحميدة', degree: 5 },
{ id: 'إساءة استخدام وسائل التواصل والأجهزة الذكية وما يبنى عليها من تصوير وخلافه', degree: 5 },
{ id: 'نشر الرذيلة عن طريق إقامة علاقات محرمة او توزيع ارقام او خلاف ذلك', degree: 5 },
{ id: 'الحالات المماثلة لمخالفات الدرجة الخامسة والتي يصبح فيها المتدرب خطراً على مجتمع الوحدة التدريبية', degree: 5 }]
const clear = async () => {
    violationStore.resetRequest()
    emit('update:modelValue', false);
};
;
</script>
  