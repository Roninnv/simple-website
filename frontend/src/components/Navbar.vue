<script setup lang="ts">
</script>

<template>
  <div class="navbar fixed bg-base-300 z-50">
    <div class="navbar-start">
      <a class="btn btn-ghost text-xl">QAQ</a>
    </div>
    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li><router-link to="/">主页</router-link></li>
        <li><router-link to="/contact">留言</router-link></li>
        <li><router-link to="/friendLinks">友链</router-link></li>
        <li><router-link to="/about">关于</router-link></li>
      </ul>
    </div>
    <div class="navbar-end">
    </div>
  </div>
</template>