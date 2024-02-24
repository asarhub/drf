from rest_framework.throttling import UserRateThrottle


class CustomRateThrottle(UserRateThrottle):
    #Here user can click maximum three hits for an API. After that it will throttle
    rate = '3/hour'
