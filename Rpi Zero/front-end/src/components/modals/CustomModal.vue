<template>
  <ModalBlank @close-modal="handleClose">
    <div class="p-5 flex space-x-4">
      <!-- Icon SUCCESS -->
      <div v-if="modalType == 'SUCCESS'"
        class="w-10 h-10 rounded-full flex items-center justify-center shrink-0 bg-gray-100 dark:bg-gray-700">
        <svg class="shrink-0 fill-current text-green-500" width="16" height="16" viewBox="0 0 16 16">
          <path
            d="M8 0C3.6 0 0 3.6 0 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8zM7 11.4L3.6 8 5 6.6l2 2 4-4L12.4 6 7 11.4z" />
        </svg>
      </div>
      <!-- Icon DANGER -->
      <div v-if="modalType == 'DANGER'"
        class="w-10 h-10 rounded-full flex items-center justify-center shrink-0 bg-gray-100 dark:bg-gray-700">
        <svg class="shrink-0 fill-current text-red-500" width="16" height="16" viewBox="0 0 16 16">
          <path
            d="M8 0C3.6 0 0 3.6 0 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8zm0 12c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1zm1-3H7V4h2v5z" />
        </svg>
      </div>
      <!-- Icon INFO -->
      <div v-if="modalType == 'INFO'"
        class="w-10 h-10 rounded-full flex items-center justify-center shrink-0 bg-gray-100 dark:bg-gray-700">
        <svg class="shrink-0 fill-current text-violet-500" width="16" height="16" viewBox="0 0 16 16">
          <path
            d="M8 0C3.6 0 0 3.6 0 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8zm1 12H7V7h2v5zM8 6c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1z" />
        </svg>
      </div>
      <!-- Content -->
      <div class="w-full">
        <!-- Modal header -->
        <div class="mb-2">
          <div class="text-lg font-semibold text-gray-800 dark:text-gray-100">{{modalTitle}}</div>
        </div>
        <!-- Modal content -->
        <div class="text-sm mb-10">
          <div class="space-y-2">
            <p>{{modalMessage}}</p>
          </div>
        </div>
        <!-- Modal footer -->
        <div class="flex flex-wrap justify-end space-x-2">
          <button
            class="btn-sm border-gray-200 dark:border-gray-700/60 hover:border-gray-300 dark:hover:border-gray-600 text-gray-800 dark:text-gray-300"
            @click.stop="handleClose"
            >{{modalCancelText}}</button>
          <button v-if="modalType != 'INFO'" class="btn-sm bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-gray-100 dark:text-gray-800 dark:hover:bg-white" @click.stop="handleConfirm">{{modalSuccessText}}</button>
        </div>
      </div>
    </div>
  </ModalBlank>
</template>

<script>
import ModalBlank from './ModalBlank.vue';

export default {
  name: 'CustomModal',
  props: ['type'],
  // emits: ['close-modal'],
  components: {
    ModalBlank,
  },
  data: (props) => ({
    modalType: null,
    modalMessage: null,
    modalTitle: null,
    modalCancelText: null,
    modalSuccessText: null,
    modalInvocationType: props.type
  }),
  mounted() {
  },
  beforeMount() {
    const data = this.$store.getters.storeModalData
    this.modalType = data.modalType;
    this.modalMessage = data.modalMessage;
    this.modalTitle = data.modalTitle;
    this.modalCancelText = data.modalCancelText;
    this.modalSuccessText = data.modalSuccessText;
  },
  methods: {
    handleClose() {
      if (this.modalInvocationType === 'local'){
        this.$store.commit('closeLocalModal')
      } else {
        this.$store.commit('closeGlobalModal')
      }
    },
    handleConfirm() {
      if (this.modalInvocationType === 'local'){
        this.$store.dispatch('handleLocalModalClose')
      } else {
        this.$store.dispatch('handleGlobalModalClose')
      }
    }
  },
  computed: {
  },
}
</script>