from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial (manifesto)
@app.route('/')
def home():
    manifesto_text = """
    <h1>Manifesto for AI for Happiness</h1>
    <p>Happiness is the ultimate goal of life.</p>
    <p>We believe that AI should be developed and used to enhance human well-being, promoting a happier and healthier society. Join us in our mission to integrate happiness as a core objective in AI design and implementation.</p>
    <p>Our vision is to create an ecosystem where technology serves humanity's greatest needs. We advocate for:</p>
    <ul>
        <li>Ethical AI practices that prioritize human welfare.</li>
        <li>Transparent algorithms that foster trust and accountability.</li>
        <li>Collaborative efforts between technologists, psychologists, and community leaders to shape a better future.</li>
    </ul>
    <p>Together, we can harness the power of AI to make a positive impact on society.</p>
    <p>For more information and resources, please visit our <a href="/dashboard">Dashboard</a> to explore data related to AI and happiness.</p>
    """
    return render_template('index.html', manifesto=manifesto_text)

# Rota para o dashboard (pode ser expandido depois)
@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard for AI and Happiness Data</h1>"

if __name__ == '__main__':
    app.run(debug=True)
