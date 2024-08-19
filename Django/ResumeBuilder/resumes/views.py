
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee,EmployeeProject
from django.template.loader import render_to_string

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image, ListFlowable, ListItem
from reportlab.lib.enums import TA_LEFT
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


def header(canvas, header_img_path):
    canvas.saveState()
    header_img = Image(header_img_path, 6.5 * inch, 1 * inch)
    header_img.drawOn(canvas, 0.75 * inch, 10.5 * inch) 
    canvas.restoreState()
    canvas.translate(0, -0.35 * inch)

def generate_pdf(request):
    empid = request.GET.get('empid')
    
    response = requests.get(f'http://127.0.0.1:8000/api/employee_project_detail/?empid={empid}')

    if response.status_code == 200:
        data = response.json()
    else:
        return HttpResponse(f"Request failed with status code {response.status_code}") 


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{data['name']}.pdf"'


    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Bullet2', alignment=TA_LEFT, leftIndent=20))
    header_img_path = '/Users/mchinmayaraogmail.com/Downloads/image.png' 

    elements.append(Paragraph(f"<b>Name:</b> {data['name']}", styles['Normal']))
    elements.append(Paragraph(f"<b>Email:</b> {data['email']}", styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Professional Summary</b>", styles['Heading2']))
    elements.append(Paragraph("<bullet>&bull;</bullet>" + data['summary'], styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Personal Information</b>", styles['Heading2']))
    personal_info = data['personal_info']
    elements.append(Paragraph(f"Address: {personal_info['address']}", styles['Normal']))
    elements.append(Paragraph(f"Date of Birth: {personal_info['date_of_birth']}", styles['Normal']))
    elements.append(Paragraph(f"Nationality: {personal_info['nationality']}", styles['Normal']))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Technical Skill Set</b>", styles['Heading2']))
    bullet_points = [ListItem(Paragraph(skill, styles['Bullet2'])) for skill in data['technical_skills'].split(',')]
    elements.append(ListFlowable(bullet_points, bulletType='bullet', start='\u2022'))
    elements.append(Spacer(1, 12))


    elements.append(Paragraph("<b>Professional Projects</b>", styles['Heading2']))
    for project in data['projects']:
        elements.append(Paragraph(f"<b>Project Name:</b> {project['name']}", styles['Heading3']))
        elements.append(Paragraph(f"<b>Description:</b> {project['description']}", styles['Normal']))
        elements.append(Paragraph(f"<b>Start Date:</b> {project['start_date']}", styles['Normal']))
        elements.append(Paragraph(f"<b>Role:</b> {project['role']}", styles['Normal']))
        elements.append(Paragraph("<b>Contributions:</b>", styles['Normal']))
        contributions_bullets = [ListItem(Paragraph(contribution, styles['Bullet2'])) for contribution in project['contributions'].split(',')]
        elements.append(ListFlowable(contributions_bullets, bulletType='bullet', start='\u2022'))
        elements.append(Spacer(1, 12))


    doc.build(elements, onFirstPage=lambda canvas, doc: header(canvas, doc, header_img_path),
              onLaterPages=lambda canvas, doc: header(canvas, doc, header_img_path))

    return response
