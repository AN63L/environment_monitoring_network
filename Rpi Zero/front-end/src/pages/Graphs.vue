<template>
  <div>
    <!-- Page header -->
    <div class="sm:flex sm:justify-between sm:items-center mb-8">
    
      <!-- Left: Title -->
      <div class="mb-4 sm:mb-0 grid grid-cols-2 gap-2">
        <h1 class="text-2xl md:text-3xl text-gray-800 dark:text-gray-100 font-bold">Sensor data history (Graphs)</h1>
        <button class="ml-2" @click="loadAllCharts">
          <svg xmlns="http://www.w3.org/2000/svg" height="18" width="18" viewBox="0 0 18 18"><title>refresh 2</title><g stroke-width="1.5" fill="none" stroke="#212121" class="nc-icon-wrapper"><polyline points="8.5 12.75 10.75 15 8.5 17.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><path d="M4.952,4.238c-1.347,1.146-2.202,2.855-2.202,4.762,0,3.452,2.798,6.25,6.25,6.25,.579,0,1.14-.079,1.672-.226" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></path><polyline points="9.5 5.25 7.25 3 9.5 .75" stroke-linecap="round" stroke-linejoin="round"></polyline><path d="M13.048,13.762c1.347-1.146,2.202-2.855,2.202-4.762,0-3.452-2.798-6.25-6.25-6.25-.597,0-1.175,.084-1.722,.24" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        </button>
      </div>
    
    </div>

    <!-- Cards -->
    <div class="grid grid-cols-2 gap-2 pt-4">
        <generic-card title="Temperature" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'temp_chart'" reload> 
          <bar-chart v-if="temperatureChartData.labels.length == 1" :data="temperatureChartData" class="p-4"/>
          <line-chart v-if="temperatureChartData.labels.length > 1" :data="temperatureChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="temperatureChartData.labels.length == 0">NO DATA</p>
        </generic-card>
        <generic-card title="Humidity" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'humidity_chart'" reload>
          <bar-chart v-if="humidityChartData.labels.length == 1" :data="humidityChartData" class="p-4"/>
          <line-chart v-if="humidityChartData.labels.length > 1" :data="humidityChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="humidityChartData.labels.length == 0">NO DATA</p>
        </generic-card>
    </div>

    <div class="grid grid-cols-2 gap-6 pt-4">
        <generic-card title="Pressure" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'pressure_chart'" reload>
          <bar-chart v-if="pressureChartData.labels.length == 1" :data="pressureChartData" class="p-4"/>
          <line-chart v-if="pressureChartData.labels.length > 1" :data="pressureChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="pressureChartData.labels.length == 0">NO DATA</p>
        </generic-card>
        <generic-card title="Gas Resistance" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'gas_resistance_chart'" reload>
          <bar-chart v-if="gasResistanceChartData.labels.length == 1" :data="gasResistanceChartData" class="p-4"/>
          <line-chart v-if="gasResistanceChartData.labels.length > 1" :data="gasResistanceChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="gasResistanceChartData.labels.length == 0">NO DATA</p>
        </generic-card>
    </div>
    
    <div class="grid grid-cols-3 gap-3  pt-4">
        <generic-card title="PM 1.0" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'pm1_chart'" reload>
          <bar-chart v-if="pm1ChartData.labels.length == 1" :data="pm1ChartData" class="p-4"/>
          <line-chart v-if="pm1ChartData.labels.length > 1" :data="pm1ChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="pm1ChartData.labels.length == 0">NO DATA</p>
        </generic-card>
        <generic-card title="PM 2.5" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'pm25_chart'" reload>
          <bar-chart v-if="pm25ChartData.labels.length == 1" :data="pm25ChartData" class="p-4"/>
          <line-chart v-if="pm25ChartData.labels.length > 1" :data="pm25ChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="pm25ChartData.labels.length == 0">NO DATA</p>
        </generic-card>
        <generic-card title="PM 10" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'pm10_chart'" reload>
          <bar-chart v-if="pm10ChartData.labels.length == 1" :data="pm10ChartData" class="p-4"/>
          <line-chart v-if="pm10ChartData.labels.length > 1" :data="pm10ChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="pm10ChartData.labels.length == 0">NO DATA</p>
        </generic-card>
    </div>
    
    <div class="grid grid-cols-1 gap-6  pt-4">
        <generic-card title="Rain frequency" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'rain_chart'" tooltip="% of time rain is detected" reload>
          <stacked-bar-chart :data="rainApexData" :chartOptions="chartOptionsParsedApexRain" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="rainApexData.length == 0">NO DATA</p>
        </generic-card>
    </div>
    <div class="grid grid-cols-1 gap-6  pt-4">
        <generic-card title="Soil moisture frequency" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'moisture_chart'" tooltip="% of time soil moisture is detected" reload>
          <stacked-bar-chart :data="moistureApexData" :chartOptions="chartOptionsParsedApexMoisture" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="moistureApexData.length == 0">NO DATA</p>
        </generic-card>
    </div>

    <div class="grid grid-cols-2 gap-6  pt-4">
        <generic-card title="Rain percentage" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'rain_percentage_chart'" tooltip="Average rain rate detected" reload>
          <bar-chart v-if="rainPercentageChartData.labels.length == 1" :data="rainPercentageChartData" class="p-4"/>
          <line-chart v-if="rainPercentageChartData.labels.length > 1" :data="rainPercentageChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="rainPercentageChartData.labels.length == 0">NO DATA</p>
        </generic-card> 
        <generic-card title="Soil moisture percentage" filter :filterOptions="chartFilterOptions" @updated-filter="handleFilterUpdate" :chartId="'moisture_percentage_chart'" tooltip="Average soil moisture rate detected" reload>
          <bar-chart v-if="moisturePercentageChartData.labels.length == 1" :data="moisturePercentageChartData" class="p-4"/>
          <line-chart v-if="moisturePercentageChartData.labels.length > 1" :data="moisturePercentageChartData" class="p-4"/>
          <p class="border-2 h-full mb-40 content-center text-center" v-if="moisturePercentageChartData.labels.length == 0">NO DATA</p>
        </generic-card>
    </div>
  </div>
</template>

<script>
import GenericCard from '../components/cards/GenericCard.vue';
import LineChart from '../components/charts/LineChart.vue';
import { chartFilterOptions } from '../utils/constants';
import BarChart from '../components/charts/BarChart.vue';
import apiRoutes from '@/utils/apiRoutes';
import { get } from '@/utils/apiMethods';
import logger from '@/utils/logger';
import DoughnutChart from '../components/charts/DoughnutChart.vue';
import StackedBarChart from '../components/charts/StackedBarChart.vue';

export default {
  name: 'Graphs',
  data: (props) => ({
    chartFilterOptions,
  }),
  components: {
    GenericCard,
    LineChart,
    BarChart,
    DoughnutChart,
    StackedBarChart,
  },
  setup(){
  },
  mounted() {
    this.loadAllCharts();
  },
  computed: {
    temperatureChartData() {
      return this.$store.state.data.temperatureChartData;
    },
    humidityChartData() {
      return this.$store.state.data.humidityChartData;
    },
    pressureChartData() {
      return this.$store.state.data.pressureChartData;
    },
    gasResistanceChartData() {
      return this.$store.state.data.gasResistanceChartData;
    },
    pm1ChartData() {
      return this.$store.state.data.pm1ChartData;
    },
    pm25ChartData() {
      return this.$store.state.data.pm25ChartData;
    },
    pm10ChartData() {
      return this.$store.state.data.pm10ChartData;
    },
    rainPercentageChartData() {
      return this.$store.state.data.rainPercentageChartData;
    },
    moisturePercentageChartData() {
      return this.$store.state.data.moisturePercentageChartData;
    },
    rainApexData() {
      return this.$store.state.data.rainApexData;
    },
    chartOptionsParsedApexRain() {
      return this.$store.state.data.chartOptionsParsedApexRain;
    },
    moistureApexData() {
      return this.$store.state.data.moistureApexData;
    },
    chartOptionsParsedApexMoisture() {
      return this.$store.state.data.chartOptionsParsedApexMoisture;
    },
  },
  methods: {
    async handleFilterUpdate(value) {
      switch(value[1]){
        case 'temp_chart':
          await this.loadTempChart(value[0].value, false);
          break;
        case 'humidity_chart':
          await this.loadHumidityChart(value[0].value, false);
          break;
        case 'pressure_chart':
          await this.loadPressureChart(value[0].value, false);
          break;
        case 'gas_resistance_chart':
          await this.loadGasResistanceChart(value[0].value, false);
          break;
        case 'pm1_chart':
          await this.loadPM1Chart(value[0].value, false);
          break;
        case 'pm25_chart':
          await this.loadPM2Chart(value[0].value, false);
          break;
        case 'pm10_chart':
          await this.loadPM10Chart(value[0].value, false);
          break;
        case 'rain_chart':
          await this.loadRainChart(value[0].value, false);
          break;
        case 'moisture_chart':
          await this.loadMoistureChart(value[0].value, false);
          break;
        case 'rain_percentage_chart':
          await this.loadRainPercentageChart(value[0].value, false);
          break;
        case 'moisture_percentage_chart':
          await this.loadMoisturePercentageChart(value[0].value, false);
          break;
        default:
          logger.error('ERROR chart filter update. Unknown chart ID');
      }
    },
    async loadTempChart(filter_value, quiet){
      // temperature chart
      const data = await get(apiRoutes.CHART('temp_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.commit('updateTemperatureChartData', data.data)
    },
    async loadHumidityChart(filter_value, quiet){
      // humidity chart
      const data = await get(apiRoutes.CHART('humidity_chart'), quiet, [{
              name: 'filter_by',
              value: filter_value,
            }]);
      this.$store.commit('updateHumidityChartData', data.data)
    },
    async loadPressureChart(filter_value, quiet){
      // pressure chart
      const data = await get(apiRoutes.CHART('pressure_chart'), quiet, [{
              name: 'filter_by',
              value: filter_value,
            }]);
      this.$store.commit('updatePressureChartData', data.data)
    },
    async loadGasResistanceChart(filter_value, quiet){
      // gas resistance chart
      const data = await get(apiRoutes.CHART('gas_resistance_chart'), quiet, [{
              name: 'filter_by',
              value: filter_value,
            }]);
      this.$store.commit('updateGasResistanceChartData', data.data)
    },
    async loadPM1Chart(filter_value, quiet){
      // pm1 chart
      const data = await get(apiRoutes.CHART('pm1_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.commit('updatePm1ChartData', data.data)
    },
    async loadPM2Chart(filter_value, quiet){
      // pm2 chart
      const data = await get(apiRoutes.CHART('pm25_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.commit('updatePm25ChartData', data.data)
    },
    async loadPM10Chart(filter_value, quiet){
      // pm 10 chart
      const data = await get(apiRoutes.CHART('pm10_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.commit('updatePm10ChartData', data.data)
    },
    async loadRainChart(filter_value, quiet){
      // rain chart
      const data = await get(apiRoutes.CHART('rain_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      // parse data
      this.$store.dispatch('updateRainChartDataApex', data.data)
    },
    async loadMoistureChart(filter_value, quiet){
      // moisture chart
      const data = await get(apiRoutes.CHART('moisture_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.dispatch('updateMoistureChartDataApex', data.data)
    },
    async loadRainPercentageChart(filter_value, quiet){
      // rain percentage chart
      const data = await get(apiRoutes.CHART('rain_percentage_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.commit('updateRainPercentageChartData', data.data)
    },
    async loadMoisturePercentageChart(filter_value, quiet){
      // moisture percentage chart
      const data = await get(apiRoutes.CHART('moisture_percentage_chart'), quiet, [{
        name: 'filter_by',
        value: filter_value,
      }]);
      this.$store.commit('updateMoisturePercentageChartData', data.data)
    },
    async loadAllCharts(){
      // to avoid having a loader spin for each request, handle here
      this.$store.dispatch('toggleLocalSpinner', true);
      await this.loadTempChart(0, true);
      await this.loadHumidityChart(0, true);
      await this.loadPressureChart(0, true);
      await this.loadGasResistanceChart(0, true);
      await this.loadPM1Chart(0, true);
      await this.loadPM2Chart(0, true);
      await this.loadPM10Chart(0, true);
      await this.loadRainChart(0, true);
      await this.loadMoistureChart(0, true);
      await this.loadRainPercentageChart(0, true);
      await this.loadMoisturePercentageChart(0, true);
      this.$store.dispatch('toggleLocalSpinner', false);
    }
  }
}
</script>