<template>
  <router-view />
</template>

<script>
import apiRoutes from '@/utils/apiRoutes';
import { get } from '@/utils/apiMethods';

export default {
  name: 'App',
  async mounted() {
    this.getAPIStatus();
  },
  methods: {
    async getAPIStatus(){
      try {
        const resp = await get(apiRoutes.HEALTH, true);
        this.$store.dispatch('handleAPIStatus', resp.status)
      } catch (e){
        this.$store.dispatch('handleAPIStatus', true)
      }
    }
  }
}
</script>

