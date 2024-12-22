<template>
  <div class="flex flex-col items-center justify-center min-h-screen space-y-4 mt-12">
    <h1 class="text-3xl font-bold">留言板</h1>

    <!-- 模拟留言展示 -->
    <div class="mt-8 w-[48rem]">
      <h2 class="text-2xl font-semibold">历史留言</h2>
      <div class="mt-4 space-y-6"> <!-- 增加了更大的间距 -->
        <div class="bg-neutral p-4 rounded-md shadow-md">
          <p class="text-lg font-medium">用户1:</p>
          <p>这是一条模拟留言内容。感谢你们的努力！</p>
          <p class="text-sm text-gray-500 mt-2">2024-12-22</p> <!-- 添加日期 -->
        </div>
        <div class="bg-neutral p-4 rounded-md shadow-md">
          <p class="text-lg font-medium">用户2:</p>
          <p>这是另一条模拟留言。继续加油！</p>
          <p class="text-sm text-gray-500 mt-2">2024-12-21</p> <!-- 添加日期 -->
        </div>
      </div>
    </div>

    <!-- 留言输入框 -->
    <div class="mt-48">
      <textarea class="textarea textarea-accent w-[48rem] h-[16rem]" v-model="message" placeholder="留下你想说的话"></textarea>
    </div>

    <!-- 提交按钮 -->
    <button @click="submitMessage" class="btn btn-accent">提交</button>

    <!-- 提交后的提示 -->
    <div v-if="submitted" class="text-green-500 mt-4">
      谢谢您的留言！
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

// 留言内容的响应式变量
const message = ref('');

// 提交后的状态
const submitted = ref(false);

// 提交留言的函数
const submitMessage = () => {
  if (message.value.trim()) {
    // 模拟提交操作
    console.log('留言内容:', message.value);
    submitted.value = true;
    // 清空留言框
    message.value = '';
  } else {
    alert('留言不能为空');
  }
};
</script>

<style scoped>
/* 样式可以根据需求自定义 */
textarea {
  resize: none;
}

button {
  width: 100px;
}
</style>
