from flask import Flask, render_template_string
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Пример данных. В реальном приложении вы бы извлекали их из базы данных или другого источника.
    df = pd.DataFrame({
        'Month': ['January', 'February', 'March'],
        'Income': [1000, 1200, 1100]
    })
    
    fig = px.bar(df, x='Month', y='Income', title='Monthly Income')
    
    div = fig.to_html(full_html=False)
    
    return render_template_string("""
        <html>
            <head>
                <title>Finance Dashboard</title>
            </head>
            <body>
                {{ div|safe }}
            </body>
        </html>
    """, div=div)

if __name__ == '__main__':
    app.run(debug=True)
