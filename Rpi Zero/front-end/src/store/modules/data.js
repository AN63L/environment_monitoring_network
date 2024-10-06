import {measure_AQI, qualitative_AQI} from '@/utils/sharedFunctions'
import { emptyTable, emptyChart, emptyApexChartOptions } from '@/utils/constants';
import logger from '@/utils/logger';


const state = {
  temperatureChartData: emptyChart,
  humidityChartData: emptyChart,
  pressureChartData: emptyChart,
  gasResistanceChartData: emptyChart,
  pm1ChartData: emptyChart,
  pm25ChartData: emptyChart,
  pm10ChartData: emptyChart,
  moistureChartData: emptyChart,
  rainPercentageChartData: emptyChart,
  moisturePercentageChartData: emptyChart,
  sensor1DataLastAcquisition: 'null',
  sensor2DataLastAcquisition: 'null',
  headersEnv: [
    {
      value: null,
      metric: '%',
      legend: 'Humidity',
      header_value: null
    },
    {
        value: null,
        metric: '°C',
        legend: 'Temperature',
        header_value: null
    },
    {
        value: null,
        metric: 'hPa',
        legend: 'Pressure',
        header_value: null
    },
    {
        value: null,
        metric: 'm',
        legend: 'Altitude',
        header_value: null
    }
  ],
  headersAQI: [
    {
      value: null,
      metric: 'µg/m3',
      legend: 'PM 1.0',
      header_value: null
    },
    {
      value: null,
      metric: 'µg/m3',
      legend: 'PM 2.5',
      header_value: null
    },
    {
        value: null,
        metric: 'µg/m3',
        legend: 'PM 10',
        header_value: null
    },
    {
        value: null,
        metric: null,
        legend: 'IAQ',
        header_value: null
    },
    {
        value: null,
        metric: null,
        legend: 'Air Quality',
        header_value: null
  }],
  headersHumidity: [
    {
      value: null,
      metric: null,
      legend: 'Is Raining ?',
      header_value: null
    },
    {
        value: null,
        metric: null,
        legend: 'Is soil moist ?',
        header_value: null
    }
  ],
  sensor1TableData: emptyTable,
  sensor2TableData: emptyTable,
  rainApexData: [],
  chartOptionsParsedApexRain: emptyApexChartOptions,
  moistureApexData: [],
  chartOptionsParsedApexMoisture: emptyApexChartOptions
};

const mutations = {
  async updateDashboardData(state, data) {
    state.sensor1DataLastAcquisition = data.sensor_1.last_update_seconds
    state.sensor2DataLastAcquisition = data.sensor_2.last_update_seconds
    // humidity
    state.headersEnv[0].value = data.sensor_1.humidity
    // temperature
    state.headersEnv[1].value = (data.sensor_1.temperature).toFixed(2)
    // pressure
    state.headersEnv[2].value = data.sensor_1.pressure
    // altitude
    state.headersEnv[3].value = data.sensor_1.altitude
    // pm1
    state.headersAQI[0].value = data.sensor_1.pm_1
    // pm2
    state.headersAQI[1].value = data.sensor_1.pm_2
    // pm10
    state.headersAQI[2].value = data.sensor_1.pm_10
    // AQI
    const AQ = await measure_AQI(data.sensor_1.temperature, data.sensor_1.pressure, data.sensor_1.humidity, data.sensor_1.gas_resistance, data.sensor_1.pm_2, data.sensor_1.pm_10)
    state.headersAQI[3].value = AQ
    // Air quality
    state.headersAQI[4].value = await qualitative_AQI(AQ)
    // is raining
    state.headersHumidity[0].value =  data.sensor_2.is_raining
    // is soil moist
    state.headersHumidity[1].value = data.sensor_2.is_soil_moist
  },
  async updateSensor1Data(state, data) {
    state.sensor1TableData = data
  },
  async updateSensor2Data(state, data) {
    state.sensor2TableData = data
  },
  async updateTemperatureChartData(state, data) {
    state.temperatureChartData = data
  },
  async updateHumidityChartData(state, data) {
    state.humidityChartData = data
  },
  async updatePressureChartData(state, data) {
    state.pressureChartData = data
  },
  async updateGasResistanceChartData(state, data) {
    state.gasResistanceChartData = data
  },
  async updatePm1ChartData(state, data) {
    state.pm1ChartData = data
  },
  async updatePm25ChartData(state, data) {
    state.pm25ChartData = data
  },
  async updatePm10ChartData(state, data) {
    state.pm10ChartData = data
  },
  async updateRainPercentageChartData(state, data) {
    state.rainPercentageChartData = data
  },
  async updateMoisturePercentageChartData(state, data) {
    state.moisturePercentageChartData = data
  },

};
const actions = {
  updateLatestData({commit, state}, data){
    commit('updateDashboardData', data);
  },
  updateSensor1TableData({commit, state}, data){
    const columns = []
    const parsed_data = {}
    for (let x = 0; x < Object.keys(data[0]).length; x++){
      let obj = {
        label: Object.keys(data[0])[x],
        field: Object.keys(data[0])[x],
        width: (((1/(Object.keys(data).length-1))*100).toFixed(0)).toString()+"%",
        sortable: true,
      }
      columns.push(obj)
    }
    parsed_data['columns'] = columns
    parsed_data['rows'] = data
    parsed_data['isLoading'] = false
    parsed_data['total'] = data.length 
    parsed_data['sortable'] = {
      order: "id",
      sort: "dsc",
    },
    commit('updateSensor1Data', parsed_data);
  },
  setSensor1NoData({commit, state}){
    const parsed_data = {}
    parsed_data['columns'] = []
    parsed_data['rows'] = []
    parsed_data['isLoading'] = false
    parsed_data['total'] = 0
    commit('updateSensor1Data', parsed_data);
  },
  updateSensor2TableData({commit, state}, data){
    const columns = []
    const parsed_data = {}
    for (let x = 0; x < Object.keys(data[0]).length; x++){
      let obj = {
        label: Object.keys(data[0])[x],
        field: Object.keys(data[0])[x],
        width: (((1/(Object.keys(data).length-1))*100).toFixed(0)).toString()+"%",
        sortable: true,
      }
      columns.push(obj)
    }
    parsed_data['columns'] = columns
    parsed_data['rows'] = data
    commit('updateSensor2Data', parsed_data);
  },
  setSensor2NoData({commit, state}){
    const parsed_data = {}
    parsed_data['columns'] = []
    parsed_data['rows'] = []
    parsed_data['isLoading'] = false
    parsed_data['total'] = 0
    commit('updateSensor2Data', parsed_data);
  },
  updateRainChartDataApex({commit, state}, data){
    const x_labels = data.labels;
    let datasets = [];
    for (let i = 0; i < data.datasets.length; i++){
      datasets.push({
        name: data.datasets[i].label,
        data: data.datasets[i].data,
    })
    }
    state.rainApexData = datasets;
    // update of parent attribute required, otherwise the labels won't be displayed properly
    state.chartOptionsParsedApexRain = {
      ...state.chartOptionsParsedApexRain,
      ...{
        xaxis: {
          categories: x_labels
        }
      }
    }
  },
  updateMoistureChartDataApex({commit, state}, data){
    const x_labels = data.labels;
    let datasets = [];
    for (let i = 0; i < data.datasets.length; i++){
      datasets.push({
        name: data.datasets[i].label,
        data: data.datasets[i].data,
    })
    }
    state.moistureApexData = datasets;
    // update of parent attribute required, otherwise the labels won't be displayed properly
    state.chartOptionsParsedApexMoisture = {
      ...state.chartOptionsParsedApexMoisture,
      ...{
        xaxis: {
          categories: x_labels
        }
      }
    }
  }
};
const getters = {
  
};
export default {
  state,
  getters,
  actions,
  mutations,
}
