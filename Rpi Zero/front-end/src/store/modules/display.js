import logger from '@/utils/logger';
import {selectFunction} from '@/utils/sharedFunctions';

const sharedFunctionNames = ['EMPTY'];

const types = ['SUCCESS, DANGER, INFO']
const state = {
  localSpinnerVisible: false,
  globalSpinnerVisible: false,
  localModalVisible: false,
  globalModalVisible: false,
  modalType: null,
  modalMessage: null,
  modalTitle: null,
  modalCancelText: null,
  modalSuccessText: null,
  modalConfirmFunction: null,
  globalToastVisible: false,
  globalToastText: null,
  globalToastType: null,
  APIIndicatorToastVisible: false,
};
const mutations = {
  toggleLocalSpinnerVisibility(state, value) {
    state.localSpinnerVisible = value;
  },
  toggleGlobalSpinnerVisibility(state, value) {
    state.globalSpinnerVisible = value;
  },
  closeLocalModal(state, value) {
    state.localModalVisible = false;
    state.modalType = null;
    state.modalMessage = null;
    state.modalTitle = null;
  },
  closeGlobalModal(state, value) {
    state.globalModalVisible = false;
    state.modalType = null;
    state.modalMessage = null;
    state.modalTitle = null;
  },
  updateModalData(state, data) {
    state.modalType = data.modalType
    state.modalMessage = data.modalMessage
    state.modalTitle = data.modalTitle
    state.modalCancelText = data.modalCancelText
    state.modalSuccessText = data.modalSuccessText
    state.modalConfirmFunction = data.modalConfirmFunction
  },
  openLocalModal(state, value) {
    state.localModalVisible = true;
  },
  openGlobalModal(state, value) {
    state.globalModalVisible = true;
  },
  closeGlobalToast(state, value) {
    state.globalToastVisible = false;
    state.globalToastText = null;
    state.globalToastType = null;
  },
  openGlobalToast(state, value) {
    state.globalToastVisible = true;
  },
  updateGlobalToastData(state, data) {
    state.globalToastText = data.globalToastText;
    state.globalToastType = data.globalToastType;
  },
  updateAPIStatus(state, data) {
    state.APIIndicatorToastVisible = data;
  },
};
const actions = {
  toggleLocalSpinner({commit, state}, value){
    commit('toggleLocalSpinnerVisibility', value)
  },
  toggleGlobalSpinner({commit, state}, value){
    commit('toggleGlobalSpinnerVisibility', value)
  },
  displayLocalModal({commit, state}, data) {
    commit('updateModalData', data)
    commit('openLocalModal')
  },
  displayGlobalModal({commit, state}, data) {
    commit('updateModalData', data)
    commit('openGlobalModal')
  },
  async handleLocalModalClose({commit, state}, data) {
    commit('closeLocalModal');
    if (sharedFunctionNames.includes(state.modalConfirmFunction)){
      await selectFunction(state.modalConfirmFunction)
    }
    state.modalConfirmFunction = null;
  },
  async handleGlobalModalClose({commit, state}, data) {
    commit('closeGlobalModal');
    if (sharedFunctionNames.includes(state.modalConfirmFunction)){
      await selectFunction(state.modalConfirmFunction)
    }
    state.modalConfirmFunction = null;
  },
  displayGlobalToast({commit, state}, data) {
    commit('updateGlobalToastData', data)
    commit('openGlobalToast')
    setTimeout(function(){
      commit('closeGlobalToast')
    }, 5000);
  },
  handleGlobalToastClose({commit, state}, data) {
    commit('closeGlobalToast')
  },
  handleAPIStatus ({commit, state}, data) {
    if (data === 200){
      commit('updateAPIStatus', false)
    } else {
      commit('updateAPIStatus', true)
    }
  },
};
const getters = {
  storeModalData (state) {
    const modalData = {
      modalType: state.modalType,
      modalMessage: state.modalMessage,
      modalTitle: state.modalTitle,
      modalCancelText: state.modalCancelText,
      modalSuccessText: state.modalSuccessText,
      modalConfirmFunction: state.modalConfirmFunction,
    }
    return modalData;
  },
  storeToastData (state) {
    const modalData = {
      globalToastText: state.globalToastText,
      globalToastType: state.globalToastType
    }
    return modalData;
  },
  apiToastVisibility (state) {
    return state.APIIndicatorToastVisible;
  },
};
export default {
  state,
  getters,
  actions,
  mutations,
}
