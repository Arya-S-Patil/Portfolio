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
        'description': 'This coffee table book explore the works of Gauri Gill, one of the most acclaimed contemporary photographers and my personal favourite. Her narratives in itself is awe inspiring in a sense that one can experience visually. This project deepened my understanding of conceptual storytelling and print production, allowing me to merge content, context and design into an immersive visual experience.',
        'images': [
            'static/assets/pub1/pub 2.png',
            'static/assets/pub1/pub 3.png',
            'static/assets/pub1/pub 4.png',
            'static/assets/pub1/pub 5.png',
            'static/assets/pub1/pub 6.png', 
        ]
    },
    {
        'id': 'pub-2',
        'title': 'Editorial Magazine Design',
        'category': 'Publication Design',
        'category_slug': 'publication',
        'image': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800',
        'gif': 'Sandy_Loading.gif',  # Project-specific GIF
        'description': 'A contemporary magazine layout exploring modern typography and grid systems.',
        'images': [
            'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=1200',
            'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=1200',
        ]
    },
    
    # Branding - 2 projects (will display as 1 row x 2 columns)
    {
        'id': 'brand-1',
        'title': 'Cafe Branding Identity',
        'category': 'Branding',
        'category_slug': 'branding',
        'image': 'https://images.unsplash.com/photo-1558655146-d09347e92766?w=800',
        'gif': 'project-brand-1.gif',  # Project-specific GIF
        'description': 'Complete brand identity for a sustainable coffee shop including logo, packaging, and collateral.',
        'images': [
            'https://images.unsplash.com/photo-1558655146-d09347e92766?w=1200',
            'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=1200',
        ]
    },
    {
        'id': 'brand-2',
        'title': 'Tech Startup Brand',
        'category': 'Branding',
        'category_slug': 'branding',
        'image': 'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=800',
        'gif': 'Sandy_Loading.gif',  # Project-specific GIF
        'description': 'Modern brand identity for an AI-focused tech startup with a bold visual language.',
        'images': [
            'https://images.unsplash.com/photo-1626785774573-4b799315345d?w=1200',
            'https://images.unsplash.com/photo-1558655146-d09347e92766?w=1200',
        ]
    },
    
    # Photo Essay - Single full-width project
    {
        'id': 'photo-1',
        'title': 'Urban Stories: Delhi Chronicles',
        'category': 'Photo Essay',
        'category_slug': 'photo',
        'image': 'https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=1200',
        'gif': 'Sandy_Loading.gif',  # Project-specific GIF
        'description': 'A photographic journey through the streets of Delhi, capturing daily life and architecture.',
        'images': [
            'https://images.unsplash.com/photo-1452587925148-ce544e77e70d?w=1200',
            'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1200',
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
        'description': 'Based on a brief by Ather Energy for the Kyoorius Young Blood Awards, Route Zero is a youth-led riders club built around the philosophy of zero, zero emissions and zero as a circle.This project was developed in collaboration alongside a friend, with equal credit shared for the concept and execution.',
        'images': [
            'static/assets/ather/ather 2.png',
            'static/assets/ather/ather 3.png',
            'static/assets/ather/ather 4.png',
            'static/assets/ather/ather 5.png',
            'static/assets/ather/ather 6.png',
            'static/assets/ather/ather 7.png',
            'static/assets/ather/ather 8.png',
            'static/assets/ather/ather 9.png',
            'static/assets/ather/ather 10.png',

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
        'description': 'A month-long daily design challenge exploring different creative disciplines.',
        'images': [
            'https://images.unsplash.com/photo-1561070791-2526d30994b5?w=1200',
            'https://images.unsplash.com/photo-1586717791821-3f44a563fa4c?w=1200',
        ]
    },
    
    # Blogs - Single full-width project
    {
        'id': 'blog-1',
        'title': 'Design & Writing Blog',
        'category': 'Blogs',
        'category_slug': 'blogs',
        'image': 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=1200',
        'gif': 'Sandy_Loading.gif',  # Project-specific GIF
        'description': 'A collection of blogs exploring design thinking, creativity, and the intersection of art and technology.',
        'images': [
            'https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=1200',
            'https://images.unsplash.com/photo-1455849318169-8e84fc2d37f0?w=1200',
        ]
    }
]

CATEGORIES = [
    {'name': 'All', 'slug': 'all'},
    {'name': 'Publication Design', 'slug': 'publication'},
    {'name': 'Branding', 'slug': 'branding'},
    {'name': 'Photo Essay', 'slug': 'photo'},
    {'name': 'Ather x Route Zero', 'slug': 'route'},
    {'name': '30 Days of Design', 'slug': 'design'},
    {'name': 'Blogs', 'slug': 'blogs'}
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