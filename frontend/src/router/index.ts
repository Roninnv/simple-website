import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";
import Contact from "@/views/Contact.vue";
import FriendLinks from "@/views/FriendLinks.vue";
import About from "@/views/About.vue";
import PostDetail from "@/views/PostDetail.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/friendLinks",
    name: "FriendLinks",
    component: FriendLinks,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/:id",
    name: "PostDetail",
    component: PostDetail,
    props: true, // 使路由参数成为组件的 props
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
