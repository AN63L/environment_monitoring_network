<template>
<div>
    <!-- Dashboard actions -->
    <div class="sm:flex sm:justify-between sm:items-center mb-8">

      <!-- Left: Title -->
      <div class="mb-4 sm:mb-0 grid grid-cols-2 gap-2">
        <h1 class="text-2xl md:text-3xl text-gray-800 dark:text-gray-100 font-bold">Notifications</h1>
        <button class="ml-2" @click="loadData">
          <svg xmlns="http://www.w3.org/2000/svg" height="18" width="18" viewBox="0 0 18 18"><title>refresh 2</title><g stroke-width="1.5" fill="none" stroke="#212121" class="nc-icon-wrapper"><polyline points="8.5 12.75 10.75 15 8.5 17.25" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></polyline><path d="M4.952,4.238c-1.347,1.146-2.202,2.855-2.202,4.762,0,3.452,2.798,6.25,6.25,6.25,.579,0,1.14-.079,1.672-.226" stroke-linecap="round" stroke-linejoin="round" stroke="#212121"></path><polyline points="9.5 5.25 7.25 3 9.5 .75" stroke-linecap="round" stroke-linejoin="round"></polyline><path d="M13.048,13.762c1.347-1.146,2.202-2.855,2.202-4.762,0-3.452-2.798-6.25-6.25-6.25-.597,0-1.175,.084-1.722,.24" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        </button>
      </div>
    </div>
    
    <div v-if="notifications == null" class="grid grid-cols-1 gap-6">
      <p>Could not acquire notifications statuses</p>
    </div>
    <!-- We added a key to force an update of the component, without it the status doesn't update -->
    <!-- the question mark is there to avoid error at initialisation where the attribute doesn't exist yet -->
    <div class="grid grid-cols-2 gap-6">
      <toggle title="Last sensor 1 update over 10 minutes ago" tooltip="Get notified when last sensor 1 update was over 10 minutes ago" :key="notifications?.sensor_1_last_update_over_10" :status="notifications?.sensor_1_last_update_over_10" toggle_type="sensor_1_last_update_over_10" @update-toggle="updateNotificationStatus"/>
      <toggle title="Last sensor 2 update over 10 minutes ago" tooltip="Get notified when last sensor 2 update was over 10 minutes ago" :key="notifications?.sensor_2_last_update_over_10" :status="notifications?.sensor_2_last_update_over_10" toggle_type="sensor_2_last_update_over_10" @update-toggle="updateNotificationStatus"/>
      <toggle title="Soil very dry" tooltip="Get notified when the soil is very dry" :key="notifications?.soil_very_dry" :status="notifications?.soil_very_dry" toggle_type="soil_very_dry" @update-toggle="updateNotificationStatus"/>
      <toggle title="Soil moist" tooltip="Get notified when the soil is moist" :key="notifications?.soil_very_moist" :status="notifications?.soil_very_moist" toggle_type="soil_very_moist" @update-toggle="updateNotificationStatus"/>
      <toggle title="Stopped raining" tooltip="Get notified when it stops raining" :key="notifications?.started_raining" :status="notifications?.started_raining" toggle_type="started_raining" @update-toggle="updateNotificationStatus"/>
      <toggle title="Started raining" tooltip="Get notified when it stops raining" :key="notifications?.stopped_raining" :status="notifications?.stopped_raining" toggle_type="stopped_raining" @update-toggle="updateNotificationStatus"/>
    </div>

  </div>

</template>

<script>
import Toggle from '@/components/toggles/Toggle.vue';
import apiRoutes from '@/utils/apiRoutes';
import { get, put } from '@/utils/apiMethods';

export default {
  name: 'Dashboard',
  components: {
    Toggle
  },
  data: (props) => ({
  }),
  mounted() {
    this.loadData();
  },
  computed: {
    notifications() {
      return this.$store.state.notifications.notifications;
    },
  },
  methods: {
    async loadData(){
      // get data from api
      const data = await get(apiRoutes.NOTIFICATIONS, false);
      if (data.data != null){;
        this.$store.dispatch('setNotifications', data.data);
      }
    },
    async updateNotificationStatus(filter, value){
      const data = await put(apiRoutes.UPDATE_NOTIFICATIONS(filter), true, {'value': value});
      this.$store.commit('updateNotificationAttribute', {filter, value});
    }
  }
}
</script>