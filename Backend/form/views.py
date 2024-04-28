from django.shortcuts import render

# Create your views here.
# from rest_framework import generics
# from .models import *
# from .serializers import LeadSerializer
# class LeadListCreateView(generics.ListCreateAPIView):
#     queryset=Lead.objects.all()
#     serializer_class=LeadSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import LeadSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
class LeadListCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            self.send_lead_email(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log the validation errors
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def send_lead_email(self,lead_data):
        subject='New Lead Submission'
        html_message = render_to_string('lead_email_template.html',{'lead':lead_data})
        plain_message = strip_tags(html_message)
        from_email = 'anaghapr2001@gmail.com'
        to=['anaghapr2001@gmail.com']
        send_mail(subject,plain_message,from_email,to,html_message=html_message)

        
# from django.core.mail import EmailMessage
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json

# @csrf_exempt
# def send_email(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email_subject = data['subject']
#         email_body = """
#         I trust this message finds you well.

#         On behalf of Loyal IT Solutions, I want to extend our sincere appreciation for expressing your interest in participating
#         in our ERP Implementation Joint Project Promotion. Your decision to explore this opportunity with us is truly valued, and we are excited about the prospect of collaborating with your team.

#         We understand the importance of a seamless ERP implementation, and we are committed to delivering a solution that not
#         only meets but exceeds your expectations. To ensure that we tailor our approach to your specific requirements, a representative from our team will be reaching out to you shortly.

#         Our goal is to understand your unique needs, address any questions you may have, and outline the details of our collaborative
#         venture. Your insights are invaluable, and we are dedicated to crafting a partnership that is mutually beneficial.

#         Thank you once again for considering Loyal IT Solutions for this endeavor. We look forward to the opportunity to work
#         together and will be in contact with you at the earliest convenience.

#         Best regards,
#         CTO
#         """

#         to_email = data['to']

#         email = EmailMessage(email_subject, email_body, to=[to_email])
#         email.send()

#         return JsonResponse({'message': 'Email sent successfully'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=400)

# class LeadListCreateView(generics.ListCreateAPIView):
#     queryset = Lead.objects.all()
#     serializer_class = LeadSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)

#             # Send email
#             email_subject = 'Lead Submission Confirmation'
#             email_body = 'Thank you for your lead submission!'
#             to_email = serializer.validated_data['email']
#             email = EmailMessage(email_subject, email_body, to=[to_email])
#             email.send()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             # Log the validation errors
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class LeadListCreateView(generics.ListCreateAPIView):
#     queryset = Lead.objects.all()
#     serializer_class = LeadSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)

#             # Send email
#             email_subject = 'Lead Submission Confirmation'
#             email_body = 'Thank you for your lead submission!'
#             to_email = serializer.validated_data['email']
#             email = EmailMessage(email_subject, email_body, to=[to_email])
#             email.send()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             # Log the validation errors
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from openpyxl import Workbook
from django.http import HttpResponse
def export_to_excel(request):
    backend_data=Lead.objects.all()
    wb=Workbook()
    ws=wb.active
    headers=['lead_no','Date','Company Name','Company Address','Country','Street','City','Contact Person','Contact No','Email','Designation','Company HeadQuarters','Business Verticals','Introuction of Project'] 
    ws.append(headers)

    for row in backend_data:
        ws.append([row.lead_no,row.date,row.company_name,row.company_address,row.country,row.street,row.city,row.contact_person,row.contact_no,row.email,row.designation,row.company_headquarters,row.business_verticals,row.additional_notes])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'

    # Save the workbook to the response
    wb.save(response)

    return response








# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags

# @csrf_exempt
# def send_form_data_email(request):
    if request.method == 'POST':
        form_data = json.loads(request.body)
        
     
        html_table = '<table border="1">'
        for key, value in form_data.items():
            html_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
        html_table += '</table>'

        html_content = render_to_string('email_template.html', {'form_data': form_data, 'html_table': html_table})
        plain_text_content = strip_tags(html_content)

        send_mail(
            subject='Form Submission',
            message=plain_text_content,
            from_email='anaghapr2001@gmail.com',
            recipient_list=['anaghapr2001@gmail.com'],
            html_message=html_content,
            fail_silently=False,
        )
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})