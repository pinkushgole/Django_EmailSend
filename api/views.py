from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.response import Response
# # Create your views here.

class SendMail(APIView):
    def post(self, request):
        email_get=request.data.get('email')
        subject = 'OTP'
        body = 'otp is 1234'
        from_email = 'javaprogrammer0407@gmail.com'  # Sender email
        to_email = [email_get]  # Replace with recipient's email

        
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=from_email,
            to=to_email
        )

        try:
            # `fail_silently` is an argument for the `send` method, not the constructor
            email.send(fail_silently=False)
            return Response({'message': 'Email sent successfully'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
       
        