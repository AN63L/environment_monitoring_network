<template>

<div>
    <!-- Page header -->
    <div class="sm:flex sm:justify-between sm:items-center mb-5">
    
      <!-- Left: Title -->
      <div class="mb-4 sm:mb-0 grid grid-cols-2 gap-2">
        <h1 class="text-2xl md:text-3xl text-gray-800 dark:text-gray-100 font-bold">Sensor data history (tables)</h1>
        <button class="ml-2" @click="loadData">
          <svg xmlns="http://www.w3.org/2000/svg" height="18" width="18" viewBox="0 0 18 18"><title>refresh 2</title><g stroke-width="1.5" fill="none" stroke="#212121" class="nc-icon-wrapper"><polyline points="8.5 12.75 10.75 15 8.5 17.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><path d="M4.952,4.238c-1.347,1.146-2.202,2.855-2.202,4.762,0,3.452,2.798,6.25,6.25,6.25,.579,0,1.14-.079,1.672-.226" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></path><polyline points="9.5 5.25 7.25 3 9.5 .75" stroke-linecap="round" stroke-linejoin="round"></polyline><path d="M13.048,13.762c1.347-1.146,2.202-2.855,2.202-4.762,0-3.452-2.798-6.25-6.25-6.25-.597,0-1.175,.084-1.722,.24" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        </button>
      </div>

    </div>

    <!-- Cards -->
    <div class="mt-4">
        <generic-table-card title="Sensor 1 data (last 100)" :data="sensor1Table" @reload="loadSensor1Table(false)"/>
      </div>
      <div class="mt-4">
        <generic-table-card title="Sensor 2 data (last 100)" :data="sensor2Table" @reload="loadSensor2Table(false)"/>
      </div>
  </div>
</template>

<script>
import Sidebar from '@/containers/Sidebar.vue'
import Header from '@/containers/Header.vue'
import GenericTableCard from '@/components/tables/GenericTableCard.vue'
import apiRoutes from '@/utils/apiRoutes';
import { get } from '@/utils/apiMethods';

export default {
  name: 'Tables',
  components: {
    Sidebar,
    Header,
    GenericTableCard
  },
  data: (props) => ({
  }),
  mounted() {
    this.loadData();
  },
  computed: {
    sensor1Table() {
      return this.$store.state.data.sensor1TableData;
    },
    sensor2Table() {
      return this.$store.state.data.sensor2TableData;
    },
  },
  setup(){
  },
  methods: {
    async loadSensor1Table(quiet){
    const data = await get(apiRoutes.SENSOR_1, quiet);
    if (data.data.length !== 0){
      this.$store.dispatch('updateSensor1TableData', data.data)
    } else {
      this.$store.dispatch('setSensor1NoData')
    }
    },
    async loadSensor2Table(quiet){
    const data = await get(apiRoutes.SENSOR_2, quiet);
    if (data.data.length !== 0){
      this.$store.dispatch('updateSensor2TableData', data.data)
    } else {
      this.$store.dispatch('setSensor2NoData')
    }
    },
    async loadData(){
      // to avoid having a loader spin for each request, handle here
      this.$store.dispatch('toggleLocalSpinner', true);
      await this.loadSensor1Table(true);
      await this.loadSensor2Table(true);
      this.$store.dispatch('toggleLocalSpinner', false);
    }
  }
}
</script>