import { Notify } from 'quasar';


export const sendNotify = async (
  messages,
  caption,
  type
) => {
  Notify.create({
    type: type,
    message: messages,
    caption: caption,
    timeout: 1000
  });
};
