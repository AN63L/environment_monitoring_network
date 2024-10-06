<template>
  <div role="alert">
    <div class="inline-flex min-w-80 px-4 py-2 rounded-lg text-sm text-white bg-red-500">
      <div class="flex w-full justify-between items-start">
        <div class="flex">
          <svg class="shrink-0 fill-current opacity-80 mt-[3px] mr-3" width="16" height="16" viewBox="0 0 16 16">
            <path d="M8 0C3.6 0 0 3.6 0 8s3.6 8 8 8 8-3.6 8-8-3.6-8-8-8zm3.5 10.1l-1.4 1.4L8 9.4l-2.1 2.1-1.4-1.4L6.6 8 4.5 5.9l1.4-1.4L8 6.6l2.1-2.1 1.4 1.4L9.4 8l2.1 2.1z" />
          </svg>
          <div class="font-medium">
            <p>API Unavailable. Please reload or check API connection</p>
          </div>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
export default {
  name: 'APIIndicatorToast',
  props: [],
}
</script>