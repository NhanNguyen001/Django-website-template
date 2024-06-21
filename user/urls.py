from django.urls import path

from .views import (login_view, signup_view, verify_email, o_auth_login,
                    verification_alert, verification_resend, logout_view,
                    guest_login_view
                    )


urlpatterns = [

    path('guest/login/', guest_login_view, name='guest-login'),
    path('logout/', logout_view, name='logout'),
    # path('signup/', signup_view, name='signup'),
    path('email/verify/', verify_email, name='verify-email'),

    path('email/verification/resend/', verification_resend, name='resend-verification'),
    path('email/verification-alert/', verification_alert, name='verification-alert'),

]
