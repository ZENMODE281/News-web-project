# News Discussion Platform - Design System & Style Guide

## 🎨 **Brand Identity**

### **Color Palette**
```css
/* Primary Colors */
--primary-blue: #343a37;      /* Brand blue - main CTAs */
--primary-dark: #1E40AF;      /* Dark blue - hover states */
--primary-light: #60A5FA;     /* Light blue - highlights */

/* Neutral Colors */
--gray-900: #dae0ef;          /* Headlines, main text */
--gray-700: #374151;          /* Body text */
--gray-500: #6B7280;          /* Secondary text */
--gray-300: #D1D5DB;          /* Borders, dividers */
--gray-100: #F3F4F6;          /* Backgrounds */
--gray-50: #F9FAFB;           /* Card backgrounds */

/* Semantic Colors */
--success: #10B981;           /* Success messages */
--warning: #F59E0B;           /* Warnings */
--error: #EF4444;             /* Errors, destructive actions */
--info: #3B82F6;              /* Information */

/* Status Colors */
--upvote: #FF4500;            /* Reddit-like upvote */
--downvote: #7193FF;          /* Downvote blue */
--trending: #8B5CF6;          /* Trending purple */
--new: #06D6A0;               /* New content green */
```

### **Typography**
```css
/* Font Family */
--font-family: 'Inter', sans-serif;

/* Headlines can optionally use: 'Playfair Display' or 'Merriweather' */

/* Scale (using modular scale 1.25) */
--text-xs: 0.75rem;    /* 12px - labels, tags */
--text-sm: 0.875rem;   /* 14px - small text */
--text-base: 1rem;     /* 16px - body text */
--text-lg: 1.125rem;   /* 18px - lead text */
--text-xl: 1.25rem;    /* 20px - subheadings */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px - main headings */
--text-5xl: 3rem;      /* 48px - hero text */

/* Weights */
--font-light: 300;
--font-regular: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

/* Line Heights */
--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.75;
```

## 📐 **Layout & Spacing**

### **Grid System**
```css
/* Container widths */
--container-sm: 640px;
--container-md: 768px;
--container-lg: 1024px;
--container-xl: 1280px;
--container-2xl: 1536px;

/* Spacing Scale (8px base) */
--space-1: 0.25rem;    /* 4px */
--space-2: 0.5rem;     /* 8px */
--space-3: 0.75rem;    /* 12px */
--space-4: 1rem;       /* 16px */
--space-6: 1.5rem;     /* 24px */
--space-8: 2rem;       /* 32px */
--space-12: 3rem;      /* 48px */
--space-16: 4rem;      /* 64px */
```

### **Breakpoints**
```css
/* Mobile-first approach */
--sm: 640px;
--md: 768px;
--lg: 1024px;
--xl: 1280px;
--2xl: 1536px;
```

## 🧩 **Component Library**

### **Buttons**
```css
/* Primary Button */
.btn-primary {
  background: var(--primary-blue);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 600;
  font-size: var(--text-sm);
  border: none;
  transition: all 0.2s;
}
.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
}

/* Secondary Button */
.btn-secondary {
  background: white;
  color: var(--gray-700);
  border: 1px solid var(--gray-300);
  /* rest same as primary */
}

/* Text Button */
.btn-text {
  background: transparent;
  color: var(--primary-blue);
  /* rest same */
}

/* Icon Button */
.btn-icon {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### **Cards**
```css
.article-card {
  background: white;
  border-radius: 0.75rem;
  border: 1px solid var(--gray-200);
  padding: var(--space-6);
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  transition: box-shadow 0.2s;
}
.article-card:hover {
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
}

.discussion-card {
  /* Similar but with different padding */
}
```

### **Forms**
```css
.input-field {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--gray-300);
  border-radius: 0.5rem;
  font-size: var(--text-base);
  transition: border-color 0.2s;
}
.input-field:focus {
  outline: none;
  border-color: var(--primary-blue);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Labels */
.form-label {
  display: block;
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--gray-700);
  margin-bottom: var(--space-2);
}

/* Error States */
.input-error {
  border-color: var(--error);
}
.error-message {
  color: var(--error);
  font-size: var(--text-sm);
  margin-top: var(--space-2);
}
```

### **Navigation**
```css
/* Top Navigation */
.navbar {
  height: 4rem;
  border-bottom: 1px solid var(--gray-200);
  background: white;
}

/* Sidebar (if applicable) */
.sidebar {
  width: 16rem;
  background: var(--gray-50);
  border-right: 1px solid var(--gray-200);
}
```

### **Vote/Reaction System**
```css
.vote-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem;
  background: transparent;
  border: none;
  color: var(--gray-500);
  border-radius: 0.25rem;
}
.vote-button.upvoted {
  color: var(--upvote);
}
.vote-button.downvoted {
  color: var(--downvote);
}
.vote-count {
  font-weight: 600;
  font-size: var(--text-sm);
}
```

## 🎭 **Interaction & Animation**

### **Transitions**
```css
/* Standard transitions */
--transition-fast: 150ms ease;
--transition-normal: 250ms ease;
--transition-slow: 350ms ease;

/* Hover effects */
.hover-lift:hover {
  transform: translateY(-2px);
  transition: transform var(--transition-normal);
}

/* Fade in */
.fade-in {
  animation: fadeIn 0.3s ease;
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

### **Loading States**
```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--gray-100) 25%,
    var(--gray-200) 50%,
    var(--gray-100) 75%
  );
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}
@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

## 📱 **Mobile-Specific Styles**

### **Touch Targets**
```css
/* Minimum touch target size */
.min-touch-target {
  min-width: 44px;
  min-height: 44px;
}
```

### **Mobile Navigation**
```css
@media (max-width: 768px) {
  .mobile-hidden {
    display: none;
  }
  .mobile-menu {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    /* ... */
  }
}
```

## 🏷️ **Content Specific Styling**

### **Article Headlines**
```css
.headline-primary {
  font-size: var(--text-2xl);
  font-weight: 700;
  line-height: 1.3;
  color: var(--gray-900);
  margin-bottom: var(--space-4);
}

.headline-secondary {
  font-size: var(--text-xl);
  font-weight: 600;
  /* ... */
}
```

### **Discussion Threads**
```css
.comment-level-1 { margin-left: 0; }
.comment-level-2 { margin-left: 2rem; }
.comment-level-3 { margin-left: 4rem; }
.comment-level-4 { margin-left: 6rem; }

.thread-line {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--gray-200);
}
```

### **Tags & Categories**
```css
.category-tag {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: var(--text-xs);
  font-weight: 500;
}

.tag-politics { background: #FEE2E2; color: #991B1B; }
.tag-tech { background: #DBEAFE; color: #1E40AF; }
.tag-sports { background: #DCFCE7; color: #166534; }
/* etc */
```

## 🎯 **Utility Classes**

```css
/* Display */
.hidden { display: none; }
.block { display: block; }
.flex { display: flex; }
.grid { display: grid; }

/* Spacing Utilities */
.mt-2 { margin-top: var(--space-2); }
.p-4 { padding: var(--space-4); }

/* Text Utilities */
.text-center { text-align: center; }
.font-bold { font-weight: 700; }
.text-gray-500 { color: var(--gray-500); }

/* Responsive Utilities */
.desktop-only { display: none; }
@media (min-width: 768px) {
  .desktop-only { display: block; }
  .mobile-only { display: none; }
}
```

## 📝 **Accessibility Guidelines**

1. **Color Contrast:** Minimum 4.5:1 for normal text
2. **Focus States:** Always visible focus indicators
3. **ARIA Labels:** Use appropriate ARIA attributes
4. **Keyboard Navigation:** Full keyboard support
5. **Alt Text:** All images must have descriptive alt text

## 🚀 **Implementation Notes**

1. **CSS Variables:** Store all design tokens as CSS variables
2. **Component First:** Build reusable components before pages
3. **Mobile First:** Design for mobile, enhance for desktop
4. **Performance:** Lazy load images and comments
5. **Dark Mode:** Consider adding dark mode support

---

**Next Steps:**
1. Create a Figma/Sketch file with these tokens
2. Set up your CSS/SCSS with these variables
3. Build a component library starting with Button and Card
4. Test color contrast ratios
5. Create responsive layout grids

