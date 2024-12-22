<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '@/api';

const router = useRouter();
const messages = ref<any[]>([]);

const fetchMessages = async () => {
  try {
    const response = await apiClient.get('/');
    messages.value = Object.keys(response.data).map((key) => ({
      id: key,
      ...response.data[key],
    }));
  } catch (error) {
    console.error('Failed to fetch messages:', error);
  }
};

fetchMessages();

const handleReadNow = (id: string) => {
  const idWithoutExtension = id.replace(/\.md$/, '');

  router.push({
    name: 'PostDetail',
    params: { id: idWithoutExtension },
  });
};

</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen space-y-4 mt-36">
    <div class="card bg-neutral w-[48rem] h-[18rem] shadow-xl" v-for="message in messages" :key="message.id">
      <div class="card-body">
        <h2 class="card-title">{{ message.title }}</h2>
        <p>{{ message.date }}</p>
        <p class="tags">
          <span v-for="tag in message.tags" :key="tag" class="badge badge-outline">
            {{ tag }}
          </span>
        </p>
        <div class="card-actions justify-end">
          <button class="btn btn-primary" @click="handleReadNow(message.id)">Read Now</button>
        </div>
      </div>
    </div>
  </div>
</template>
