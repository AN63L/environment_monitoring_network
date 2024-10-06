<template>
  <Bar :data="data" :options="chartOptions" />
</template>

<script>
import { chartOptions } from '@/utils/constants';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  name: 'BarChart',
  props: ['data'],
  data: (props) => ({
    chartOptions
  }),
  components: {
    Bar
  },
  setup(props) {}
}
</script>