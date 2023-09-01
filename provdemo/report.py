def write_html(df):
    # Convert the DataFrame to an HTML table
    html_table = df.to_html(index=False)

    # Define the HTML template
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Provenance Report</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                border: 1px solid #ddd;
            }}

            th, td {{
                text-align: left;
                padding: 8px;
            }}

            th {{
                background-color: #f2f2f2;
            }}

            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Provenance Report</h1>
        {html_table}
    </body>
    </html>
    """

    # Write the HTML template to a file
    with open("provenance_report.html", "w") as file:
        file.write(html_template)
