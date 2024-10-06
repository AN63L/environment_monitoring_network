import { createRouter, createWebHistory } from 'vue-router'

const Wrapper = () => import('@/containers/Wrapper.vue');
const Dashboard = () => import('@/pages/Dashboard.vue');
const Graphs = () => import('@/pages/Graphs.vue');
const Tables = () => import('@/pages/Tables.vue');
const Notifications = () => import('@/pages/Notifications.vue');
const PageNotFound = () => import('@/pages/PageNotFound.vue');

function configRoutes() {
    return [
      {
        path: '/:pathMatch(.*)*',
        component: PageNotFound,
      },
      {
        path: '/',
        component: Wrapper,
        children: [
          {
            path: '/',
            name: 'Dashboard',
            component: Dashboard,
          },
          {
            path: '/graphs',
            name: 'Graphs',
            component: Graphs,
          },
          {
            path: '/tables',
            name: 'Tables',
            component: Tables,
          },
          {
            path: '/notifications',
            name: 'Notifications',
            component: Notifications,
          },
        ],
      },
    ];
  }

const routerHistory = createWebHistory()

const router = createRouter({
history: routerHistory,
scrollBehavior: () => ({ y: 0 }),
routes: configRoutes(),
})
export default router;