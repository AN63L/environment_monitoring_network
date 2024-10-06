<template>
  <div class="flex h-[100dvh] overflow-hidden">

    <transition name="fade">
      <spinner-overlay v-if="globalSpinnerVisible"/>
    </transition>
    <custom-modal v-if="globalModalVisible" class="overlay" type="global"/>
    <custom-toast v-if="globalToastVisible" class="toast" />
    <network-toast v-if="APIIndicatorToastVisible" class="toast" />
    <!-- Sidebar -->
    <Sidebar :sidebarOpen="sidebarOpen" @close-sidebar="sidebarOpen = false" />

    <!-- Content area -->
    <div class="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
      
      <!-- Site header -->
      <Header :sidebarOpen="sidebarOpen" @toggle-sidebar="sidebarOpen = !sidebarOpen" />
      <custom-modal v-if="localModalVisible" class="overlay" type="local"/>
      <main class="grow">
        <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
          <transition name="fade">
            <spinner-overlay v-if="localSpinnerVisible"/>
          </transition>
          <router-view :key="$route.path"></router-view>
        </div>
      </main>
    </div> 

  </div>
</template>

<script>
import { ref } from 'vue'
import Sidebar from './Sidebar.vue'
import Header from './Header.vue'
import SpinnerOverlay from '@/components/spinners/SpinnerOverlay.vue';
import CustomModal from '../components/modals/CustomModal.vue';
import CustomToast from '../components/toasts/CustomToast.vue';
import NetworkToast from '@/components/toasts/NetworkToast.vue';


export default {
  name: 'Dashboard',
  components: {
    Sidebar,
    Header,
    SpinnerOverlay,
    CustomModal,
    CustomToast,
    NetworkToast
  },
  setup() {

    const sidebarOpen = ref(false)

    return {
      sidebarOpen,
    }  
  },
  computed: {
    localSpinnerVisible() {
      return this.$store.state.display.localSpinnerVisible;
    },
    globalSpinnerVisible() {
      return this.$store.state.display.globalSpinnerVisible;
    },
    localModalVisible() {
      return this.$store.state.display.localModalVisible;
    },
    globalModalVisible() {
      return this.$store.state.display.globalModalVisible;
    },
    globalToastVisible() {
      return this.$store.state.display.globalToastVisible;
    },
    APIIndicatorToastVisible() {
      return this.$store.state.display.APIIndicatorToastVisible;
    },
  },
}
</script>
<style scoped>
.overlay {
  position: absolute;
  height: 100%;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.75);
  z-index: 999;
  display: flex;
  justify-content: center;
  align-items: center;
}
.toast {
  position: absolute;
  /* height: 100%; */
  width: 100%;
  z-index: 999;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>