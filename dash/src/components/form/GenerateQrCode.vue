<template>
  <client-only>
    <div v-if="props?.value" class="row justify-between items-center">
      <QRCodeVue3
        class="col-4"
        :width="200"
        :height="200"
        :download="props?.download"
        downloadButton="my-button"
        :downloadOptions="{ name: 'Qr', extension: 'png' }"
        :value="props?.value"
        :qrOptions="{ typeNumber: 10, mode: 'Byte', errorCorrectionLevel: 'Q' }"
        :dotsOptions="{ type: 'square', color: '#05004d' }"
        :cornersSquareOptions="{ type: 'square', color: '#0e013c' }"
      />
      <span class="col-md-4 text-weight-bold text-primary" v-if="props?.name">
        {{ props?.name }}</span
      >
    </div>

    <div v-else>----</div>
  </client-only>
</template>

<script lang="ts">
import { defineComponent, defineAsyncComponent } from 'vue';

export default defineComponent({
  name: 'GenerateQrCode',
  components: {
    QRCodeVue3: defineAsyncComponent(() =>
      Promise.resolve(import('qrcode-vue3'))
    ),
  },
  props: {
    value: { type: String, default: '' },
    download: { type: Boolean, default: true },
    name: { type: String, default: '' },
  },
  setup(props) {
    return { props };
  },
});
</script>

<style>
.my-button {
  margin-right: 10px !important;
}
</style>
