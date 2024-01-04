import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, KeepTogether

def generate_report(data, output_file='business_report.pdf'):
    # Create a PDF report
    pdf = SimpleDocTemplate(output_file, pagesize=letter)
    story = []

    # Add a title to the report
    title = "Business Quarterly Report"
    story.append(title)

    # Add content based on the data
    for department, group in data.groupby('Department'):
        story.append(f'\nDepartment: {department}')

        # Add details for each category and quarter
        table_data = [['Category', 'Quarter', 'Value']]
        for _, row in group.iterrows():
            table_data.append([row['Category'], row['Quarter'], row['Value']])

        # Create a table for the data and wrap it in KeepTogether
        table = Table(table_data)
        story.append(KeepTogether([table]))

    # Build the PDF
    pdf.build(story)

# Load data from the CSV file
data = pd.read_csv('business_data.csv')

# Generate the report
generate_report(data, output_file='business_report.pdf')
