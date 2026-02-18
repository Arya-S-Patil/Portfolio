// ===================================
// CLIMBING.IN Portfolio JavaScript
// ===================================

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {

    // ===================================
    // LOADING SCREEN
    // ===================================
    const loadingScreen = document.getElementById('loading-screen');
    
    console.log('Loading screen initialized');
    
    // Hide loading screen after 5 seconds to let GIF play
    setTimeout(() => {
        console.log('Hiding loading screen');
        if (loadingScreen) {
            loadingScreen.classList.add('hidden');
            loadingScreen.style.display = 'none';
            document.body.style.overflow = '';
        }
        
        // Trigger sticker fly-in animation
        const profileWrapper = document.querySelector('.profile-stickers-wrapper');
        if (profileWrapper) {
            profileWrapper.classList.add('hero-animate');
        }
        
        // Add "landed" class to stickers after animation completes (0.7s)
        setTimeout(() => {
            const stickers = document.querySelectorAll('.sticker');
            stickers.forEach(sticker => {
                sticker.classList.add('landed');
            });
        }, 700);
        
        // Show profile image immediately
        const profileImage = document.querySelector('.image-flip');
        if (profileImage) {
            profileImage.classList.add('profile-visible');
        }
        
    }, 5000); // Show loading GIF for 5 seconds

    // ===================================
    // MENU TOGGLE
    // ===================================
    const menuButton = document.getElementById('menu-button');
    const menuDropdown = document.getElementById('menu-dropdown');
    
    menuButton.addEventListener('click', function(e) {
        e.stopPropagation();
        menuDropdown.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!menuDropdown.contains(e.target) && e.target !== menuButton) {
            menuDropdown.classList.remove('active');
        }
    });

    // Smooth scroll for menu items
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
                menuDropdown.classList.remove('active');
            }
        });
    });

    // ===================================
    // FLIP CARDS - SIMPLE HOVER ONLY
    // ===================================
    
    // Get all stickers
    const stickers = document.querySelectorAll('.sticker');
    
    // Detect if device is touch-enabled
    const isTouchDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
    
    // Track flip timeouts for each element
    const flipTimeouts = new WeakMap();
    
    // Stickers: Simple hover flip or tap for mobile
    stickers.forEach(sticker => {
        if (isTouchDevice) {
            // On touch devices, toggle on tap and auto-flip back after 3 seconds
            sticker.addEventListener('click', function(e) {
                e.preventDefault();
                this.classList.add('flipped');
                
                // Clear any existing timeout
                if (flipTimeouts.has(this)) {
                    clearTimeout(flipTimeouts.get(this));
                }
                
                // Set new timeout to flip back
                const timeout = setTimeout(() => {
                    this.classList.remove('flipped');
                }, 3000);
                
                flipTimeouts.set(this, timeout);
            });
        } else {
            // On desktop, hover behavior
            sticker.addEventListener('mouseenter', function() {
                this.classList.add('flipped');
            });
            
            sticker.addEventListener('mouseleave', function() {
                this.classList.remove('flipped');
            });
        }
    });
    
    // Profile image: hover flip or tap
    const profileImage = document.querySelector('.image-flip');
    if (profileImage) {
        if (isTouchDevice) {
            profileImage.addEventListener('click', function(e) {
                e.preventDefault();
                this.classList.add('flipped');
                
                // Clear any existing timeout
                if (flipTimeouts.has(this)) {
                    clearTimeout(flipTimeouts.get(this));
                }
                
                // Set new timeout to flip back
                const timeout = setTimeout(() => {
                    this.classList.remove('flipped');
                }, 3000);
                
                flipTimeouts.set(this, timeout);
            });
        } else {
            profileImage.addEventListener('mouseenter', function() {
                this.classList.add('flipped');
            });
            
            profileImage.addEventListener('mouseleave', function() {
                this.classList.remove('flipped');
            });
        }
    }
    
    // Logo: hover flip or tap
    const logoFlip = document.getElementById('logo-flip');
    if (logoFlip) {
        if (isTouchDevice) {
            // On touch devices, toggle on tap and auto-flip back after 3 seconds
            logoFlip.addEventListener('click', function(e) {
                e.preventDefault();
                this.classList.add('flipped');
                if (flipTimeouts.has(this)) clearTimeout(flipTimeouts.get(this));
                const timeout = setTimeout(() => {
                    this.classList.remove('flipped');
                }, 3000);
                flipTimeouts.set(this, timeout);
            });
        } else {
            // On desktop, hover behavior
            logoFlip.addEventListener('mouseenter', function() {
                this.classList.add('flipped');
            });
            
            logoFlip.addEventListener('mouseleave', function() {
                this.classList.remove('flipped');
            });
        }
    }
    
    // Section headers and other flip cards: hover flip or tap
    const otherFlipCards = document.querySelectorAll('.flip-card:not(.sticker):not(.image-flip):not(.logo-flip)');
    otherFlipCards.forEach(card => {
        if (isTouchDevice) {
            card.addEventListener('click', function(e) {
                // Don't toggle if clicking on a button or link inside
                if (e.target.tagName !== 'BUTTON' && e.target.tagName !== 'A') {
                    this.classList.add('flipped');
                    
                    // Clear any existing timeout
                    if (flipTimeouts.has(this)) {
                        clearTimeout(flipTimeouts.get(this));
                    }
                    
                    // Set new timeout to flip back
                    const timeout = setTimeout(() => {
                        this.classList.remove('flipped');
                    }, 3000);
                    
                    flipTimeouts.set(this, timeout);
                }
            });
        } else {
            card.addEventListener('mouseenter', function() {
                this.classList.add('flipped');
            });
            
            card.addEventListener('mouseleave', function() {
                this.classList.remove('flipped');
            });
        }
    });

    // ===================================
    // SCROLL ANIMATIONS
    // ===================================
    
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.3,  // Trigger when 30% of element is visible
        rootMargin: '0px 0px -50px 0px'
    };

    const scrollObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Special handling for project cards - play GIF
                if (entry.target.classList.contains('project-card')) {
                    entry.target.classList.add('in-view');
                }
            }
        });
    }, observerOptions);

    // Observe project cards
    const projectCards = document.querySelectorAll('[data-scroll-animate]');
    projectCards.forEach(card => {
        scrollObserver.observe(card);
    });

    // ===================================
    // CATEGORY FILTERS
    // ===================================
    const filterButtons = document.querySelectorAll('.filter-btn');
    const allProjectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const category = this.getAttribute('data-category');
            
            // Update active state
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Filter projects immediately without delay
            allProjectCards.forEach(card => {
                const cardCategory = card.getAttribute('data-category');
                
                if (category === 'all' || cardCategory === category) {
                    card.classList.remove('hidden');
                    card.classList.add('visible');
                } else {
                    card.classList.add('hidden');
                    card.classList.remove('visible');
                }
            });
        });
    });

    // Helper function to check if element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // ===================================
    // PROJECT DETAIL MODAL
    // ===================================
    const projectDetail = document.getElementById('project-detail');
    const closeProjectBtn = document.getElementById('close-project');
    const detailCategory = document.getElementById('detail-category');
    const detailTitle = document.getElementById('detail-title');
    const detailDescription = document.getElementById('detail-description');
    const detailImages = document.getElementById('detail-images');
    const prevProjectBtn = document.getElementById('prev-project');
    const nextProjectBtn = document.getElementById('next-project');
    const prevProjectBtnMobile = document.getElementById('prev-project-mobile');
    const nextProjectBtnMobile = document.getElementById('next-project-mobile');

    let currentProjectIndex = 0;
    let projects = [];

    // Fetch projects data
    fetch('/api/projects')
        .then(response => response.json())
        .then(data => {
            projects = data;
        });

    // Open project detail
    allProjectCards.forEach(card => {
        card.addEventListener('click', function() {
            const projectId = this.getAttribute('data-project-id');
            openProjectDetail(projectId);
        });
    });

    function openProjectDetail(projectId) {
        const project = projects.find(p => p.id === projectId);
        if (!project) return;

        currentProjectIndex = projects.indexOf(project);

        // Populate project details
        detailCategory.textContent = project.category;
        detailTitle.textContent = project.title;
        detailDescription.textContent = project.description;

        // Clear and populate images
        detailImages.innerHTML = '';
        project.images.forEach(imageUrl => {
            const img = document.createElement('img');
            img.src = imageUrl;
            img.alt = project.title;
            detailImages.appendChild(img);
        });

        // Show modal
        projectDetail.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    // Close project detail
    closeProjectBtn.addEventListener('click', closeProjectDetail);

    function closeProjectDetail() {
        projectDetail.classList.remove('active');
        document.body.style.overflow = '';
    }

    // Previous project
    prevProjectBtn.addEventListener('click', function() {
        currentProjectIndex = currentProjectIndex > 0 ? currentProjectIndex - 1 : projects.length - 1;
        const project = projects[currentProjectIndex];
        openProjectDetail(project.id);
    });

    // Next project
    nextProjectBtn.addEventListener('click', function() {
        currentProjectIndex = currentProjectIndex < projects.length - 1 ? currentProjectIndex + 1 : 0;
        const project = projects[currentProjectIndex];
        openProjectDetail(project.id);
    });

    // Mobile Previous project
    if (prevProjectBtnMobile) {
        prevProjectBtnMobile.addEventListener('click', function() {
            currentProjectIndex = currentProjectIndex > 0 ? currentProjectIndex - 1 : projects.length - 1;
            const project = projects[currentProjectIndex];
            openProjectDetail(project.id);
        });
    }

    // Mobile Next project
    if (nextProjectBtnMobile) {
        nextProjectBtnMobile.addEventListener('click', function() {
            currentProjectIndex = currentProjectIndex < projects.length - 1 ? currentProjectIndex + 1 : 0;
            const project = projects[currentProjectIndex];
            openProjectDetail(project.id);
        });
    }

    // Close on ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && projectDetail.classList.contains('active')) {
            closeProjectDetail();
        }
    });

    // ===================================
    // RESUME MODAL
    // ===================================
    const resumeModal = document.getElementById('resume-modal');
    const viewResumeBtn = document.getElementById('view-resume-btn');
    const closeResumeBtn = document.getElementById('close-resume');

    if (viewResumeBtn) {
        viewResumeBtn.addEventListener('click', function() {
            resumeModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    }

    if (closeResumeBtn) {
        closeResumeBtn.addEventListener('click', function() {
            resumeModal.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    // Close resume modal on ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && resumeModal.classList.contains('active')) {
            resumeModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // Close resume modal on background click
    resumeModal.addEventListener('click', function(e) {
        if (e.target === resumeModal) {
            resumeModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // ===================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ===================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // ===================================
    // INITIALIZE ANIMATIONS
    // ===================================
    
    // Initial check for elements already in viewport
    setTimeout(() => {
        projectCards.forEach(card => {
            if (isInViewport(card)) {
                card.classList.add('visible');
            }
        });
    }, 100);

    // ===================================
    // UTILITY FUNCTIONS
    // ===================================
    
    console.log('CLIMBING.IN Portfolio loaded successfully!');
});