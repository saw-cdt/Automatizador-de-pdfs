import pdfkit
import jinja2

from datetime import datetime

client_name = 'Alex Quintanilla'

item1 = 'Tv'
item2 = 'Mueble'
item3 = 'Lavadora'

subtotal1 = 100
subtotal2 = 200
subtotal3 = 300
total = subtotal1 + subtotal2 + subtotal3

today_date = datetime.today().strftime('%d %b, %Y')
month = datetime.today().strftime('%B')

data = {'client_name': client_name, 'item1':item1, 'item2':item2, 'item3':item3, 'today_date':today_date, 
        'subtotal1':f'${subtotal1:.2f}', 'subtotal2':f'${subtotal2:.2f}', 'subtotal3':f'${subtotal3:.2f}',
        'total':f'${total:.2f}',
        'month':month}

template_loader = jinja2.FileSystemLoader('./src')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'factura.html'
template = template_env.get_template(html_template)
output_text = template.render(data)

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

output_pdf = 'contrato.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css=r'src\factura.css')