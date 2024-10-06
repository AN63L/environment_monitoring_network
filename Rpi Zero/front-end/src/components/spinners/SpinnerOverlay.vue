<template>
  <div class="overlay">
    <VueSpinner class="spinner" size="100" color="linear-gradient(135deg,var(--tw-gradient-stops))" />
  </div>
</template>

<script>
import {VueSpinner} from 'vue3-spinners';
export default {
  name: 'SpinnerOverlay',
  components: { VueSpinner },
};
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

.spinner {
  justify-content: center;
  
}
</style>
