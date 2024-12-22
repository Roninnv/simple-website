<script setup lang="ts">
import Navbar from "@/components/Navbar.vue"
</script>

<template>
  <div class="grid grid-rows-[auto_auto] min-h-screen">
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<style scoped></style>
