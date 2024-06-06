import { sendNotify } from './notify';

export const handelErrore = async (error) => {
  let messages;

  switch (error?.response?.status) {
    case 400:
      messages = 'المدخلات غير صحيحة';
      break;
    case 401:
      messages = 'ليس لديك صلاحيةلاجراء التعديل المطلوب ';
      break;
    case 403:
      messages = 'ليس لديك صلاحيةلاجراء التعديل المطلوب ';
      break;
    case 404:
      messages = 'غير موجود';
      break;
    case 500:
      messages = 'حدث خطأ ما';
      break;
    default:
      messages = 'حدث خطأ ما';
      break;
  }

  await sendNotify(messages, error?.response?.data?.non_field_errors?.[0] ?? '', 'negative');
};
