<template>
  <div>
  <div class="grow">
    <div class="flex flex-col col-span-full xl:col-span-8 bg-white dark:bg-gray-800 shadow-sm rounded-xl">
      <header class="px-5 py-4 border-b border-gray-100 dark:border-gray-700/60 flex items-center">
        <h2 class="font-semibold text-gray-800 dark:text-gray-100">{{title}}</h2>
        <button class="ml-2" @click="triggerReload">
          <svg xmlns="http://www.w3.org/2000/svg" height="18" width="18" viewBox="0 0 18 18"><title>refresh 2</title><g stroke-width="1.5" fill="none" stroke="#212121" class="nc-icon-wrapper"><polyline points="8.5 12.75 10.75 15 8.5 17.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><path d="M4.952,4.238c-1.347,1.146-2.202,2.855-2.202,4.762,0,3.452,2.798,6.25,6.25,6.25,.579,0,1.14-.079,1.672-.226" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></path><polyline points="9.5 5.25 7.25 3 9.5 .75" stroke-linecap="round" stroke-linejoin="round"></polyline><path d="M13.048,13.762c1.347-1.146,2.202-2.855,2.202-4.762,0-3.452-2.798-6.25-6.25-6.25-.597,0-1.175,.084-1.722,.24" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        </button>
      </header>
      <div class="px-5 py-1">
          <table-lite
            :is-loading="data.isLoading"
            :columns="data.columns"
            :rows="data.rows"
            :sortable="data.sortable"
            :total="data.totalRecordCount"
            :is-hide-paging="true"
          />
      </div>
    </div>
  </div>
</div>
</template>

<script>
import TableLite from "vue3-table-lite";
import { reactive } from "vue";

export default {
  name: 'GenericTableCard',
  props: ['title', 'data'],
  components: {
    TableLite
  },
  mounted(){
  },
  setup(props, context) {
    const triggerReload = () => {
      context.emit('reload')
    }
    return {triggerReload}
  },
  methods: {
  }
}
</script>