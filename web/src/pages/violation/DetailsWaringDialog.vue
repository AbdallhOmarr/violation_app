<template>
    <q-dialog :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" :model-value="props.modelValue" full-width>
        <form-component titel="تفاصيل مخالفة" @clear:data="clear" :show-button="false">
            <template #content>
                <div class="q-pa-md col-12">
                    <details-component titel="تفاصيل المخالفة
        " :-alldata="details" :name="name" @delete:data="deleteWaring" @print:data="exportPdfs">
                    </details-component>
                </div>
            </template>
        </form-component>
    </q-dialog>
    <!-- pdf 1-->
    <div style="display: none">
        <div id="violation" dir="rtl">
            <div class="tbl-header">
                <p style="font-size:large; font-weight: bold;word-spacing: 10px;padding: 5px">
                    :المتدرب {{
                        details?.trainee_name }}</p>

                <p style="font-size:large; font-weight: bold;word-spacing: 10px;padding: 5px">المخالفة </p>
                <p style="font-size:large; font-weight:normal; padding: 5px;word-spacing: 10px;">
                    {{ details?.violation_details }}
                </p>
                <p style="font-size:large; font-weight:normal; padding: 5px;word-spacing: 10px;">
                    أتعهد بعدم تكرار المخالفة والالتزام بالتعليمات
                    كافة
                </p>
                <p style="font-size:large; font-weight: bold;padding: 5px">------------------ :التاريخ </p>
                <p style="font-size:large; font-weight: bold;padding: 5px">------------------ :التوقيع </p>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { ref, defineEmits, onMounted } from 'vue';
import { storeToRefs } from 'pinia';
//store
import { useViolationStore } from 'src/stores/violations';
//component
import FormComponent from 'src/components/form/FormComponent.vue';
import DetailsComponent from 'src/components/details/DetailsComponent.vue';

const violationStore = useViolationStore()
const { details } = storeToRefs(violationStore)

const name = ref([{ key: 'trainee_name', val: 'المتدرب' }, { key: 'date', val: 'تارخ المخالفة' },
{ key: 'trainer_name', val: "معد المخالفة" },
{ key: 'violation_type', val: "نوع المخالفة" },
{ key: 'degree', val: 'درجة المخالفة' }, { key: 'violation_details', val: 'تفاصيل المخالفة' }, { key: 'taken_procedure', val: 'الاجراء المتخذ من قبل المدرب' }]);

const emit = defineEmits(['update:modelValue']);
const props = defineProps({
    modelValue: {
        type: String,
    },
});

const clear = async () => {
    emit('update:modelValue', false);
};

const deleteWaring = () => {
    emit('update:modelValue', false);
    violationStore.destroy(details.value.id)
}

const exportPdfs = async () => {
    var element = document.getElementById('violation').outerHTML;
    const combinedHtml = element;
    var opt = {
        margin: 10,
        pagebreak: {
            avoid: ['table', 'img'],
        },
        filename: `violation(${details.value.violation_type}).pdf`,
        pagebreak: { mode: 'avoid-all' },
        jsPDF: { format: 'a4', orientation: 'portrait' },
    };
    html2pdf()
        .set(opt)
        .from(combinedHtml)
        .toPdf()
        .get('pdf')
        .then((pdf) => {
            var totalPages = pdf.internal.getNumberOfPages();

            for (let i = 1; i <= totalPages; i++) {
                // set footer to every page
                pdf.setPage(i);
                // set footer font
                pdf.setFontSize(10);
                pdf.setTextColor(150);

                // this example gets internal pageSize just as an example to locate your text near the borders in case you want to do something like "Page 3 out of 4"
                pdf.text(
                    pdf.internal.pageSize.getWidth() / 2.25,
                    pdf.internal.pageSize.getHeight() - 3,
                    `Page ${i} of ${totalPages} `
                );
            }
        })
        .save();
};

function addScript(url) {
    var script = document.createElement('script');
    script.type = 'application/javascript';
    script.src = url;
    document.head.appendChild(script);
}

onMounted(() => {
    addScript(
        'https://raw.githack.com/eKoopmans/html2pdf/master/dist/html2pdf.bundle.js'
    );
});

</script>
  