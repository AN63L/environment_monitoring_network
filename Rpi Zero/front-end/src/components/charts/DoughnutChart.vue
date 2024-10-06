<template>
  <Doughnut :data="data" :options="chartOptions" />
</template>

<script>
import { chartOptions } from '@/utils/constants';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Doughnut } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  name: 'DoughtnutChar',
  props: ['data'],
  data: (props) => ({
    chartOptions
  }),
  components: {
    Doughnut
  },
  setup(props) {}
}
</script>