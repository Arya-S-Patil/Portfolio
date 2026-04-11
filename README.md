# CLIMBING.IN Portfolio Website

A modern, interactive portfolio website with flipping stickers, animations, and responsive design.

## Features

- **Loading Screen**: Animated GIF on page load
- **Interactive Hero Section**: Flippable central image, 4 stickers, and logo banner
- **Projects Section**: Filterable project grid with scroll-triggered animations
- **About Section**: Personal bio with animated portrait GIF
- **Contact Section**: Email, phone, and social media links
- **Resume Modal**: In-page PDF viewer with download option
- **Project Detail Modal**: Full project galleries with navigation
- **Fully Responsive**: Mobile-first design with media queries

## Installation

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

## File Structure

```
Portfolio/
├── app.py                      # Flask application
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Main HTML template
├── static/
│   ├── css/
│   │   ├── style.css           # Main stylesheet
│   │   └── style.css.bak       # Backup stylesheet
│   ├── js/
│   │   └── main.js             # Front-end behavior and filtering
│   ├── images/                 # Hero and UI images
│   │   ├── profile.webp
│   │   ├── profile-back.webp
│   │   ├── sticker1.webp
│   │   ├── sticker1-back.webp
│   │   ├── sticker2.webp
│   │   ├── sticker2-back.webp
│   │   ├── sticker3.webp
│   │   ├── sticker3-back.webp
│   │   ├── sticker4.webp
│   │   ├── sticker4-back.webp
│   │   ├── portrait.gif
│   │   ├── portrait.webp
│   │   ├── behance-icon.webp
│   │   ├── instagram-icon.webp
│   │   ├── linkedin-icon.webp
│   │   ├── medium-icon.webp
│   │   ├── Back.webp
│   │   ├── Cross.webp
│   │   ├── next.webp
│   │   └── previous.webp
│   └── assets/
│       ├── loading.gif         # Loading animation
│       ├── loading2.gif        # Alternate loading animation
│       ├── resume.pdf          # Resume PDF used by modal
│       ├── projects/           # Project GIFs and preview assets
│       ├── Artist way zine/    # Publication project assets
│       ├── Beakvox branding project/  # Branding project assets
│       ├── ather/              # Ather x Route Zero project assets
│       ├── pub1/               # Publication project images
│       └── 30 days of design/  # Challenge project assets
```

## Customization Guide

### 1. Replace Demo Images

Replace the actual files used by the current repo:

#### Hero Section Images
- `static/images/profile.webp` - main profile image
- `static/images/profile-back.webp` - alternate profile image
- `static/images/sticker1.webp` to `static/images/sticker4.webp` - sticker fronts
- `static/images/sticker1-back.webp` to `static/images/sticker4-back.webp` - sticker backs
- `static/images/portrait.gif` - animated portrait

#### Social Icons
- `static/images/behance-icon.webp`
- `static/images/instagram-icon.webp`
- `static/images/linkedin-icon.webp`
- `static/images/medium-icon.webp`

#### Loading and Resume
- `static/assets/loading.gif`
- `static/assets/loading2.gif`
- `static/assets/resume.pdf`

#### Project Asset Folders
- `static/assets/Artist way zine/`
- `static/assets/Beakvox branding project/`
- `static/assets/ather/`
- `static/assets/pub1/`
- `static/assets/30 days of design/`
- `static/assets/projects/`

### 2. Update Page Content

#### HTML Content
Update `templates/index.html` for the displayed text, project labels, contact info, and resume modal content.

- Hero section content
- About section text and biography
- Contact email and phone links
- Resume download button and modal

#### Project Data
The project listings are defined in `app.py` inside the `PROJECTS` array.

Each project object includes:
- `id` - unique project identifier
- `title` - project title
- `category` - display category name
- `category_slug` - filter slug used by the UI
- `image` - initial thumbnail image URL
- `gif` - project GIF filename in `static/assets/projects/`
- `description` - project description
- `images` - list of asset paths used by the project detail modal

#### Categories
The available categories in `app.py` are:
- `all`
- `publication`
- `branding`
- `route`
- `design`

Make sure each `project['category_slug']` matches one of these slugs.

### 3. Installation and Local Run

Install dependencies and start the Flask app:

```bash
pip install -r requirements.txt
python app.py
```

Then open:

```
http://localhost:10000
```

The app listens on port `10000` by default.

### 4. Notes on Current Repo Content

- The repo uses `.webp` image assets in `static/images/`.
- `static/assets/resume.pdf` is the resume file used by the resume modal.
- Project GIFs are stored in `static/assets/projects/`.
- `requirements.txt` currently includes `Flask==3.0.0` and `gunicorn`.

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
