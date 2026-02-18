# CLIMBING.IN Portfolio Website

A modern, interactive portfolio website with flipping stickers, animations, and responsive design.

## 🎨 Features

- **Loading Screen**: Animated GIF on page load
- **Interactive Hero Section**: Flippable central image, 4 stickers, and logo banner
- **Projects Section**: Filterable project grid with scroll-triggered animations
- **About Section**: Personal bio with animated portrait GIF
- **Contact Section**: Email, phone, and social media links
- **Resume Modal**: In-page PDF viewer with download option
- **Project Detail Modal**: Full project galleries with navigation
- **Fully Responsive**: Mobile-first design with media queries

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the application**:
```bash
python app.py
```

3. **Open in browser**:
```
http://localhost:10000
```

## 📁 File Structure

```
Portfolio/
├── app.py                      # Flask application
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # Main HTML template
├── static/
│   ├── css/
│   │   ├── style.css          # All styles
│   │   └── style.css.bak      # Backup
│   ├── js/
│   │   └── main.js            # All JavaScript
│   ├── images/                # Hero section images
│   │   ├── profile.png        # Central image (front)
│   │   ├── profile-back.png   # Central image (back)
│   │   ├── sticker1.png       # Sticker 1 (front)
│   │   ├── sticker1-back.png  # Sticker 1 (back)
│   │   ├── sticker2.png       # Sticker 2 (front)
│   │   ├── sticker2-back.png  # Sticker 2 (back)
│   │   ├── sticker3.png       # Sticker 3 (front)
│   │   ├── sticker3-back.png  # Sticker 3 (back)
│   │   ├── sticker4.png       # Sticker 4 (front)
│   │   ├── sticker4-back.png  # Sticker 4 (back)
│   │   ├── portrait.gif       # Animated portrait
│   │   ├── behance-icon.png   # Social icon
│   │   ├── instagram-icon.png # Social icon
│   │   ├── linkedin-icon.png  # Social icon
│   │   └── medium-icon.png    # Social icon
│   └── assets/
│       ├── loading.gif        # Loading screen animation
│       ├── loading2.gif       # Alternative loading
│       ├── resume.pdf         # Your resume PDF
│       ├── projects/          # Project-specific GIFs
│       │   ├── project-pub-1.gif
│       │   ├── project-pub-2.gif
│       │   ├── project-brand-1.gif
│       │   ├── project-brand-2.gif
│       │   ├── project-photo-1.gif
│       │   ├── project-route-1.gif
│       │   ├── project-design-1.gif
│       │   ├── project-blog-1.gif
│       │   └── Sandy_Loading.gif
│       ├── pub1/              # Publication project images
│       │   ├── pub 2.png
│       │   ├── pub 3.png
│       │   ├── pub 4.png
│       │   ├── pub 5.png
│       │   └── pub 6.png
│       └── ather/             # Ather x Route Zero images
│           ├── ather 2.png
│           ├── ather 3.png
│           ├── ather 4.png
│           ├── ather 5.png
│           ├── ather 6.png
│           ├── ather 7.png
│           ├── ather 8.png
│           ├── ather 9.png
│           └── ather 10.png
```

## 🎨 Customization Guide

### 1. Replace Demo Images

All demo images are **placeholder images**. Replace them with your actual images:

#### Hero Section Images
- `static/images/profile.png` - Your main profile photo (400x400px recommended)
- `static/images/profile-back.png` - Alternative profile image (same size)
- `static/images/sticker1.png` to `sticker4.png` - Your sticker designs
- `static/images/sticker1-back.png` to `sticker4-back.png` - Sticker backs
- `static/images/logo-back.png` - Logo banner back image

#### About Section
- `static/images/illustration.png` - Your illustration (400x500px)
- `static/images/portrait.gif` - Animated portrait (300x400px)

#### GIFs
- `static/assets/loading.gif` - Loading animation
- `static/assets/loading2.gif` - Alternative loading animation

#### Social Icons
- Replace all `*-icon.png` files with actual social media icons (80x80px)

#### Resume
- `static/assets/resume.pdf` - **REPLACE WITH YOUR ACTUAL RESUME**

### 2. Update Content

#### Personal Information (templates/index.html)

**About Section** (lines 245-260):
```html
<p class="about-intro">
    Morning! I'm <strong>YOUR NAME</strong>, an aspiring...
    <!-- Update with your bio -->
</p>
```

**Poem** (lines 265-276):
```html
<blockquote>
    <!-- Replace with your own poem or remove this section -->
</blockquote>
```

**Contact Info** (lines 355-365):
```html
<a href="mailto:YOUR_EMAIL@gmail.com" class="contact-email">
    YOUR_EMAIL@gmail.com
</a>

<a href="tel:+91YOUR_PHONE" class="contact-phone">
    +91 YOUR_PHONE
</a>
```

#### Projects (app.py)

Edit the `PROJECTS` array (lines 7-135):

**Project Data Structure**:
```python
{
    'id': 'unique-id',
    'title': 'Project Title',
    'category': 'Category Name',
    'category_slug': 'category-slug',
    'image': 'https://image-url.jpg',  # Static thumbnail
    'gif': 'project-name.gif',         # Animated GIF
    'description': 'Your description',
    'images': [
        'static/assets/folder/image1.png',
        'static/assets/folder/image2.png'
    ]
}
```

**Important Project Requirements**:
- **Static image**: URL or local path shown initially
- **GIF filename**: Placed in `static/assets/projects/`
- **Category slug**: Must match a category in `CATEGORIES`
- **Images array**: Can be URLs or local asset paths

#### Categories

Edit `CATEGORIES` array in app.py (lines 137-145). The structure is:
```python
{'name': 'Display Name', 'slug': 'url-slug'}
```

The `slug` must match the `category_slug` used in your projects. Current categories:
- `publication` - Publication Design
- `branding` - Branding
- `photo` - Photo Essay
- `route` - Ather x Route Zero
- `design` - 30 Days of Design
- `blogs` - Blogs

### 3. Customize Colors

Edit CSS variables in `static/css/style.css` (lines 10-16):
```css
:root {
    --neon-green: #B8FF3C;       /* Primary accent - titles & highlights */
    --dark-bg: #1a1a1a;          /* Light dark background */
    --darker-bg: #0f0f0f;        /* Darker background */
    --cream: #F5F0E8;            /* Text color */
    --pink: #D64C7F;             /* Secondary accent - banners */
    --pink-light: #E57FA0;       /* Light pink variant */
}
```

**Background Pattern**: Sections alternate between `--dark-bg` and `--darker-bg` for visual contrast.

### 4. Fonts

Current fonts (from Google Fonts):
- **Rubik Vinyl** - Section titles and banners
- **Work Sans** - Body text

To change fonts, update the Google Fonts link in `templates/index.html` (line 11) and the CSS font-family declarations.

### 5. Social Media Links

Update social media URLs in `templates/index.html` (lines 340-360):
```html
<a href="https://www.behance.net/YOUR_USERNAME" class="social-link" target="_blank">
    <img src="{{ url_for('static', filename='images/behance-icon.png') }}" alt="Behance">
</a>

<a href="https://www.instagram.com/YOUR_USERNAME" class="social-link" target="_blank">
    <img src="{{ url_for('static', filename='images/instagram-icon.png') }}" alt="Instagram">
</a>

<a href="https://www.linkedin.com/in/YOUR_USERNAME" class="social-link" target="_blank">
    <img src="{{ url_for('static', filename='images/linkedin-icon.png') }}" alt="LinkedIn">
</a>

<a href="https://medium.com/@YOUR_USERNAME" class="social-link" target="_blank">
    <img src="{{ url_for('static', filename='images/medium-icon.png') }}" alt="Medium">
</a>
```

## 🌐 API Endpoints

The Flask app provides JSON APIs for dynamic content:

- **GET** `/` - Main portfolio page
- **GET** `/api/projects` - All projects as JSON
- **GET** `/api/projects/<category>` - Projects filtered by category slug
  - Examples: `/api/projects/publication`, `/api/projects/branding`
  - Use `all` to get all projects: `/api/projects/all`
- **POST** `/api/contact` - Contact form submission
  - Body: `{"name": "", "email": "", "message": ""}`

## 📱 Responsive Breakpoints

- **Desktop**: 1025px and up (default)
- **Tablet**: 768px - 1024px
- **Mobile Landscape**: 481px - 767px  
- **Mobile Portrait**: 361px - 480px
- **Small Mobile**: 360px and below

Mobile-specific features:
- Reduced font sizes for better fit
- Single-column project grid
- Adjusted banner padding for text overflow prevention
- Touch-friendly tap-to-flip interactions

## 🎯 Key Interactions

### Flip Cards
- **Desktop**: Hover to flip stickers and logo
- **Mobile**: Tap/click to flip
- **Main Profile**: Always clickable, flips to show back side

### Hero Section
- **Stickers**: Fly in from center on page load (0.7s animation)
- **Profile Image**: Appears immediately when page loads
- **Logo Banner**: Flips to show tagline on hover/tap

### Menu & Navigation
- **Menu Button**: Top-left corner with star icon
- **Menu Items**: Smooth scroll to sections
- **Close**: Click outside or click another item

### Project Cards
- **Scroll Trigger**: GIF plays when card scrolled into view
- **Click**: Opens project detail modal with full gallery
- **Static Image**: Shows by default, GIF replaces on scroll

### Project Detail Modal
- **Navigation**: Previous/Next buttons to cycle through projects
- **Close**: X button or ESC key
- **Images**: Swipeable on mobile, scrollable on desktop

## 🛠 Development

### Project Structure

- **Backend**: Flask server (`app.py`) serves HTML template and JSON endpoints
- **Frontend**: Single-page experience with vanilla JavaScript
- **Styling**: CSS Grid and Flexbox for responsive layouts
- **Animations**: CSS keyframes + JavaScript event triggers

### Adding New Sections

1. Add HTML markup in `templates/index.html`
2. Add CSS styles in `static/css/style.css`
3. Add responsive styles at media breakpoints
4. Add JavaScript interactivity in `static/js/main.js` if needed
5. Update menu items to link to new sections

### Common Customizations

**Change animation timings** (style.css):
- Hero animation: Look for `@keyframes sticker*-fly-in`
- GIF scroll trigger: `js/main.js` - search for `IntersectionObserver`

**Adjust banner responsiveness**: 
- Check mobile media queries starting at line 1333

**Modify color scheme**:
- Edit CSS variables in `:root` selector (lines 10-16)

## � Dependencies

- Flask - Web framework
- Python 3.7+ - Runtime

Install with:
```bash
pip install -r requirements.txt
```

## 🚀 Deployment

### Local Testing
```bash
python app.py
# Visit: http://localhost:10000
```

### Production Deployment

The app supports environment variables:
- `PORT` - Server port (default: 10000)

Example deployment command:
```bash
PORT=8080 python app.py
```

### Deploy to Hosting Services
- **Heroku**: Add Procfile, push to Heroku
- **Vercel**: Not compatible (Node.js only)
- **Netlify**: Not compatible (static site only)  
- **PythonAnywhere**: Upload files, configure WSGI
- **AWS/GCP/Azure**: Deploy Flask app to compute service

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)
