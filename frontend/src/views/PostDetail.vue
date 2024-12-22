<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import apiClient from '@/api';

const messageContent = ref<string>('');

const route = useRoute();

onMounted(async () => {
  const id = route.params.id as string;

  try {
    const response = await apiClient.get(`/md-files/${id}.md`);
    messageContent.value = response.data;
  } catch (error) {
    console.error('获取消息失败:', error);
  }
});
</script>

<template>
  <div class="flex items-start min-h-screen">
    <div class="mockup-window bg-base-300 border w-[800px] max-h-[90vh] overflow-y-auto mx-auto mt-20">
      <div class="bg-base-200 px-4 py-16">
        <div v-if="messageContent">
          <div v-html="messageContent"></div>
        </div>
        <div v-else>
          <p>Loading...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>