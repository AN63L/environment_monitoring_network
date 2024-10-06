import logger from '@/utils/logger';


const state = {
  notifications: null,
};

const mutations = {
  async updateNotificationAttribute(state, data) {
    state.notifications = {
      ...state.notifications,
      [data.filter]: data.value
    }
  },
  async updateNotificationsObject(state, data) {
    state.notifications = data
  },

};
const actions = {
  setNotifications({commit, state}, data){
    let parsed_data = {}
    for (let i = 0; i < data.length; i++){
      parsed_data[data[i].name] = data[i].active
    }
    commit('updateNotificationsObject', parsed_data);
  },
};
const getters = {
  
};
export default {
  state,
  getters,
  actions,
  mutations,
}
