<template>
  <q-uploader
    :factory="factoryFn"
    class="col-12 q-my-md q-mx-sm"
    label="Upload image"
    v-model="imageShow"
  >
    <template v-slot:list="scope">
      <q-list v-if="scope.files.length > 0" separator>
        <q-item v-for="file in scope.files" :key="file.__key">
          <q-item-section>
            <q-item-label class="full-width ellipsis">
              {{ file.name }}
            </q-item-label>

            <q-item-label caption> Status: {{ file.__status }} </q-item-label>

            <q-item-label caption>
              {{ file.__sizeLabel }} / {{ file.__progressLabel }}
            </q-item-label>
          </q-item-section>

          <q-item-section v-if="file.__img" thumbnail class="gt-xs">
            <img :src="file.__img.src ? file.__img.src : imageShow" />
          </q-item-section>

          <q-item-section top side>
            <q-btn
              class="gt-xs"
              size="12px"
              flat
              dense
              round
              icon="delete"
              @click="scope.removeFile(file)"
            />
          </q-item-section>
        </q-item>
      </q-list>
      <q-list v-else-if="imageShow" separator>
        <q-item>
          <q-item-section>
            <q-item-label class="full-width ellipsis">
              {{ props.name }}
            </q-item-label>

            <q-item-label caption>
              path : {{ props?.details?.files_path }}
            </q-item-label>
          </q-item-section>

          <q-item-section thumbnail class="gt-xs">
            <img :src="imageShow" />
          </q-item-section>
        </q-item>
      </q-list>
    </template>
  </q-uploader>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { defineEmits, onMounted } from 'vue';
import { useUpload } from 'src/stores/uploadImage';
import { useItemStore } from 'src/stores/item';
import { useMaterItemStore } from 'src/stores/masterItem';
import { useMemberStore } from 'src/stores/member';

const uploadStore = useUpload();
const { image, imageShow, mediId } = storeToRefs(uploadStore);

const masterItem = useMaterItemStore();
const { request: requestMaster } = storeToRefs(masterItem);
const itemStore = useItemStore();
const { request: requestItem } = storeToRefs(itemStore);
const memberStore = useMemberStore();
const { request: requestMember } = storeToRefs(memberStore);

const props = defineProps({
  type: {
    type: String,
    default: '',
  },
  details: {
    type: String,
    default: '',
  },
  name: {
    type: String,
    default: '',
  },
});

const factoryFn = async (file) => {
  const formData = new FormData();
  if (file.length > 0) {
    formData.append('files', file[0]);
    formData.append('filePath', file[0].name);
    await uploadStore.uploadImage(
      formData,
      {
        full_size_image: file[0].name,
        files_path:
          props.type == 'masterItemId'
            ? `mast_${props.details?.id}`
            : props.type == 'itemId'
            ? `item_${props.details?.id}`
            : props.type == 'memberId'
            ? `memb_${props.details?.id}`
            : undefined,
        add_date: new Date(),
      },
      {
        masterItemId:
          props.type == 'masterItemId' ? props.details?.id : undefined,
        itemId: props.type == 'itemId' ? props.details?.id : undefined,
        memberId: props.type == 'memberId' ? props.details?.id : undefined,
      }
    );
    props.type == 'masterItemId'
      ? (requestMaster.value = { ...props?.details, media_id: mediId.value })
      : props.type == 'itemId'
      ? (requestItem.value = { ...props?.details, media_id: mediId.value })
      : (requestMember.value = { ...props?.details, media_id: mediId.value });
    props.type == 'masterItemId'
      ? masterItem.editMasterItem(props.details?.id)
      : props.type == 'itemId'
      ? itemStore.editItem(props.details?.id)
      : memberStore.editMember(props.details?.id);
  }
};

onMounted(async () => {
  uploadStore.downlodImage({
    fileName: props?.details?.full_size_image,
    filesPath: props?.details?.files_path,
  });
});
</script>
