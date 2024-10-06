<template>
  <div class="bg-white border-2 shadow-sm rounded-xl grid sm:grid-cols-1 md:grid-cols-1 md:gap-1">
    <div class="flex flex-wrap">
      <header class="px-5 py-4 ">
        <h2 class="font-semibold text-gray-800 dark:text-gray-100">{{title}}</h2>
      </header>
      <tooltip v-if="tooltip" class="mt-3" position="top" size="lg"><p class="text-sm">{{tooltip}}</p></tooltip>
    </div>
    <chart-dropdown v-if="filter" :filterOptions="filterOptions" @range-selected="handleRangeClick" class="ml-3" reload/>
    <slot/>
  </div>
</template>

<script>
import ChartDropdown from '@/components/dropdowns/ChartDropdown.vue'
import Tooltip from '@/components/tooltips/Tooltip.vue';

export default {
  name: 'GenericCard',
  props: {
    title: {
      type: String,
      default: null,
    },
    filter: {
      type: Boolean,
      default: false,
    },
    tooltip: {
      type: String,
      default: null,
    },
    filterOptions: {
      type: Array,
      default: null,
    },
    chartId: {
      type: String,
      default: null,
    },
    reload: {
      type: Boolean,
      default: null,
    },
  },
  components: {
    ChartDropdown,
    Tooltip,
  },
  setup(props, context) {
    const handleRangeClick = (value) => {
      context.emit('updated-filter', [value, props.chartId])
    }
    return {handleRangeClick}
  },
  methods: {
    
  }
}
</script>