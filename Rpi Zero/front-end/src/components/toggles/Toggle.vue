<template>
    <div class="bg-white border-2 shadow-sm rounded-xl flex justify-between items-center">
      <div class="flex items-center">
        <header class="px-5 py-4 ">
          <h2 class="font-semibold text-gray-800 dark:text-gray-100">{{title}}</h2>
        </header>
        <div>
            <tooltip v-if="tooltip" position="right" size="lg"><p class="text-sm">{{tooltip}}</p></tooltip>
        </div>
      </div>
      <div>
        <div class="flex items-center mr-4">
        <div class="text-sm text-gray-400 dark:text-gray-500 italic mr-2">{{isOn ? 'On' : 'Off'}}</div>
        <div class="form-switch" @click="handleUpdate">
        <input type="checkbox" :id="toggle_type" class="sr-only" v-model="isOn" :true-value="true" :false-value="false" :disabled="isOn == undefined || isOn == null"/>
        <label class="bg-gray-400 dark:bg-gray-700" for="isOn">
            <span class="bg-white shadow-sm" aria-hidden="true"></span>
            <span class="sr-only">{{title}}</span>
        </label>
        </div>
    </div>
      </div>
    </div>
</template>

<script>
import Tooltip from '@/components/tooltips/Tooltip.Vue'
import { ref } from 'vue'

export default {
  name: 'Toggle',
  props: {
    title: {
      type: String,
      default: null,
    },
    tooltip: {
      type: String,
      default: null,
    },
    status: {
      type: Boolean,
      default: true
    },
    toggle_type: {
      type: String,
      default: null,
    },
  },
  components: {
    Tooltip,
  },
  data: (props) => ({
    isOn: props.status
  }),
  mounted() {
  },
  setup(props, context){
  },
  computed: {
  },
  methods: {
    handleUpdate(){
      this.$emit('update-toggle', this.$props.toggle_type, !this.isOn)
    }
  }
}
</script>