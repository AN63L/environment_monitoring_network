<template>
  <div class="min-w-fit">
    <!-- Sidebar backdrop (mobile only) -->
    <div class="fixed inset-0 bg-gray-900 bg-opacity-30 z-40 lg:hidden lg:z-auto transition-opacity duration-200" :class="sidebarOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'" aria-hidden="true"></div>

    <!-- Sidebar -->
    <div
      id="sidebar"
      ref="sidebar"
      class="flex lg:!flex flex-col absolute z-40 left-0 top-0 lg:static lg:left-auto lg:top-auto lg:translate-x-0 h-[100dvh] overflow-y-scroll lg:overflow-y-auto no-scrollbar w-64 lg:w-20 lg:sidebar-expanded:!w-64 2xl:!w-64 shrink-0 bg-white dark:bg-gray-800 p-4 transition-all duration-200 ease-in-out"
      :class="[variant === 'v2' ?  'border-r border-gray-200 dark:border-gray-700/60' : 'rounded-r-2xl shadow-sm', sidebarOpen ? 'translate-x-0' : '-translate-x-64']"
    >

      <!-- Sidebar header -->
      <div class="flex justify-between mb-10 pr-3 sm:px-2">
        <!-- Close button -->
        <button
          ref="trigger"
          class="lg:hidden text-gray-500 hover:text-gray-400"
          @click.stop="$emit('close-sidebar')"
          aria-controls="sidebar"
          :aria-expanded="sidebarOpen"
        >
          <span class="sr-only">Close sidebar</span>
          <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M10.7 18.7l1.4-1.4L7.8 13H20v-2H7.8l4.3-4.3-1.4-1.4L4 12z" />
          </svg>
        </button>
        <!-- Logo -->
        <router-link class="block" to="/">
          <img class="rounded-full ml-1" src="@/images/logo.svg" height="10%" alt="project logo" />
        </router-link>
      </div>

      <!-- Links -->
      <div class="space-y-8">
        <!-- Pages group -->
        <div>
      <!-- Links -->
    <h3 class="text-xs uppercase text-gray-400 dark:text-gray-500 font-semibold pl-3">
      <span class="hidden lg:block lg:sidebar-expanded:hidden 2xl:hidden text-center w-6" aria-hidden="true">•••</span>
      <span class="lg:hidden lg:sidebar-expanded:block 2xl:block">Analytics</span>
    </h3>
    <ul class="mt-3">
      <router-link to="/" custom v-slot="{ href, navigate, isExactActive }">
        <li class="pl-4 pr-3 py-2 rounded-lg mb-0.5 last:mb-0 bg-[linear-gradient(135deg,var(--tw-gradient-stops))]" :class="isExactActive && 'from-violet-500/[0.12] dark:from-violet-500/[0.24] to-violet-500/[0.04]'">
          <a class="block text-gray-800 dark:text-gray-100 truncate transition" :class="isExactActive ? '' : 'hover:text-gray-900 dark:hover:text-white'" :href="href" @click="navigate">
            <div class="flex items-center h-6">
              <svg class="shrink-0 fill-current" :class="isExactActive ? 'text-violet-500' : 'text-gray-400 dark:text-gray-500'" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path d="M5.936.278A7.983 7.983 0 0 1 8 0a8 8 0 1 1-8 8c0-.722.104-1.413.278-2.064a1 1 0 1 1 1.932.516A5.99 5.99 0 0 0 2 8a6 6 0 1 0 6-6c-.53 0-1.045.076-1.548.21A1 1 0 1 1 5.936.278Z" />
                <path d="M6.068 7.482A2.003 2.003 0 0 0 8 10a2 2 0 1 0-.518-3.932L3.707 2.293a1 1 0 0 0-1.414 1.414l3.775 3.775Z" />
              </svg> 
              <span class="text-sm font-medium ml-4 lg:opacity-0 lg:sidebar-expanded:opacity-100 2xl:opacity-100 duration-200">Dashboard</span>
            </div>
          </a>
        </li>
      </router-link>
      <router-link to="/graphs" custom v-slot="{ href, navigate, isExactActive }">
        <li class="pl-4 pr-3 py-2 rounded-lg mb-0.5 last:mb-0 bg-[linear-gradient(135deg,var(--tw-gradient-stops))]" :class="isExactActive && 'from-violet-500/[0.12] dark:from-violet-500/[0.24] to-violet-500/[0.04]'">
          <a class="block text-gray-800 dark:text-gray-100 truncate transition" :class="isExactActive ? '' : 'hover:text-gray-900 dark:hover:text-white'" :href="href" @click="navigate">
            <div class="flex items-center h-6">
              <svg class="shrink-0 fill-current" :class="isExactActive ? 'text-violet-500' : 'text-gray-400 dark:text-gray-500'" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <rect x="13.25" y="2.75" width="2.5" height="12.5" rx="1" ry="1" stroke-linecap="round" stroke-linejoin="round"></rect><rect x="7.75" y="7.75" width="2.5" height="7.5" rx="1" ry="1" stroke-linecap="round" stroke-linejoin="round"></rect><rect x="2.25" y="11.75" width="2.5" height="3.5" rx="1" ry="1" stroke-linecap="round" stroke-linejoin="round"></rect><polyline points="6.25 2.75 8.75 2.75 8.75 5.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><line x1="8.5" y1="3" x2="2.75" y2="8.75" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></line>
              </svg> 
              <span class="text-sm font-medium ml-4 lg:opacity-0 lg:sidebar-expanded:opacity-100 2xl:opacity-100 duration-200">Graphs</span>
            </div>
          </a>
        </li>
      </router-link> 
      <router-link to="/tables" custom v-slot="{ href, navigate, isExactActive }">
        <li class="pl-4 pr-3 py-2 rounded-lg mb-0.5 last:mb-0 bg-[linear-gradient(135deg,var(--tw-gradient-stops))]" :class="isExactActive && 'from-violet-500/[0.12] dark:from-violet-500/[0.24] to-violet-500/[0.04]'">
          <a class="block text-gray-800 dark:text-gray-100 truncate transition" :class="isExactActive ? '' : 'hover:text-gray-900 dark:hover:text-white'" :href="href" @click="navigate">
            <div class="flex items-center h-6">
              <svg class="shrink-0 fill-current" :class="isExactActive ? 'text-violet-500' : 'text-gray-400 dark:text-gray-500'" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path d="M6.649 1.018a1 1 0 0 1 .793 1.171L6.997 4.5h3.464l.517-2.689a1 1 0 1 1 1.964.378L12.498 4.5h2.422a1 1 0 0 1 0 2h-2.807l-.77 4h2.117a1 1 0 1 1 0 2h-2.501l-.517 2.689a1 1 0 1 1-1.964-.378l.444-2.311H5.46l-.517 2.689a1 1 0 1 1-1.964-.378l.444-2.311H1a1 1 0 1 1 0-2h2.807l.77-4H2.46a1 1 0 0 1 0-2h2.5l.518-2.689a1 1 0 0 1 1.17-.793ZM9.307 10.5l.77-4H6.612l-.77 4h3.464Z" />
              </svg> 
              <span class="text-sm font-medium ml-4 lg:opacity-0 lg:sidebar-expanded:opacity-100 2xl:opacity-100 duration-200">Tables</span>
            </div>
          </a>
        </li>
      </router-link>  
      <router-link to="/notifications" custom v-slot="{ href, navigate, isExactActive }">
        <li class="pl-4 pr-3 py-2 rounded-lg mb-0.5 last:mb-0 bg-[linear-gradient(135deg,var(--tw-gradient-stops))]" :class="isExactActive && 'from-violet-500/[0.12] dark:from-violet-500/[0.24] to-violet-500/[0.04]'">
          <a class="block text-gray-800 dark:text-gray-100 truncate transition" :class="isExactActive ? '' : 'hover:text-gray-900 dark:hover:text-white'" :href="href" @click="navigate">
            <div class="flex items-center h-6">
              <svg class="shrink-0 fill-current h-6" :class="isExactActive ? 'text-violet-500' : 'text-gray-400 dark:text-gray-500'" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <g class="nc-icon-wrapper"><line x1="14.5" y1="1.5" x2="16.5" y2="3.5" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></line><line x1="3.5" y1="1.5" x2="1.5" y2="3.5" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></line><circle cx="9" cy="9" r="6.25" stroke-linecap="round" stroke-linejoin="round"></circle><line x1="4.581" y1="13.419" x2="2.75" y2="15.25" stroke-linecap="round" stroke-linejoin="round"></line><line x1="13.419" y1="13.419" x2="15.25" y2="15.25" stroke-linecap="round" stroke-linejoin="round"></line><polyline points="9 5.75 9 9 11.75 10.75" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline></g>
              </svg> 
              <span class="text-sm font-medium ml-4 lg:opacity-0 lg:sidebar-expanded:opacity-100 2xl:opacity-100 duration-200">Notifications</span>
            </div>
          </a>
        </li>
      </router-link>  
    </ul>
    </div>
      </div>

      <!-- Expand / collapse button -->
      <div class="pt-3 hidden lg:inline-flex 2xl:hidden justify-end mt-auto">
        <div class="w-12 pl-4 pr-3 py-2">
          <button class="text-gray-400 hover:text-gray-500 dark:text-gray-500 dark:hover:text-gray-400" @click.prevent="sidebarExpanded = !sidebarExpanded">
            <span class="sr-only">Expand / collapse sidebar</span>
            <svg class="shrink-0 fill-current text-gray-400 dark:text-gray-500 sidebar-expanded:rotate-180" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path d="M15 16a1 1 0 0 1-1-1V1a1 1 0 1 1 2 0v14a1 1 0 0 1-1 1ZM8.586 7H1a1 1 0 1 0 0 2h7.586l-2.793 2.793a1 1 0 1 0 1.414 1.414l4.5-4.5A.997.997 0 0 0 12 8.01M11.924 7.617a.997.997 0 0 0-.217-.324l-4.5-4.5a1 1 0 0 0-1.414 1.414L8.586 7M12 7.99a.996.996 0 0 0-.076-.373Z" />
            </svg>
          </button>
        </div>
      </div>

      <div class="hidden lg:inline-flex 2xl:hidden justify-center">
        <div class="">
          <button class="text-gray-400 hover:text-gray-500 dark:text-gray-500 dark:hover:text-gray-400">
            <span v-if="sidebarExpanded" target="_blank" class="lg:block text-sm">version</span><span class="text-sm" target="_blank">{{ appVersion }}</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { version } from '../../package';

export default {
  name: 'Sidebar',
  props: [
    'sidebarOpen',
    'variant'
  ],
  components: {
  }, 
  setup(props, { emit }) {

    const appVersion= version;
    const trigger = ref(null)
    const sidebar = ref(null)

    const storedSidebarExpanded = localStorage.getItem('sidebar-expanded')
    const sidebarExpanded = ref(storedSidebarExpanded === null ? false : storedSidebarExpanded === 'true')

    const currentRoute = useRouter().currentRoute.value

    // close on click outside
    const clickHandler = ({ target }) => {
      if (!sidebar.value || !trigger.value) return
      if (
        !props.sidebarOpen ||
        sidebar.value.contains(target) ||
        trigger.value.contains(target)
      ) return
      emit('close-sidebar')
    }

    // close if the esc key is pressed
    const keyHandler = ({ keyCode }) => {
      if (!props.sidebarOpen || keyCode !== 27) return
      emit('close-sidebar')
    } 

    onMounted(() => {
      document.addEventListener('click', clickHandler)
      document.addEventListener('keydown', keyHandler)
    })

    onUnmounted(() => {
      document.removeEventListener('click', clickHandler)
      document.removeEventListener('keydown', keyHandler)
    })

    watch(sidebarExpanded, () => {
      localStorage.setItem('sidebar-expanded', sidebarExpanded.value)
      if (sidebarExpanded.value) {
        document.querySelector('body').classList.add('sidebar-expanded')
      } else {
        document.querySelector('body').classList.remove('sidebar-expanded')
      }
    })

    return {
      trigger,
      sidebar,
      sidebarExpanded,
      currentRoute,
      appVersion
    }
  },
}
</script>