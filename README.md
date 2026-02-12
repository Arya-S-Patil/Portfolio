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
http://localhost:5000
```

## 📁 File Structure

```
climbing-portfolio/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css          # All styles
│   ├── js/
│   │   └── main.js            # All JavaScript
│   ├── images/
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
│   │   ├── logo-back.png      # Logo banner back
│   │   ├── illustration.png   # About section illustration
│   │   ├── portrait.gif       # Animated portrait
│   │   ├── behance-icon.png   # Social icon
│   │   ├── instagram-icon.png # Social icon
│   │   ├── linkedin-icon.png  # Social icon
│   │   └── medium-icon.png    # Social icon
│   └── assets/
│       ├── loading.gif        # Loading screen animation
│       ├── decorative.gif     # Projects section decoration
│       ├── resume.pdf         # Your resume PDF
│       └── projects/          # Project-specific GIFs
│           ├── project-pub-1.gif
│           ├── project-pub-2.gif
│           ├── project-brand-1.gif
│           ├── project-brand-2.gif
│           ├── project-photo-1.gif
│           ├── project-route-1.gif
│           ├── project-design-1.gif
│           └── project-blogs-1.gif
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
- `static/assets/decorative.gif` - Projects section decoration

#### Social Icons
- Replace all `*-icon.png` files with actual social media icons (80x80px)

#### Resume
- `static/assets/resume.pdf` - **REPLACE WITH YOUR ACTUAL RESUME**

### 2. Update Content

#### Personal Information (templates/index.html)

**About Section** (around line 240):
```html
<p class="about-intro">
    Morning! I'm <strong>YOUR NAME</strong>, an aspiring...
    <!-- Update with your bio -->
</p>
```

**Poem** (lines 250-268):
```html
<blockquote>
    <!-- Replace with your own poem or remove this section -->
</blockquote>
```

**Contact Info** (lines 320-330):
```html
<a href="mailto:YOUR_EMAIL@gmail.com">YOUR_EMAIL@gmail.com</a>
<a href="tel:+91YOUR_PHONE">+91 YOUR_PHONE</a>
```

#### Projects (app.py)

Edit the `PROJECTS` array (lines 7-115):
```python
PROJECTS = [
    {
        'id': 'your-project-id',
        'title': 'Your Project Title',
        'category': 'Your Category',
        'category_slug': 'category-slug',
        'image': 'https://your-image-url.com/image.jpg',  # Static thumbnail
        'gif': 'your-project.gif',  # Animated GIF (plays on scroll)
        'description': 'Your project description',
        'images': [
            'https://image1.jpg',
            'https://image2.jpg',
        ]
    },
    # Add more projects...
]
```

**Important**: Each project needs:
1. A static `image` (thumbnail shown initially)
2. A `gif` filename (plays when scrolled into view)
3. The GIF file should be placed in `static/assets/projects/`

#### Categories

Edit `CATEGORIES` array in app.py (lines 117-125):
```python
CATEGORIES = [
    {'name': 'All', 'slug': 'all'},
    {'name': 'Your Category 1', 'slug': 'category1'},
    # Add your categories...
]
```

### 3. Customize Colors

Edit CSS variables in `static/css/style.css` (lines 7-14):
```css
:root {
    --neon-green: #B8FF3C;    /* Primary accent color */
    --dark-bg: #1a1a1a;       /* Medium dark background */
    --darker-bg: #0f0f0f;     /* Darkest background */
    --cream: #F5F0E8;         /* Text color */
    --pink: #D64C7F;          /* Secondary accent */
    --pink-light: #E57FA0;    /* Light pink variant */
}
```

### 4. Fonts

Current fonts (from Google Fonts):
- **Rubik Vinyl** - Section titles and banners
- **Work Sans** - Body text

To change fonts, update the Google Fonts link in `templates/index.html` (line 11) and the CSS font-family declarations.

### 5. Social Media Links

Update social media URLs in `templates/index.html` (lines 335-355):
```html
<a href="https://behance.net/YOUR_USERNAME" class="social-link" target="_blank">
<a href="https://instagram.com/YOUR_USERNAME" class="social-link" target="_blank">
<a href="https://linkedin.com/in/YOUR_USERNAME" class="social-link" target="_blank">
<a href="https://medium.com/@YOUR_USERNAME" class="social-link" target="_blank">
```

## 📱 Responsive Breakpoints

- **Desktop**: Default styles
- **Tablet**: max-width: 1024px
- **Mobile Landscape**: max-width: 768px
- **Mobile Portrait**: max-width: 480px
- **Small Mobile**: max-width: 360px

## 🎯 Key Interactions

### Flip Cards
- **Desktop**: Hover to flip
- **Mobile**: Tap to flip
- **All**: Click to toggle flip state

### Menu
- Click menu button to open/close
- Click menu items to scroll to sections
- Click outside to close

### Project Filters
- Click category to filter projects
- "All" shows all projects
- Smooth animations on filter change

### Modals
- **Resume**: Click "View Resume" button
- **Project Detail**: Click any project card
- **Close**: Click X button or press ESC

## 🛠 Development

### Adding New Sections

1. Add HTML in `templates/index.html`
2. Add styles in `static/css/style.css`
3. Add JavaScript if needed in `static/js/main.js`
4. Update menu items

### Testing Responsive Design

```bash
# Use browser DevTools
# Chrome: F12 → Toggle Device Toolbar (Ctrl+Shift+M)
# Test all breakpoints: 360px, 480px, 768px, 1024px, 1440px
```

## 📄 License

This is a custom portfolio template. Feel free to use and modify for your personal portfolio.

## 🤝 Support

For issues or questions, update the content and images as needed. All demo assets are placeholders and should be replaced with your actual content.

---

**Remember**: This template uses demo images and content. Replace everything with your actual portfolio content before deploying!
