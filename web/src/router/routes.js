
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/trainer/TrainersPage.vue') }
    ]
  },

  {
    path: '/trainees',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/trainee/TraineesPage.vue') }
    ]
  },
  {
    path: '/violation',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/violation/ViolationPage.vue') },
    ]
  },
  {
    path: '/section',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/department/SectionPage.vue') },

    ]
  },
  {
    path: '/login',
    component: () => import('pages/LoginPage.vue'),
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
