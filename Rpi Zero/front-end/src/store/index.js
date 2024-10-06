import { createStore, createLogger } from 'vuex'
import data from './modules/data';
import display from './modules/display';
import notifications from './modules/notifications';

export default createStore({
  modules: {
    data,
    display,
    notifications,
  },
  plugins: [createLogger()]
})
