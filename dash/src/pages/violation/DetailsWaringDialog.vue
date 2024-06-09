<template>
    <q-dialog :dir="$i18n.locale == 'en' ? ' ltr' : 'rtl'" :model-value="props.modelValue" full-width>
        <form-component titel="تفاصيل مخالفة" @clear:data="clear" :show-button="false">
            <template #content>
                <div class="q-pa-md col-12">
                    <details-component :delete="detailsTrainer?.is_superuser ? true : false" titel="تفاصيل المخالفة
        " :-alldata="details" :name="name" @delete:data="deleteWaring" @print:data="exportPdfs">
                    </details-component>
                </div>
            </template>
        </form-component>
    </q-dialog>
    <!-- pdf 1-->
    <div style="display: none">
        <div id="violation" dir="rtl">
            <div class="report-container">
                <header class="report-header">
                    <p class="report-title">تعهد</p>
                </header>
                <div class="report-content">
                    <section class="report-section">
                        <div class="section-content">
                            <div class="row">
                                <div class="col-label"> المتدرب</div>
                                <div class="col-value"> {{ details?.trainee_name }}</div>
                            </div>
                            <div class="row">
                                <div class="col-label"> المخالفة</div>
                                <div class="col-value"> {{ details?.violation_type }}</div>
                            </div>
                            <div class="row">
                                <div class="col-label">التاريخ</div>
                                <div class="col-value">{{ details?.date }}</div>
                            </div>
                            <div class="row">
                                <div class="col-label">معد المخالفة</div>
                                <div class="col-value">{{ details?.trainer_name }}</div>
                            </div>
                        </div>
                    </section>
                    <section class="report-section">
                        <div class="section-content">

                            <p style="font-size: 24px;"> اتعهد بالتزام بكافة التعليمات</p>

                        </div>
                    </section>
                    <footer class="report-footer">
                        <p> الاسم ---------------------</p>
                        <p> التاريخ ---------------------</p>
                        <p> التوقيع ---------------------</p>
                    </footer>
                </div>
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
import { useAuthStore } from 'src/stores/login';
import { Loading } from 'quasar';
import { useTrainerStore } from 'src/stores/trainers';

const violationStore = useViolationStore()
const { details } = storeToRefs(violationStore)

const AuthStore = useAuthStore()
const { authMe } = storeToRefs(AuthStore)

const trainersStore = useTrainerStore()
const { details: detailsTrainer } = storeToRefs(trainersStore)

const name = ref([{ key: 'trainee_name', val: 'المتدرب' }, { key: 'date', val: 'تارخ المخالفة' },
{ key: 'trainer_name', val: "معد المخالفة" },
{ key: 'violation_type', val: " المخالفة" },
{ key: 'degree', val: 'درجة المخالفة' }, { key: 'violation_details', val: 'ملاحظات المخالفة' }]);

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

onMounted(async () => {
    Loading.show()
    await AuthStore.getMe()
    await trainersStore.show(Number(authMe.value))
    Loading.hide()
})
</script>
<style>
.report-container {
    font-family: 'Tajawal', sans-serif;
    direction: rtl;
    text-align: right;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px;
}

.report-header {
    text-align: center;
    margin-bottom: 40px;
}

.report-title {
    font-size: 32px;
    font-weight: 700;
}

.report-section {
    margin-bottom: 10px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 20px;
}

.section-content {
    text-align: center;
    margin-bottom: 20px
}

.row {
    display: flex;
    justify-content: start;
    margin-bottom: 10px;
}

.col-label {
    font-weight: 600;
    margin-left: 10px;
}

.report-footer {
    text-align: start;
    color: #666;
    font-size: 14px;
}
</style>