<template>
  <Line :data="data" :options="chartOptions" />
</template>

<script>
import { chartOptions } from '@/utils/constants';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
  name: 'LineChart',
  props: ['data'],
  data: (props) => ({
    chartOptions
  }),
  components: {
    Line
  },
  setup(props) {}
}
</script>