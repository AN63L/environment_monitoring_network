<template>
<div>
    <!-- Dashboard actions -->
    <div class="sm:flex sm:justify-between sm:items-center mb-8">

      <!-- Left: Title -->
      <div class="mb-4 sm:mb-0 grid grid-cols-2 gap-2">
        <h1 class="text-2xl md:text-3xl text-gray-800 dark:text-gray-100 font-bold">Dashboard</h1>
        <button class="ml-2" @click="loadData">
          <svg xmlns="http://www.w3.org/2000/svg" height="18" width="18" viewBox="0 0 18 18"><title>refresh 2</title><g stroke-width="1.5" fill="none" stroke="#212121" class="nc-icon-wrapper"><polyline points="8.5 12.75 10.75 15 8.5 17.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><path d="M4.952,4.238c-1.347,1.146-2.202,2.855-2.202,4.762,0,3.452,2.798,6.25,6.25,6.25,.579,0,1.14-.079,1.672-.226" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></path><polyline points="9.5 5.25 7.25 3 9.5 .75" stroke-linecap="round" stroke-linejoin="round"></polyline><path d="M13.048,13.762c1.347-1.146,2.202-2.855,2.202-4.762,0-3.452-2.798-6.25-6.25-6.25-.597,0-1.175,.084-1.722,.24" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1">
      <p class="text-sm italic">Last sensor 1 data received:  {{sensor1DataLastAcquisition}} seconds ago</p>
      <p class="text-sm italic">Last sensor 2 data received:  {{sensor2DataLastAcquisition}} seconds ago</p>
    </div>
      <!-- Cards -->
      <div class="grid grid-cols-1 gap-6">
        <card-with-headers title="Environment metrics Metrics" :headers="headersEnv" :cols="2"/>
        <card-with-headers title="Air quality" :headers="headersAQI" :cols="3" tooltip="IAQ is based on average of PM2.5, PM10 and BME680 sensor IAQ calculations"/>
        <card-with-headers title="Humidity" :headers="headersHumidity" :cols="2"/>
      </div>

  </div>

</template>

<script>
import GenericCard from '@/components/cards/GenericCard.vue';
import CardWithHeaders from '@/components/cards/CardWithHeaders.vue';
import apiRoutes from '@/utils/apiRoutes';
import { get } from '@/utils/apiMethods';

export default {
  name: 'Dashboard',
  components: {
    GenericCard,
    CardWithHeaders,
  },
  data: (props) => ({
  }),
  mounted() {
    this.loadData();
  },
  computed: {
    sensor1DataLastAcquisition() {
      return this.$store.state.data.sensor1DataLastAcquisition;
    },
    sensor2DataLastAcquisition() {
      return this.$store.state.data.sensor2DataLastAcquisition;
    },
    headersEnv() {
      return this.$store.state.data.headersEnv;
    },
    headersAQI() {
      return this.$store.state.data.headersAQI;
    },
    headersHumidity() {
      return this.$store.state.data.headersHumidity;
    },
  },
  methods: {
    async loadData(){
      // get data from api
      const data = await get(apiRoutes.LATEST, false);
      // update store data
      if (data.data != null){
        this.$store.dispatch('updateLatestData', data.data)
      }
    }
  }
}
</script>