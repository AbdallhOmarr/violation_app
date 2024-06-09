import { boot } from 'quasar/wrappers';
import axios from 'axios';
import { Cookies } from 'quasar';
import { handelErrore } from 'src/helper/hendelErrore';
import { sendNotify } from 'src/helper/notify';

const api = axios.create({ baseURL: 'https://api.systemgenius.site/api/' });

export default boot(({ app, redirect, ssrContext }) => {
  const cookies = process.env.SERVER ? Cookies.parseSSR(ssrContext) : Cookies;
  app.config.globalProperties.$axios = axios;
  app.config.globalProperties.$api = api;
  if (cookies.has('access_token')) {
    const token = cookies.get('access_token');
    api.defaults.headers.common['Authorization'] = `Token ${token}`;

  }

  api.interceptors.response.use(
    async (res) => {
      if (res.config.url?.includes("trainers/")) {
        if (res.config.method == "post")
          sendNotify('تم اضافة مدرب الجديد  بنجاح', '', 'positive');
        if (res.config.method == "put")
          sendNotify('تم تعديل بيانات المدرب  بنجاح', '', 'positive');
        if (res.config.method == "delete")
          sendNotify('تم حذف المدرب  بنجاح', '', 'positive');
      }
      if (res.config.url?.includes("departments/")) {
        if (res.config.method == "post")
          sendNotify('تم اضافة القسم الجديد بنجاح', '', 'positive');
        if (res.config.method == "delete")
          sendNotify('تم حذف القسم  بنجاح', '', 'positive');
      }
      if (res.config.url?.includes("trainees/")) {
        if (res.config.method == "post")
          sendNotify('تم اضافة المتدرب الجديد  بنجاح', '', 'positive');
        if (res.config.method == "put")
          sendNotify('تم تعديل بيانات المتدرب  بنجاح', '', 'positive');
        if (res.config.method == "delete")
          sendNotify('تم حذف المتدرب  بنجاح', '', 'positive');
      }
      if (res.config.url?.includes("violations/")) {
        if (res.config.method == "post")
          sendNotify('تم اضافة المخالفة الجديد  بنجاح', '', 'positive');
        if (res.config.method == "put")
          sendNotify('تم تعديل بيانات المخالفة  بنجاح', '', 'positive');
        if (res.config.method == "delete")
          sendNotify('تم حذف المخالفة  بنجاح', '', 'positive');
      }
      return res;
    },
    async (error) => {
      handelErrore(error);

    }
  );

});

export { api };
