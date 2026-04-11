from flask import Flask, render_template, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# Project data - organized for the specific grid layout
PROJECTS = [
    # Publication Design - 2 projects (will display as 1 row x 2 columns)
    {
        'id': 'pub-1',
        'title': 'Lenses That Listen',
        'category': 'Publication Design',
        'category_slug': 'publication',
        'image': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=800',
        'gif': 'project-pub-1.gif',  # Project-specific GIF
        'flip_text': 'Publication Design',
        'description': 'This coffee table book explores the works of Gauri Gill, one of the most acclaimed contemporary photographers and my personal favourite. This project deepened my understanding of conceptual storytelling and print production, allowing me to merge content, context and design into an immersive visual experience.',
        'images': [
            'static/assets/pub1/pub 2.webp',
            'static/assets/pub1/pub 3.webp',
            'static/assets/pub1/pub 4.webp',
            'static/assets/pub1/pub 5.webp',
            'static/assets/pub1/pub 6.webp', 
        ]
    },
    {
        'id': 'pub-2',
        'title': 'Liminal - Margins of The Artist Way',
        'category': 'Publication Design',
        'category_slug': 'publication',
        'image': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800',
        'gif': 'Artist way zine .gif',  # Project-specific GIF
        'flip_text': 'Experimental Publication Design',
        'description': 'Picked up Julia Cameron\'s The Artist\'s Way last summer for a creative reset. This zine is a compilation of that journey, a walk-through ritual and releases. Check out the project for more context.',
        'images': [
            'static/assets/Artist way zine/1.webp',
            'static/assets/Artist way zine/2.webp',
            'static/assets/Artist way zine/3.webp',
            'static/assets/Artist way zine/4.webp',
            'static/assets/Artist way zine/5.webp',
            'static/assets/Artist way zine/6.webp',
            'static/assets/Artist way zine/7.webp',
            'static/assets/Artist way zine/8.webp',
            'static/assets/Artist way zine/9.webp',
            'static/assets/Artist way zine/10.webp',
            'static/assets/Artist way zine/11.webp',
            'static/assets/Artist way zine/12.webp',
            'static/assets/Artist way zine/13.webp',
            'static/assets/Artist way zine/14.webp',
            'static/assets/Artist way zine/15.GIF',
            'static/assets/Artist way zine/last_video.webm'
        ]
    },
    
    # Branding - 2 projects (will display as 1 row x 2 columns) Currently just 1
    {
        'id': 'brand-1',
        'title': 'Breakvox',
        'category': 'Branding',
        'category_slug': 'branding',
        'image': 'https://images.unsplash.com/photo-1558655146-d09347e92766?w=800',
        'gif': 'project-brand-1.gif',  # Project-specific GIF
        'flip_text': 'Brand and Visual Identity',
        'description': 'BreakVox is a vibrant music platform dedicated to spotlight independent artists and niche taste. With bold and expressive identity, BreakVox goes beyond casual streaming, building real and meaningful experiences. ',
        'images': [
            'static/assets/Beakvox branding project/b1.gif',
            'static/assets/Beakvox branding project/b2.webp',
            'static/assets/Beakvox branding project/b3.webp',
            'static/assets/Beakvox branding project/b4.webp',
            'static/assets/Beakvox branding project/b5.webp',
            'static/assets/Beakvox branding project/b6.webp',
            'static/assets/Beakvox branding project/b7.webp',
            'static/assets/Beakvox branding project/b8.webp',
            'static/assets/Beakvox branding project/b9.webp',
            'static/assets/Beakvox branding project/b10.webp',
            'static/assets/Beakvox branding project/b11.webp',
            'static/assets/Beakvox branding project/b12.webp',
            'static/assets/Beakvox branding project/b13.webp',
            'static/assets/Beakvox branding project/breakvox logo process gif b4.gif'

        ]
    },
  
    # Ather x Route Zero - Single full-width project
    {
        'id': 'route-1',
        'title': 'Ather x Route Zero Collaboration',
        'category': 'Ather x Route Zero',
        'category_slug': 'route',
        'image': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1200',
        'gif': 'project-route-1.gif',  # Project-specific GIF
        'flip_text': 'Branding and Campaign Design',
        'description': 'Based on a brief by Ather Energy for the Kyoorius Young Blood Awards, Route Zero is a youth-led riders club built around the philosophy of zero, zero emissions and zero as a circle.This project was developed in collaboration alongside a friend, with equal credit shared for the concept and execution.',
        'images': [
            'static/assets/ather/ather 2.webp',
            'static/assets/ather/ather 3.webp',
            'static/assets/ather/ather 4.webp',
            'static/assets/ather/ather 5.webp',
            'static/assets/ather/ather 6.webp',
            'static/assets/ather/ather 7.webp',
            'static/assets/ather/ather 8.webp',
            'static/assets/ather/ather 9.webp',
            'static/assets/ather/ather 10.webp',

        ]
    },
    
    # 30 Days of Design - Single full-width project
    {
        'id': 'design-1',
        'title': '30 Days of Design Challenge',
        'category': '30 Days of Design',
        'category_slug': 'design',
        'image': 'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=1200',
        'gif': 'project-design-1.gif',  # Project-specific GIF
        'flip_text': 'Graphic Exploration.',
        'description': 'Born purely out of passion, an unrecognised void led me to tell stories beyond any external pressure, simply allowing creativity to flow. While I have grown since this project, I still keep it as an account of that vulnerable expression. The following is just a glimpse, for a closer look, check out my Instagram.',
        'images': [
            'static/assets/30 days of design/1.gif',
            'static/assets/30 days of design/1.png',
            'static/assets/30 days of design/2.png',
            'static/assets/30 days of design/3.png',       
        ]
    },
    
   
]

CATEGORIES = [
    {'name': 'All', 'slug': 'all'},
    {'name': 'Publication Design', 'slug': 'publication'},
    {'name': 'Branding', 'slug': 'branding'},
    
    {'name': 'Ather x Route Zero', 'slug': 'route'},
    {'name': '30 Days of Design', 'slug': 'design'},
   
]

@app.route('/')
def index():
    """Main page route"""
    return render_template('index.html', categories=CATEGORIES, projects=PROJECTS)

@app.route('/api/projects')
def get_projects():
    """API endpoint to get all projects"""
    return jsonify(PROJECTS)

@app.route('/api/projects/<category>')
def get_projects_by_category(category):
    """API endpoint to get projects by category"""
    if category == 'all':
        return jsonify(PROJECTS)
    filtered = [p for p in PROJECTS if p['category_slug'] == category]
    return jsonify(filtered)

@app.route('/api/contact', methods=['POST'])
def contact():
    """Contact form submission endpoint"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400
        
        # In demo mode, just print to console
        print(f"\n--- New Contact Form Submission ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"-----------------------------------\n")
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'}), 200
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to process request'}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)