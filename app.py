from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage (manifesto)
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

@app.route('/statistics')
def statistics():
    stats_text = """
    <ul>
        <li><strong>Mental Health Apps:</strong> About 80% of users of mental health apps report feeling better after using them.</li>
        <li><strong>AI Chatbots:</strong> 60% of users feel more comfortable discussing mental health issues with AI chatbots than with human therapists.</li>
        <li><strong>User Satisfaction:</strong> 75% of people using AI-based recommendations for personal well-being reported increased happiness.</li>
        <li><strong>Increased Productivity:</strong> AI tools improve productivity by 40%, leading to lower stress and increased life satisfaction.</li>
        <li><strong>Global Reach:</strong> 50% of people worldwide believe technology will significantly improve their mental health in the next decade.</li>
    </ul>
    """
    return render_template('statistics.html', statistics=stats_text)


# Dashboard route (can be expanded later)
@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard for AI and Happiness Data</h1>"

if __name__ == '__main__':
    app.run(debug=True)
