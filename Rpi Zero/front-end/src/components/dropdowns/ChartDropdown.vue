<template>
  <div class="relative inline-flex max-h-10">
    <button
      ref="trigger"
      class="btn justify-between md:min-w-44 bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700/60 hover:border-gray-300 dark:hover:border-gray-600 text-gray-600 hover:text-gray-800 dark:text-gray-300 dark:hover:text-gray-100"
      aria-label="Select date range"
      aria-haspopup="true"
      @click.prevent="dropdownOpen = !dropdownOpen"
      :aria-expanded="dropdownOpen"
    >
      <span class="flex items-center">
        <span>{{options[selected].period}}</span>
      </span>
      <svg class="shrink-0 ml-1 fill-current text-gray-400 dark:text-gray-500" width="11" height="7" viewBox="0 0 11 7">
        <path d="M5.4 6.8L0 1.4 1.4 0l4 4 4-4 1.4 1.4z" />
      </svg>
    </button>
    <transition
      enter-active-class="transition ease-out duration-100 transform"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition ease-out duration-100"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-show="dropdownOpen" class="z-10 absolute top-full left-0 w-full bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700/60 py-1.5 rounded-lg shadow-lg overflow-hidden mt-1">
        <div
          ref="dropdown"
          class="font-medium text-sm text-gray-600 dark:text-gray-300"
          @focusin="dropdownOpen = true"
          @focusout="dropdownOpen = false"
        >

          <button
            v-for="option in options"
            :key="option.id"
            class="flex items-center w-full hover:bg-gray-50 hover:dark:bg-gray-700/20 py-1 px-3 cursor-pointer"
            :class="option.id === selected && 'text-violet-500'"
            @click="handleClick(option)"
          >
            <svg class="shrink-0 mr-2 fill-current text-violet-500" :class="option.id !== selected && 'invisible'" width="12" height="9" viewBox="0 0 12 9">
              <path d="M10.28.28L3.989 6.575 1.695 4.28A1 1 0 00.28 5.695l3 3a1 1 0 001.414 0l7-7A1 1 0 0010.28.28z" />
            </svg>
            <span>{{option.period}}</span>
          </button>          
        </div>
      </div>
    </transition>
    <button v-if="reload" class="ml-2" @click="handleClick({
        id: 0,
        period: 'Today',
        value: 0,
      })">
          <svg xmlns="http://www.w3.org/2000/svg" height="18" width="18" viewBox="0 0 18 18"><title>refresh 2</title><g stroke-width="1.5" fill="none" stroke="#212121" class="nc-icon-wrapper"><polyline points="8.5 12.75 10.75 15 8.5 17.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><path d="M4.952,4.238c-1.347,1.146-2.202,2.855-2.202,4.762,0,3.452,2.798,6.25,6.25,6.25,.579,0,1.14-.079,1.672-.226" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></path><polyline points="9.5 5.25 7.25 3 9.5 .75" stroke-linecap="round" stroke-linejoin="round"></polyline><path d="M13.048,13.762c1.347-1.146,2.202-2.855,2.202-4.762,0-3.452-2.798-6.25-6.25-6.25-.597,0-1.175,.084-1.722,.24" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        </button>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'ChartDropdown',
  props: {
    filterOptions: {
      type: Array,
      default: null,
    },
    reload: {
      type: Boolean,
      default: null,
    },
  },
  setup(props, context) {

    const dropdownOpen = ref(false)
    const trigger = ref(null)
    const dropdown = ref(null)    
    const selected = ref(0)

    const options = ref(props.filterOptions)

    // close on click outside
    const clickHandler = ({ target }) => {
      if (!dropdownOpen.value || dropdown.value.contains(target) || trigger.value.contains(target)) return
      dropdownOpen.value = false
    }

    // close if the esc key is pressed
    const keyHandler = ({ keyCode }) => {
      if (!dropdownOpen.value || keyCode !== 27) return
      dropdownOpen.value = false
    }

    onMounted(() => {
      document.addEventListener('click', clickHandler)
      document.addEventListener('keydown', keyHandler)
    })

    onUnmounted(() => {
      document.removeEventListener('click', clickHandler)
      document.removeEventListener('keydown', keyHandler)
    })    

    const handleClick = (option) => {
      selected.value = option.id
      dropdownOpen.value = false;
      context.emit('range-selected', option)
    }
    
    return {
      dropdownOpen,
      trigger,
      dropdown,
      selected,
      options,
      handleClick,
    }
  },
  methods: {
  }
}
</script>