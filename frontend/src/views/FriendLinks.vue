<script setup lang="ts">
// 定义友链数据类型
interface FriendLink {
  name: string; // 网站名称
  url: string;  // 网站链接
  description?: string; // 简介，可选
  logo?: string; // 网站 logo URL，可选
}

// 示例友链数据
const friendLinks: FriendLink[] = [
  {
    name: 'GitHub',
    url: 'https://github.com',
    description: 'Explore and share code repositories.',
    logo: 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png',
  },
  {
    name: 'TailwindCSS',
    url: 'https://tailwindcss.com',
    description: 'A utility-first CSS framework for rapid UI development.',
    logo: 'https://tailwindcss.com/_next/static/media/tailwindcss-mark.3c5441fc7a190fb1800d4a5c7f07ba4b1345a9c8.svg',
  },
  {
    name: 'DaisyUI',
    url: 'https://daisyui.com',
    description: 'A component library for TailwindCSS.',
    logo: 'https://daisyui.com/favicon.ico',
  },
  {
    name: 'TypeScript',
    url: 'https://www.typescriptlang.org',
    description: 'A superset of JavaScript that adds types.',
    logo: 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Typescript_logo_2020.svg',
  },
  {
    name: 'Python',
    url: 'https://www.python.org',
    description: 'The Python programming language.',
    logo: 'https://www.python.org/favicon.ico',
  },
  {
    name: 'Flask',
    url: 'https://flask.palletsprojects.com',
    description: 'A micro web framework written in Python.',
    logo: 'https://flask.palletsprojects.com/en/stable/_images/flask-horizontal.png',
  },
  {
    name: 'Git',
    url: 'https://git-scm.com',
    description: 'A distributed version control system.',
    logo: 'https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png',
  },
  {
    name: 'Node.js',
    url: 'https://nodejs.org',
    description: 'JavaScript runtime built on Chrome\'s V8 JavaScript engine.',
    logo: 'https://nodejs.org/static/images/logo.svg',
  },
  {
    name: 'Vue 3',
    url: 'https://vuejs.org',
    description: 'The Progressive JavaScript Framework.',
    logo: 'https://vuejs.org/images/logo.png',
  },
  {
    name: 'Vite',
    url: 'https://vitejs.dev',
    description: 'Next generation, front-end tooling.',
    logo: 'https://vitejs.dev/logo.svg',
  },
];
</script>

<template>
  <div class="mt-36">
    <div class="friend-links">
      <h1 class="text-2xl font-bold mb-4">Friend-links</h1>
      <ul class="grid grid-cols-2 gap-5">
        <li v-for="(link, index) in friendLinks" :key="index"
          class="p-4 border rounded-lg shadow hover:shadow-lg transition-shadow">
          <a :href="link.url" target="_blank" class="flex items-center gap-4">
            <img v-if="link.logo" :src="link.logo" alt="link.name" class="w-12 h-12 object-contain rounded-full" />
            <div>
              <h2 class="text-lg font-semibold text-blue-600 hover:underline">
                {{ link.name }}
              </h2>
              <p class="text-sm text-gray-600" v-if="link.description">
                {{ link.description }}
              </p>
            </div>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
/* 自定义样式 */
.friend-links {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>
