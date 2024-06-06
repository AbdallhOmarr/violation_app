<template>
  <div class="row justify-center " :class="props?.pading ? 'q-pa-md' : ''">
    <q-card :class="`col-${props.col}`">
      <q-table dir="rtl" :style="!$q.dark.isActive ? `--color:var(--light);` : `--color:var(--dark);`
        " v-model:pagination="pagination" :table-class="$q.dark.isActive ? 'my-custom-dark' : 'my-custom-light'"
        class="my-sticky-header-last-column-table" :rows="props?.rows" :columns="props?.columns"
        :loading="props.loadingTable" row-key="name" :hide-pagination="props.page"
        no-data-label="I didn't find anything for you" :title="props?.title">
        <template v-slot:header="props">
          <q-tr :props="props">
            <q-th v-if="isSelection"></q-th>
            <q-th v-if="isSelectionCheck">
              <q-checkbox v-model="selectAll" :color="$q.dark.isActive ? 'primary' : 'secondary'" @click="() => {
                if (selectAll) {
                  check = [...rows];
                  $emit('check:row', [...rows]);
                } else {
                  check = [];
                  $emit('check:row', []);
                }
              }
                " />
            </q-th>
            <q-th v-for="col in props.cols" :key="col.name" :props="props">
              {{ col.label }}
            </q-th>
          </q-tr>
        </template>

        <template v-slot:body="props">
          <q-tr class="cursor-pointer" @click="onRowClick(props.row)"
            :class="selected?.indexOf(props.row) != -1 ? 'selected' : ''" :props="props">
            <q-td v-if="isSelectionCheck">
              <q-checkbox v-model="check" :val="props.row" @update:model-value="() => {
                if (selectAll && check.length < rows.length)
                  selectAll = none;
                $emit('check:row', check);
              }
                " :color="$q.dark.isActive ? 'primary' : 'secondary'" />
            </q-td>
            <q-td v-if="isSelection">
              <q-btn size="sm" color="primary" round dense @click="async () => {
                oneRow
                  ? await onSelectRow(props.row)
                  : await onSelect(props.row);
                $emit('select:row', selectedRow);
              }
                " :icon="changeIcon && selectedRow?.indexOf(props.row) != -1
    ? 'remove'
    : 'add'
    " /></q-td>
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
              <span v-if="typeof col.value === 'boolean' && col.type == 'notSame'">
                <q-icon v-if="col.value" name="check_circle_outline" color="green" size="md"></q-icon>
                <q-icon v-if="!col.value" name="highlight_off" color="red" size="md"></q-icon></span>
              <span v-else-if="typeof col.value === 'boolean'">
                <q-icon v-if="col.value" name="check_circle_outline" color="green" size="md"></q-icon>
                <q-icon v-if="!col.value" name="highlight_off" color="red" size="md"></q-icon>
              </span>
              <span v-else-if="col?.togle">
                <q-toggle v-model="togle[props?.rowIndex]" @update:model-value="$emit('togle:row', togle, props)" />
              </span>
              <span v-else-if="col?.image">
                <q-btn flat dense icon="picture_as_pdf" color="primary">
                  <q-tooltip class="bg-primary" :offset="[10, 10]">
                    download pdf</q-tooltip>
                </q-btn>
              </span>
              <span v-else-if="col.status">
                <q-chip outline style="color:#126c66 " :label="col.value" />
              </span>
              <span v-else-if="col.name != 'action'">
                {{
                  !col.value
                  ? '---'
                  : col.name.includes('date') || col?.date
                    ? date.formatDate(col.value, 'YYYY/MM/DD')
                    : typeof col.value == 'object'
                      ? col.value?.[$i18n.locale]
                      : col.value
                }}
              </span>

              <span v-else-if="col.name == 'action'">
                <q-btn v-for="(item, index) in action" :key="index" flat dense :icon="item.icon" :color="item.color"
                  @click="click(item, props.row)" :disable="!item?.disable
                    ? false
                    : props.row?.[item.disable?.name] == item.disable?.value
                      ? true
                      : false
                    ">
                  <q-tooltip :class="`bg-${item.color}`" :offset="[10, 10]">
                    {{ item.tooltip }}</q-tooltip>
                </q-btn>
              </span>
              <span> </span>
              <q-popup-edit v-if="col.edit" v-model="props.row">
                <slot :name="col.name" :col="props.row"></slot>
              </q-popup-edit>
            </q-td>
          </q-tr>
          <q-tr v-show="togle[props?.rowIndex] && columns[columns.length - 1]?.expand
            " :props="props">
            <q-td colspan="100%">
              <div class="text-left">
                <slot name="expand" :col="props.row"></slot>
              </div>
            </q-td>
          </q-tr>
        </template>
        <template v-slot:loading>
          <q-inner-loading showing color="primary" />
        </template>
      </q-table>
      <slot name="pagination"></slot>
    </q-card>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref, onMounted } from 'vue';;
import { date } from 'quasar';
import { storeToRefs } from 'pinia';

const pagination = ref({
  sortBy: 'desc',
  descending: false,
  page: 1,
  rowsPerPage: 10,
});

const props = defineProps({
  rows: {
    type: Array,
  },
  columns: {
    type: Array,
  },

  loadingTable: {
    type: Boolean,
    default: false,
  },
  title: {
    type: String,
    default: '',
  },
  items: {
    type: Array,
  },
  pading: {
    type: Boolean,
    default: true,
  },
  col: {
    type: String,
    default: '12',
  },
  isSelection: {
    type: Boolean,
    default: false,
  },
  isSelectionCheck: {
    type: Boolean,
    default: false,
  },
  page: {
    type: Boolean,
    default: true,
  },
  changeIcon: {
    type: Boolean,
    default: true,
  },
  status: {
    type: String,
    default: 'status_id',
  },
  oneRow: {
    type: Boolean,
    default: false,
  },
  defaultCheck: {
    type: Array,
  },
});


const url = ref([]);
const showImage = ref([]);


const action = ref(props?.items);
const click = (item, id) => {
  item.click(id);
};
const selected = ref([]);
const selectedRow = ref([]);

const onRowClick = (row) => {
  selected.value[0] = row;
};

const onSelect = (row) => {
  selectedRow.value?.indexOf(row) == -1
    ? (selectedRow.value[selectedRow.value.length] = row)
    : (selectedRow.value = selectedRow.value.filter((item) => item !== row));
};

const onSelectRow = (row) => {
  selectedRow.value[0] = row;
};

const color = ['red', 'blue', 'teal', 'green', 'orange'];
const togle = ref([]);
const check = ref(props?.defaultCheck ? props?.defaultCheck : []);
const selectAll = ref(false);

onMounted(() => {
  if (props?.columns[props?.columns.length - 1]?.togle) {
    props?.rows.forEach((el, index) => {
      togle.value[index] =
        el?.[props?.columns[props?.columns.length - 1]?.togleName] ==
          props?.columns[props?.columns.length - 1]?.togleValue
          ? true
          : false;
    });
  }
});
</script>

<style>
:root {
  --light: #fff;
  --dark: #1d1d1d;
}

div .my-sticky-header-last-column-table {
  color: var(--q-accent);
}

.my-custom-light th,
.my-custom-light td {
  color: #000 !important;
}

.my-custom-dark th,
.my-custom-dark td {
  color: #fff !important;
}

thead tr:last-child th:last-child {
  position: sticky;
  -webkit-position: sticky;
  left: 0;
  right: 0;
  z-index: 3;

}

thead tr:first-child th

/* bg color is important for th; just specify one */
  {
  background-color: var(--q-accent);
  color: #fff !important;
}

.q-table tbody td:last-child {
  position: sticky;
  -webkit-position: sticky;
  left: 0;
  right: 0;
  z-index: 1;

}

thead tr:last-child th:last-child {
  opacity: 1;

}
</style>
