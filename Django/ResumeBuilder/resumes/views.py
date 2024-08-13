
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee,EmployeeProject
from django.template.loader import render_to_string

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.fonts import tt2ps
from reportlab.lib.fonts import addMapping
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from django.http import HttpResponse

import requests

def main(request):
    query = request.GET.get('q')
    print(query)
    if query:
        employees = Employee.objects.filter(name__icontains=query) 
    else:
        employees = Employee.objects.all()
    return render(request, 'main.html', {'employees': employees})

def employee_details(request):
    emp_id = request.GET.get('empid')
    employee = get_object_or_404(Employee, empid=emp_id)
    employee_projects = EmployeeProject.objects.filter(employee=employee)
    return render(request, 'emp_details.html', {'employee': employee,'employee_projects':employee_projects})




def generate_pdf(request):
    # JSON data
    empid = request.GET.get('empid')
    print(empid)
    
    response = requests.get(f'http://127.0.0.1:8000/api/employee_project_detail/?empid={empid}')

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        return HttpResponse(f"Request failed with status code {response.status_code}") 


    employee = Employee.objects.get(empid=empid).name
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{employee}.pdf"'


    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER)) # type: ignore
    
    elements.append(Paragraph(f"{data['name']}'s Resume", styles['Title']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph(f"<b>Employee ID:</b> {data['empid']}", styles['Normal']))
    elements.append(Paragraph(f"<b>Email:</b> {data['email']}", styles['Normal']))
    elements.append(Paragraph(f"<b>Phone:</b> {data['phone']}", styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Summary</b>", styles['Heading2']))
    elements.append(Paragraph(data['summary'], styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Personal Information</b>", styles['Heading2']))
    elements.append(Paragraph(f"Address: {data['personal_info']['address']}", styles['Normal']))
    elements.append(Paragraph(f"Date of Birth: {data['personal_info']['date_of_birth']}", styles['Normal']))
    elements.append(Paragraph(f"Nationality: {data['personal_info']['nationality']}", styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Technical Skills</b>", styles['Heading2']))
    elements.append(Paragraph(data['technical_skills'], styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Projects</b>", styles['Heading2']))
    for project in data['projects']:
        elements.append(Paragraph(f"Project Name: {project['name']}", styles['Heading3']))
        elements.append(Paragraph(f"Description: {project['description']}", styles['Normal']))
        elements.append(Paragraph(f"Start Date: {project['start_date']}", styles['Normal']))
        elements.append(Paragraph(f"Role: {project['role']}", styles['Normal']))
        elements.append(Paragraph(f"Contributions: {project['contributions']}", styles['Normal']))
        elements.append(Spacer(1, 12))


    doc.build(elements)

    return response
