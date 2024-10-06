<template>
  <apexchart type="bar" :options="chartOptions" :series="data"></apexchart>
</template>

<script>

export default {
  name: 'StackedBarChart',
  props: ['data', 'chartOptions'],
  data: (props) => ({
  }),
  components: {
    
  },
  setup(props) {
}
}
</script>