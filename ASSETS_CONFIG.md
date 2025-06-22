# 🔧 GitHub Profile Assets & Configuration

## 📁 Asset Files

### Custom CSS untuk GitHub Profile
Meskipun GitHub README tidak mendukung CSS eksternal, berikut adalah styling yang bisa diconvert ke HTML inline:

#### Color Palette
```css
:root {
  --primary-color: #F75C7E;
  --secondary-color: #4ECDC4;
  --accent-color: #45B7D1;
  --dark-bg: #0D1117;
  --light-text: #FFFFFF;
  --gray-text: #8B949E;
}
```

#### Button Styles (untuk HTML badges)
```html
<a href="https://linkedin.com/in/fajrunnadhif">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin" alt="LinkedIn" style="border-radius: 8px; transition: transform 0.3s ease;" />
</a>
```

## 🎨 Custom Banner Images

### Canva Templates
Ukuran yang disarankan untuk banner GitHub:
- **Width:** 1200px
- **Height:** 300-400px
- **Format:** PNG dengan background transparan

### Banner Ideas
1. **Professional Banner**
   - Logo Aneramedia + Nama
   - Tagline: "Backend Developer | Laravel Expert"
   - Minimalist design dengan tech icons

2. **Animated Banner**
   - Typing effect dengan tech stack
   - Gradient background
   - Subtle animations

3. **Code Banner**
   - Background dengan code snippet
   - Terminal-style design
   - Syntax highlighting

## 🔗 URL Shorteners & Tracking

### Bit.ly Links untuk Analytics
Buat short links untuk tracking clicks:
```
Portfolio: bit.ly/fajrun-portfolio
LinkedIn: bit.ly/fajrun-linkedin  
Email: bit.ly/fajrun-contact
Website: bit.ly/aneramedia-web
```

### UTM Parameters untuk Google Analytics
```
https://aneramedia.com?utm_source=github&utm_medium=profile&utm_campaign=readme
```

## 📊 GitHub Stats Configuration

### Custom Themes
```yaml
# Light Theme
theme: default
title_color: 2f80ed
icon_color: 2f80ed
text_color: 333
bg_color: ffffff

# Dark Theme  
theme: dark
title_color: ff6b6b
icon_color: ff6b6b
text_color: ffffff
bg_color: 0d1117

# Custom Brand Theme
title_color: F75C7E
icon_color: 4ECDC4
text_color: ffffff
bg_color: 1a1a1a
```

### Advanced Stats Options
```
# Most Used Languages
?username=fajrunnadhif
&layout=compact
&langs_count=8
&hide=html,css
&theme=radical
&custom_title=Tech Stack

# GitHub Stats
?username=fajrunnadhif
&show_icons=true
&include_all_commits=true
&count_private=true
&theme=radical
&hide_rank=false
&show_owner=true

# Streak Stats
?user=fajrunnadhif
&theme=radical
&hide_border=true
&stroke=0000
&background=0D1117
&ring=F75C7E
&fire=F75C7E
&currStreakLabel=F75C7E
```

## 🛠️ Workflow Configurations

### Auto-update README
```yaml
name: Update README

on:
  schedule:
    - cron: '0 0 * * *' # Daily at midnight
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Update README
        uses: jamesgeorge007/github-activity-readme@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Profile Views Counter
```yaml
name: Profile Views

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  views:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Generate profile views
        uses: komarev/ghpvc@v1
        with:
          username: fajrunnadhif
          color: brightgreen
```

## 📱 Social Media Integration

### LinkedIn Post Templates
Untuk sharing GitHub profile di LinkedIn:

```
🚀 Excited to share my updated GitHub profile! 

As a Backend Developer specializing in Laravel, I've been working on some amazing projects including:
• Survey Management Systems
• CBT Applications  
• Company Profile Websites

Check out my latest work and let's connect if you're interested in Laravel development or need IT consulting services.

#Laravel #PHP #BackendDevelopment #WebDevelopment #GitHub #Aneramedia

https://github.com/fajrunnadhif
```

### Twitter Bio
```
🚀 Backend Developer | Laravel Expert
🏢 Founder @Aneramedia  
💼 5+ years building web apps
🌐 Helping businesses grow digitally
📧 fajrun@aneramedia.com
```

## 🎯 SEO Optimization

### Meta Tags untuk Website
```html
<meta name="description" content="Fajrun Nadhif - Backend Developer and Laravel Expert. Founder of Aneramedia, specializing in web development and IT consulting services.">
<meta name="keywords" content="Laravel Developer, PHP Developer, Backend Developer, Aneramedia, Web Development, IT Consulting">
<meta property="og:title" content="Fajrun Nadhif - Backend Developer | Laravel Expert">
<meta property="og:description" content="5+ years experience in Laravel development. Building scalable web applications and providing IT consulting services.">
<meta property="og:image" content="https://github.com/fajrunnadhif/fajrunnadhif/raw/main/banner.png">
```

### Structured Data
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Fajrun Nadhif",
  "jobTitle": "Backend Developer",
  "worksFor": {
    "@type": "Organization",
    "name": "Aneramedia"
  },
  "url": "https://github.com/fajrunnadhif",
  "sameAs": [
    "https://linkedin.com/in/fajrunnadhif",
    "https://aneramedia.com"
  ],
  "knowsAbout": ["Laravel", "PHP", "MySQL", "Web Development", "API Development"]
}
```

## 🔒 Security & Privacy

### Environment Variables
```bash
# .env untuk development
GITHUB_USERNAME=fajrunnadhif
LINKEDIN_URL=https://linkedin.com/in/fajrunnadhif
EMAIL=fajrun@aneramedia.com
WEBSITE_URL=https://aneramedia.com
```

### Token Management
- Buat Personal Access Token dengan scope minimal
- Gunakan GitHub Secrets untuk workflow
- Rotate token secara berkala (3-6 bulan)

### Privacy Settings
- Set email sebagai private di GitHub
- Use noreply email untuk commits
- Review permission untuk third-party apps

## 📈 Analytics & Monitoring

### Google Analytics untuk Website
```javascript
// Track GitHub profile clicks
gtag('event', 'click', {
  'event_category': 'External Link',
  'event_label': 'GitHub Profile',
  'value': 1
});
```

### GitHub Insights
Monitor:
- Profile views dari komarev counter
- Repository stars dan forks
- Follower growth
- Contribution activity

### Performance Monitoring
- Test loading speed dengan Lighthouse
- Monitor external service uptime
- Check badge availability
- Validate all links monthly

---

**💡 Pro Tip:** Simpan semua asset dalam folder terpisah dan gunakan version control untuk tracking perubahan pada profile README Anda.
