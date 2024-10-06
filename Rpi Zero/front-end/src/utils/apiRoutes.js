export default {
    HEALTH: '/health',
    LATEST: '/metrics/latest',
    CHART: (chartId) => `/metrics/charts/${chartId}`,
    SENSOR_1:'/metrics/sensor_1',
    SENSOR_2: '/metrics/sensor_2', 
    NOTIFICATIONS: '/notifications', 
    UPDATE_NOTIFICATIONS: (notification_type) => `/notifications/${notification_type}`, 
}