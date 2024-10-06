<template>

    <div class="max-w-2xl m-auto mt-16">

      <div class="text-center px-4">
        <div class="inline-flex mb-8">
          <img class="dark:hidden" src="@/images/404.gif" width="176" height="176" alt="404 illustration" />
        </div>
        <div class="mb-6">Hmm...this page doesn't exist. Try searching for something else!</div>
        <router-link to="/" class="btn bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-gray-100 dark:text-gray-800 dark:hover:bg-white">Back To Dashboard</router-link>
      </div>

    </div>

</template>

<script>
import Wrapper from '@/containers/Wrapper.vue'

export default {
  name: 'PageNotFound',
  components: {
    Wrapper,
  },
}
</script>