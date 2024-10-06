<template>
  <!-- Unique Visitors -->
  <div class="flex items-center py-2 border-2 justify-center rounded-xl mt-2">
    <div class="mr-2">
      <div class="flex items-center justify-center">
        <div class="text-2xl font-bold text-gray-800 dark:text-gray-100 mr-2">{{header.value}} {{' '}}</div>
        <div class="text-1xl font-medium text-gray-800 dark:text-gray-100">{{header.metric}}</div>
        <div class="text-sm font-medium text-green-600">{{header.header_value}}</div>
      </div>
      <div class="text-sm text-gray-500 dark:text-gray-400 flex items-center justify-center">{{header.legend}}</div>
    </div>
    <!-- <div class="hidden md:block w-px h-8 bg-gray-200 dark:bg-gray-700 mr-5" aria-hidden="true"></div> -->
  </div>
</template>

<script>
export default {
  name: 'CardHeader',
  props: ['header'],
  components: {
  },
  setup() {
  }
}
</script>