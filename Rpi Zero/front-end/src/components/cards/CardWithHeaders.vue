<template>
  <div class="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl p-4">
    <div class="flex flex-wrap">
      <header class="px-5 py-4 border-b border-gray-100 dark:border-gray-700/60 flex items-center">
        <h2 class="font-semibold text-gray-800 dark:text-gray-100">{{title}}</h2>
      </header>
      <tooltip v-if="tooltip" class="mt-3" position="top0" size="lg"><p class="text-sm">{{tooltip}}</p></tooltip>
    </div>
    <div class="px-5 py-1 ">
      <div :class='`flex flex-wrap max-sm:*:w-1/2 grid grid-cols-${cols} gap-4 items-center`'>
        <card-header v-for="header in headers" :key="header" :header="header"/>
      </div>
    </div>
    <div class="grow">
      <slot/>
    </div>
  </div>
</template>

<script>
import CardHeader from './CardHeader.vue';
import Tooltip from '@/components/tooltips/Tooltip.vue';

 export default {
  name: 'CardWithHeaders',
  props: ['title', 'headers', 'cols', 'tooltip'],
  // data: (props) => ({
  //   title: props.title,
  //   headers: props.headers
  // }),
  components: {
    CardHeader,
    Tooltip
  },
  setup() {
  }
}
</script>