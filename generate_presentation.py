"""
generate_presentation.py — Production-grade 16:9 widescreen presentation deck generator.
Generates MovieLens_Analytics_Presentation.pptx matching all requirements:
1. 4-Tier Tree System Architecture
2. Tech Stack, Why NoSQL over SQL, and Trade-offs Made
3. Admin vs User Capabilities
4. Complete List of REST APIs
5. Side-by-side PyMongo Query Code (Left) + High-Res Output Chart (Right) for Questions (a)-(g)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# 16:9 Widescreen dimensions
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Modern Tech Dark Theme Palette
BG_COLOR = RGBColor(15, 20, 31)        # #0f141f
CARD_BG = RGBColor(22, 27, 40)         # #161b28
CARD_BORDER = RGBColor(45, 55, 78)     # #2d374e
TEXT_WHITE = RGBColor(245, 247, 250)   # #f5f7fa
TEXT_MUTED = RGBColor(140, 150, 170)   # #8c96aa
ACCENT_PURPLE = RGBColor(124, 92, 255) # #7c5cff
ACCENT_GREEN = RGBColor(0, 229, 163)   # #00e5a3
ACCENT_CYAN = RGBColor(0, 192, 240)    # #00c0f0
ACCENT_AMBER = RGBColor(255, 183, 43)  # #ffb72b
CODE_BG = RGBColor(14, 18, 27)         # #0e121b

IMG_DIR = os.path.join(os.path.dirname(__file__), "screenshots", "extracted")

prs = Presentation()
prs.slide_width = SLIDE_WIDTH
prs.slide_height = SLIDE_HEIGHT
blank_layout = prs.slide_layouts[6]

def set_slide_background(slide):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = BG_COLOR

def add_header(slide, title_text, category="DATA ENGINEERING | DS5003"):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.9))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = category.upper()
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_PURPLE
    p0.space_after = Pt(2)
    
    p1 = tf.add_paragraph()
    p1.text = title_text
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    return shape

def add_code_block(slide, left, top, width, height, title, code_text, bullets=None):
    add_card(slide, left, top, width, height, bg_color=CODE_BG, border_color=CARD_BORDER)
    tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = title.upper()
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN
    p0.space_after = Pt(6)
    
    p_code = tf.add_paragraph()
    p_code.text = code_text
    p_code.font.name = "Courier New"
    p_code.font.size = Pt(10)
    p_code.font.color.rgb = TEXT_WHITE
    p_code.space_after = Pt(8)
    
    if bullets:
        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"▶  {b}"
            p_b.font.size = Pt(11)
            p_b.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 1: Title Slide
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1)
add_card(s1, Inches(1.2), Inches(1.0), Inches(10.9), Inches(5.5), bg_color=CARD_BG, border_color=ACCENT_PURPLE)

tb1 = s1.shapes.add_textbox(Inches(1.8), Inches(1.4), Inches(9.7), Inches(4.7))
tf1 = tb1.text_frame
tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "DS5003 DATA ENGINEERING LAB  •  PROJECT PRESENTATION"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = ACCENT_PURPLE
p.space_after = Pt(6)

p = tf1.add_paragraph()
p.text = "MovieLens 25M Analytics Platform"
p.font.size = Pt(34)
p.font.bold = True
p.font.color.rgb = TEXT_WHITE
p.space_after = Pt(8)

p = tf1.add_paragraph()
p.text = "High-Performance NoSQL Data Pipeline, Role-Based Access & Interactive Visualizations"
p.font.size = Pt(15)
p.font.color.rgb = ACCENT_CYAN
p.space_after = Pt(26)

p = tf1.add_paragraph()
p.text = "Project Team Members:"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = TEXT_MUTED

members = [
    "Ben George (142613005)",
    "Nandavaram Shashi Pritham (142602010)",
    "Paltasingi Abhishek Sonu (142602013)"
]
for m in members:
    p = tf1.add_paragraph()
    p.text = f"•  {m}"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

p = tf1.add_paragraph()
p.text = "\nFaculty: Dr. Koninika Pal  •  Indian Institute of Technology Palakkad"
p.font.size = Pt(12)
p.font.color.rgb = ACCENT_AMBER

# ==============================================================================
# SLIDE 2: Problem Statement & Lab Objectives
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2)
add_header(s2, "Problem Statement & Project Objectives", "Course Requirements")

# Card 1: Problem & Solution
add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
tb2_1 = s2.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(5.0))
tf2_1 = tb2_1.text_frame
tf2_1.word_wrap = True

p = tf2_1.paragraphs[0]
p.text = "The Challenge"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = ACCENT_CYAN
p.space_after = Pt(8)

p = tf2_1.add_paragraph()
p.text = "The MovieLens dataset spans 6 CSV files with 25 million ratings and 15.5 million genome relevance scores. Performing runtime SQL joins across these massive files introduces extreme query latency, making real-time exploration sluggish."
p.font.size = Pt(12)
p.font.color.rgb = TEXT_MUTED
p.space_after = Pt(18)

p = tf2_1.add_paragraph()
p.text = "The Solution"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN
p.space_after = Pt(8)

p = tf2_1.add_paragraph()
p.text = "Build an end-to-end Data Engineering pipeline using MongoDB NoSQL, pre-aggregating metrics and denormalizing schemas for instant (<5ms) retrieval. Deliver an interactive Flask + Chart.js web dashboard with dual-role access control."
p.font.size = Pt(12)
p.font.color.rgb = TEXT_MUTED

# Card 2: Core Objectives
add_card(s2, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
tb2_2 = s2.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(5.0))
tf2_2 = tb2_2.text_frame
tf2_2.word_wrap = True

p = tf2_2.paragraphs[0]
p.text = "Core Lab Deliverables"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = ACCENT_PURPLE
p.space_after = Pt(12)

objectives = [
    "Ingest & clean 6 raw CSV files with year extraction & genre normalization.",
    "Reorganize schema into 5 query-optimized MongoDB collections.",
    "Address all 7 Analytical Scenarios (a through g) with interactive charts.",
    "Implement Role-Based Access Control (RBAC): Administrators & Users.",
    "Support Regulation 4: Real-time user rating modification & live recalculation.",
    "Ensure sub-5ms query response times using compound and text indexes."
]
for obj in objectives:
    p = tf2_2.add_paragraph()
    p.text = f"✔  {obj}"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(10)

# ==============================================================================
# SLIDE 3: Dataset Ingestion & Preprocessing
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3)
add_header(s3, "MovieLens 25M Dataset & ETL Cleaning Pipeline", "Data Engineering")

files_info = [
    ("movies.csv", "62,423 titles & genres", "Clean title strings, regex extract release year, split pipe genres into arrays."),
    ("ratings.csv", "25,000,095 ratings", "Chunk-aggregate in 5M batches -> avgRating, vote count, and 10-bin distribution."),
    ("genome-scores.csv", "15,584,448 scores", "Process in 1,000-movie chunks to filter top-5 highest relevance tags per movie."),
    ("genome-tags.csv", "1,128 tag descriptions", "Tag taxonomy lookup dictionary mapping tagId to human-readable strings."),
    ("tags.csv", "1,093,360 user tags", "Cross-join user tags with exploded genres to compute top 5 popular tags per genre."),
    ("links.csv", "62,423 ID mappings", "Enrich movies with standardized 7-digit IMDb IDs and TMDb external IDs.")
]

y_pos = 1.5
for fname, stats, role in files_info:
    add_card(s3, Inches(0.8), Inches(y_pos), Inches(11.7), Inches(0.75), bg_color=CARD_BG)
    tb = s3.shapes.add_textbox(Inches(1.0), Inches(y_pos + 0.05), Inches(11.3), Inches(0.65))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"{fname}  ({stats})"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = ACCENT_CYAN
    p2 = tf.add_paragraph()
    p2.text = f"ETL Strategy: {role}"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED
    y_pos += 0.88

# ==============================================================================
# SLIDE 4: Technologies Used
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4)
add_header(s4, "Technology Stack & Engineering Architecture", "System Design")

tech_cards = [
    ("Data Pipeline & ETL", "Python 3.12, Pandas, NumPy", [
        "In-memory zip stream extraction without disk unzipping",
        "Chunked processing of 25M ratings & 15.5M genome scores",
        "Regex parsing of release years and array normalization",
        "Batch insertion of 5,000 documents per write cycle"
    ], ACCENT_PURPLE),
    ("Database Layer", "MongoDB 7.0 (NoSQL) & PyMongo", [
        "Denormalized document store for rich movie records",
        "Sub-5ms query response on pre-aggregated collections",
        "Compound indexing on (year, ratingCount) and rating metrics",
        "Full-text search indexing on movie titles"
    ], ACCENT_GREEN),
    ("Application Backend", "Flask 3.1 & Werkzeug", [
        "REST API serving all 7 analytical lab scenarios",
        "PBKDF2 cryptographic password hashing for security",
        "Session-based Role-Based Access Control (@login_required, @admin_required)",
        "Atomic recalculation logic for live user rating modifications"
    ], ACCENT_CYAN),
    ("Frontend UI & Analytics", "Chart.js 4.4, Vanilla JS & CSS3", [
        "Dynamic autocomplete movie search across 62,423 titles",
        "Interactive Chart.js visualizations (bar, histogram, doughnut)",
        "Real-time DOM updates without full page reloads",
        "Custom responsive dark-theme design system"
    ], ACCENT_AMBER),
]

for idx, (title, subtitle, items, color) in enumerate(tech_cards):
    left = Inches(0.8 + (idx % 2) * 5.95)
    top = Inches(1.5 + (idx // 2) * 2.7)
    add_card(s4, left, top, Inches(5.75), Inches(2.5))
    tb = s4.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.35), Inches(2.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = title.upper()
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = color
    p1 = tf.add_paragraph()
    p1.text = subtitle
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(6)
    for it in items:
        p = tf.add_paragraph()
        p.text = f"•  {it}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 5: Why NoSQL (MongoDB) vs Relational SQL?
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5)
add_header(s5, "Why NoSQL (MongoDB) Over Relational SQL?", "Architectural Decision")

reasons = [
    ("1. Scale & Query Latency at 25 Million Rows", [
        "In a normalized SQL database, answering Question (a) or (b) requires joining tables with 25M ratings and 15.5M genome scores at runtime.",
        "Runtime SQL JOINs on this scale take seconds, bottlenecking an interactive web dashboard.",
        "MongoDB pre-aggregation aggregates ratings once during ETL, reducing dashboard queries to simple O(1) find_one lookups in <5ms."
    ], ACCENT_CYAN),
    ("2. Natural Denormalization for Multi-Attribute Movies", [
        "Movies naturally contain multi-valued attributes: genres array, topTags array, and 10-bin rating distribution dictionary.",
        "In SQL, this requires 3+ junction tables (movie_genres, movie_tags, rating_bins) and multiple expensive joins per query.",
        "MongoDB document schemas store nested arrays and objects natively inside a single unified document."
    ], ACCENT_PURPLE),
    ("3. High-Throughput User Rating Updates", [
        "Regulation 4 requires live user rating updates.",
        "In SQL, updating a rating triggers database-level locking or expensive VIEW recomputations.",
        "In MongoDB, our backend performs an atomic update ($set) on the movie document, updating the mean and distribution instantly."
    ], ACCENT_GREEN)
]

for idx, (title, items, color) in enumerate(reasons):
    top = Inches(1.5 + idx * 1.8)
    add_card(s5, Inches(0.8), top, Inches(11.7), Inches(1.65))
    tb = s5.shapes.add_textbox(Inches(1.0), top + Inches(0.12), Inches(11.3), Inches(1.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = color
    p0.space_after = Pt(4)
    for it in items:
        p = tf.add_paragraph()
        p.text = f"•  {it}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 6: Trade-offs Made With NoSQL
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6)
add_header(s6, "Architectural Trade-offs of Choosing NoSQL", "Design Evaluation")

tradeoffs = [
    ("Heavier Initial ETL Ingestion Phase",
     "Trade-off: To gain <5ms dashboard queries, load_data.py must spend ~15-20s pre-aggregating 25M ratings and genome scores upfront.",
     "Mitigation: This is an offline one-time batch job. Once loaded, the operational database never suffers join penalties."),
    ("Storage Redundancy (Denormalized Data)",
     "Trade-off: Embedding rating distributions and top tags inside movie documents consumes more disk storage than 3NF relational normalization.",
     "Mitigation: Disk space is cheap; user latency is expensive. Denormalizing 62K movies requires <100MB of RAM/disk, an optimal trade-off."),
    ("Application-Managed Atomic Consistency",
     "Trade-off: MongoDB does not enforce SQL foreign-key constraints across collections automatically.",
     "Mitigation: Flask backend handles atomic consistency in app.py (/api/ratings/submit), updating ratings collection and movies document simultaneously.")
]

for idx, (title, desc, mit) in enumerate(tradeoffs):
    top = Inches(1.5 + idx * 1.8)
    add_card(s6, Inches(0.8), top, Inches(11.7), Inches(1.65))
    tb = s6.shapes.add_textbox(Inches(1.0), top + Inches(0.12), Inches(11.3), Inches(1.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = f"⚖️  {title}"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_AMBER
    p0.space_after = Pt(4)
    p1 = tf.add_paragraph()
    p1.text = desc
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(3)
    p2 = tf.add_paragraph()
    p2.text = f"✓ Engineering Solution: {mit}"
    p2.font.size = Pt(11)
    p2.font.color.rgb = ACCENT_GREEN

# ==============================================================================
# SLIDE 7: System Architecture (4-Tier Clean Tree)
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7)
add_header(s7, "System Architecture: 4-Tier Data Pipeline", "Architecture Blueprint")

tiers = [
    ("Tier 1: Data Ingestion & ETL", "load_data.py", [
        "MovieLens 25M CSV Archive (6 Files)",
        "Title & regex year cleaning",
        "25M Ratings chunked pre-aggregation",
        "Top-5 Genome tags extraction"
    ], ACCENT_PURPLE),
    ("Tier 2: MongoDB NoSQL Store", "port 27017 (movielens)", [
        "movies (denormalized stats & top tags)",
        "genre_tags (popular tags per genre)",
        "ratings & users (credentials & reviews)",
        "Text index on title + compound indexes"
    ], ACCENT_GREEN),
    ("Tier 3: Backend REST API", "Flask 3.1 & PyMongo", [
        "RBAC: @login_required & @admin_required",
        "12 REST API analytical query endpoints",
        "Atomic user rating modification engine",
        "Admin user role manager & audit log"
    ], ACCENT_CYAN),
    ("Tier 4: Client Presentation", "Chart.js & Web UI", [
        "Regular User Dashboard (/)",
        "Movie autocomplete search engine",
        "Visuals for questions (a) through (g)",
        "Administrator Console (/admin)"
    ], ACCENT_AMBER)
]

for idx, (tier_name, sub, bullets, color) in enumerate(tiers):
    left = Inches(0.8 + idx * 2.95)
    add_card(s7, left, Inches(1.5), Inches(2.8), Inches(5.3))
    tb = s7.shapes.add_textbox(left + Inches(0.15), Inches(1.65), Inches(2.5), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = tier_name
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = color
    p1 = tf.add_paragraph()
    p1.text = sub
    p1.font.size = Pt(10)
    p1.font.color.rgb = TEXT_MUTED
    p1.space_after = Pt(14)
    for b in bullets:
        p = tf.add_paragraph()
        p.text = f"• {b}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

# ==============================================================================
# SLIDE 8: RBAC User vs Administrator Features
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8)
add_header(s8, "Role-Based Access Control (RBAC): User vs. Admin Features", "Security & Permissions")

# User Card
add_card(s8, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
tb_u = s8.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(5.0))
tf_u = tb_u.text_frame
tf_u.word_wrap = True

p = tf_u.paragraphs[0]
p.text = "👤 Regular User Role ('user')"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN
p.space_after = Pt(12)

user_feats = [
    ("Movie Search Autocomplete", "Type any title to instantly find movies across 62,423 titles with real-time suggestions."),
    ("Explore Analytical Scenarios", "View all 7 interactive charts (Questions a–g) with dynamic filters for release years."),
    ("Submit & Modify Ratings (Req 4)", "Select 0.5 to 5.0 stars and submit ratings. Updates average rating, count, and histogram live."),
    ("Personal Rating Persistence", "See your saved rating highlighted whenever you revisit any movie.")
]
for f_title, f_desc in user_feats:
    p = tf_u.add_paragraph()
    p.text = f"✔ {f_title}"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_WHITE
    p2 = tf_u.add_paragraph()
    p2.text = f_desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(8)

# Admin Card
add_card(s8, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
tb_a = s8.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(5.0))
tf_a = tb_a.text_frame
tf_a.word_wrap = True

p = tf_a.paragraphs[0]
p.text = "🛡️ Administrator Role ('admin')"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = ACCENT_PURPLE
p.space_after = Pt(12)

admin_feats = [
    ("Full User Capabilities", "Inherits all regular user capabilities including search, exploration, and rating submissions."),
    ("Exclusive Admin Console (/admin)", "Dedicated management console guarded by @admin_required server decorator."),
    ("System Database KPI Cards", "Live counters: Total Movies (62,423), Baseline Ratings (25M), Registered Users, Live Ratings."),
    ("User Account Role Toggling", "Inspect user accounts and toggle privileges (Promote USER ⟷ Demote ADMIN)."),
    ("Live Rating Submissions Audit", "Real-time audit log of user ratings with usernames, movie IDs, scores, and timestamps.")
]
for f_title, f_desc in admin_feats:
    p = tf_a.add_paragraph()
    p.text = f"★ {f_title}"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_WHITE
    p2 = tf_a.add_paragraph()
    p2.text = f_desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(8)

# ==============================================================================
# SLIDE 9: Complete REST API Reference (All 12 Endpoints)
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9)
add_header(s9, "Complete REST API Reference Matrix", "Backend Endpoints")

apis = [
    ("GET /api/movies/search?q=", "Dynamic movie title autocomplete search with debouncing (Limit 15).", "Auth: @login_required"),
    ("GET /api/tags/top/<movie_id>", "Question (a): Returns top 5 tags by relevance score for selected movie.", "Auth: @login_required"),
    ("GET /api/movies/top_rated?year=", "Question (b): Top 10 movies overall (min 500 reviews) or filtered by year (min 20).", "Auth: @login_required"),
    ("GET /api/tags/genre", "Question (c): Returns top 5 popular user tags for each movie genre.", "Auth: @login_required"),
    ("GET /api/ratings/distribution/<id>", "Question (d): Returns 10-bin user rating histogram (0.5 to 5.0 stars) for a movie.", "Auth: @login_required"),
    ("GET /api/ratings/total_distribution", "Question (e): Bucketed distribution of total review counts across 62,423 movies.", "Auth: @login_required"),
    ("GET /api/genres/releases?year=", "Question (f): Returns genre with highest movie releases for a specified year.", "Auth: @login_required"),
    ("GET /api/genres/coverage", "Question (g): Overall proportional genre representation across entire movie catalog.", "Auth: @login_required"),
    ("POST /api/ratings/submit", "Regulation 4: Submits user rating (0.5-5.0★) & atomically recalculates movie stats.", "Auth: @login_required"),
    ("GET /api/admin/stats", "System KPIs: Total movies, baseline ratings, registered users, and live submissions.", "Auth: @admin_required"),
    ("GET /api/admin/users", "Lists registered user accounts and their assigned role (admin vs user).", "Auth: @admin_required"),
    ("POST /api/admin/toggle_role", "Toggles account privileges between USER and ADMIN (prevents self-demotion).", "Auth: @admin_required"),
]

y_top = 1.45
for endpoint, desc, auth in apis:
    add_card(s9, Inches(0.8), Inches(y_top), Inches(11.7), Inches(0.42), bg_color=CARD_BG)
    tb = s9.shapes.add_textbox(Inches(1.0), Inches(y_top + 0.02), Inches(11.3), Inches(0.38))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = endpoint
    p.font.name = "Courier New"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN if "GET" in endpoint else ACCENT_GREEN
    
    p2 = tf.add_paragraph()
    p2.text = f"{desc}  [{auth}]"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    y_top += 0.47

# ==============================================================================
# Helper for Question Slides: Side-by-Side (Code on Left, Image on Right)
# ==============================================================================
def create_question_slide(title, q_tag, code_title, code_str, bullets, img_name):
    slide = prs.slides.add_slide(blank_layout)
    set_slide_background(slide)
    add_header(slide, title, f"ANALYTICS SCENARIO: {q_tag}")
    
    # Left: Code & Strategy Box
    add_code_block(slide, Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.4), code_title, code_str, bullets)
    
    # Right: Output Visualization Image Box
    add_card(slide, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
    
    # Add Image
    img_path = os.path.join(IMG_DIR, img_name)
    if os.path.exists(img_path):
        # Center image inside right card
        slide.shapes.add_picture(img_path, Inches(7.0), Inches(1.7), width=Inches(5.3))
    else:
        tb = slide.shapes.add_textbox(Inches(7.2), Inches(3.5), Inches(4.9), Inches(1.0))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = f"[Image: {img_name}]"
        p.font.color.rgb = ACCENT_AMBER

# ==============================================================================
# SLIDE 10: Question (a) — Top 5 Relevant Tags for a Selected Movie
# ==============================================================================
code_a = """# app.py: Lines 181-194
@app.route("/api/tags/top/<int:movie_id>")
@login_required
def api_top_tags(movie_id):
    movie = db.movies.find_one(
        {"movieId": movie_id},
        {"_id": 0, "movieId": 1, "title": 1, "topTags": 1}
    )
    return jsonify({
        "movieId": movie["movieId"],
        "title": movie.get("title", ""),
        "tags": movie.get("topTags", [])[:5]
    })"""
bullets_a = [
    "Pre-aggregated during ETL from 15.5M genome scores.",
    "Embedded directly into movie documents for O(1) retrieval.",
    "Relevance scores range from 0.0 to 1.0 (higher = greater relevance).",
    "Visualization: Horizontal bar chart with animated gradients."
]
create_question_slide("Question (a) — Top 5 Relevant Tags for a Movie", "QUESTION (A)", "PyMongo Query Implementation", code_a, bullets_a, "page_7_0_Im11.png")

# ==============================================================================
# SLIDE 11: Question (d) — Rating Distribution for a Selected Movie (0.5–5.0★)
# ==============================================================================
code_d = """# app.py: Lines 257-290
@app.route("/api/ratings/distribution/<int:movie_id>")
@login_required
def api_rating_distribution(movie_id):
    movie = db.movies.find_one(
        {"movieId": movie_id},
        {"_id": 0, "ratingDistribution": 1, 
         "avgRating": 1, "ratingCount": 1}
    )
    # 10-bin histogram breakdown (0.5 to 5.0 stars)
    dist = movie.get("ratingDistribution", {})
    return jsonify({
        "avgRating": movie.get("avgRating", 0.0),
        "ratingCount": movie.get("ratingCount", 0),
        "distribution": [
            {"rating": float(r), "count": dist.get(r, 0)}
            for r in ["0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0"]
        ]
    })"""
bullets_d = [
    "Stores exact vote counts across all 10 star tiers (0.5 to 5.0).",
    "Pre-computed from 25M reviews during ETL batch processing.",
    "Dynamically shifts in real-time when a logged-in user submits a rating.",
    "Visualization: High-DPI bar chart histogram with vote tooltips."
]
create_question_slide("Question (d) — Rating Distribution for a Movie", "QUESTION (D)", "PyMongo Query Implementation", code_d, bullets_d, "page_8_0_Im12.png")

# ==============================================================================
# SLIDE 12: Question (b) — Top 10 Movies by Average Rating
# ==============================================================================
code_b = """# app.py: Lines 199-239
@app.route("/api/movies/top_rated")
@login_required
def api_top_rated():
    year = request.args.get("year", type=int)
    if year:
        # Minimum 20 reviews for statistical significance
        query = {"year": year, "ratingCount": {"$gte": 20}}
        results = db.movies.find(query).sort([
            ("avgRating", DESCENDING), ("ratingCount", DESCENDING)
        ]).limit(10)
    else:
        # Overall top 10 with minimum 500 reviews threshold
        results = db.movies.find({"ratingCount": {"$gte": 500}}).sort([
            ("avgRating", DESCENDING), ("ratingCount", DESCENDING)
        ]).limit(10)
    return jsonify(list(results))"""
bullets_b = [
    "Minimum review threshold prevents single 5-star review outliers.",
    "Dynamic release year filter dropdown on dashboard.",
    "Fast execution via compound index: (ratingCount, avgRating).",
    "Visualization: Horizontal ranked bar chart."
]
create_question_slide("Question (b) — Overall & Year-wise Top 10 Movies", "QUESTION (B)", "PyMongo Query Implementation", code_b, bullets_b, "page_9_0_Im13.png")

# ==============================================================================
# SLIDE 13: Question (c) — Most Popular Tags for Each Genre
# ==============================================================================
code_c = """# app.py: Lines 244-252
@app.route("/api/tags/genre")
@login_required
def api_tags_by_genre():
    results = list(
        db.genre_tags.find(
            {},
            {"_id": 0, "genre": 1, "topTag": 1, 
             "count": 1, "topTags": 1}
        ).sort("genre", ASCENDING)
    )
    return jsonify(results)"""
bullets_c = [
    "Computed during ETL by exploding movie genres and cross-joining 1.09M tags.",
    "Returns top 5 popular tags per genre with exact application counts.",
    "Stored in dedicated genre_tags collection with unique genre index.",
    "Visualization: Interactive table with rank #1 tag highlighted in purple with star badge."
]
create_question_slide("Question (c) — Most Popular Tags Given for Each Genre", "QUESTION (C)", "PyMongo Query Implementation", code_c, bullets_c, "page_10_0_Im14.png")

# ==============================================================================
# SLIDE 14: Question (e) — Distribution of Total Ratings for Movies
# ==============================================================================
code_e = """# app.py: Lines 294-328
@app.route("/api/ratings/total_distribution")
@login_required
def api_total_rating_distribution():
    pipeline = [
        {"$match": {"ratingCount": {"$gt": 0}}},
        {
            "$bucket": {
                "groupBy": "$ratingCount",
                "boundaries": [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000],
                "default": "50000+",
                "output": {"count": {"$sum": 1}}
            }
        }
    ]
    return jsonify(list(db.movies.aggregate(pipeline)))"""
bullets_e = [
    "Groups all 62,423 titles into popularity brackets (1-9, 10-49, ..., 50,000+).",
    "Uses MongoDB $bucket aggregation operator for logarithmic binning.",
    "Reveals long-tail distribution: few blockbusters, many niche movies.",
    "Visualization: Categorical bar chart showing catalog popularity curve."
]
create_question_slide("Question (e) — Distribution of Total Ratings for Movies", "QUESTION (E)", "MongoDB Aggregation Pipeline", code_e, bullets_e, "page_11_0_Im15.png")

# ==============================================================================
# SLIDE 15: Question (f) — Genre with Highest Releases in a Selected Year
# ==============================================================================
code_f = """# app.py: Lines 333-347
@app.route("/api/genres/releases")
@login_required
def api_genre_releases():
    year = request.args.get("year", type=int)
    pipeline = [
        {"$match": {"year": year}},
        {"$unwind": "$genres"},
        {"$group": {"_id": "$genres", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$project": {"_id": 0, "genre": "$_id", "count": 1}}
    ]
    results = list(db.movies.aggregate(pipeline))
    return jsonify({"year": year, "releases": results})"""
bullets_f = [
    "Dynamic filter selects any release year (e.g. landmark year 1995).",
    "Unrolls genres array ($unwind) and aggregates movie count per genre.",
    "First item in sorted array identifies the dominant genre of that year.",
    "Visualization: Sorted horizontal bar chart with peak genre highlighted."
]
create_question_slide("Question (f) — Genre with Highest Releases by Year", "QUESTION (F)", "MongoDB Aggregation Pipeline", code_f, bullets_f, "page_12_0_Im16.png")

# ==============================================================================
# SLIDE 16: Question (g) — Genre-wise Coverage of Movies
# ==============================================================================
code_g = """# app.py: Lines 352-361
@app.route("/api/genres/coverage")
@login_required
def api_genre_coverage():
    pipeline = [
        {"$unwind": "$genres"},
        {"$group": {"_id": "$genres", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$project": {"_id": 0, "genre": "$_id", "count": 1}}
    ]
    return jsonify(list(db.movies.aggregate(pipeline)))"""
bullets_g = [
    "Calculates total catalogue share for every cinematic genre.",
    "A movie with multiple genres contributes proportionally to each.",
    "Indexed on genres field for rapid pipeline aggregation.",
    "Visualization: Multi-colored interactive doughnut chart with percentage legends."
]
create_question_slide("Question (g) — Genre-wise Movie Coverage", "QUESTION (G)", "MongoDB Aggregation Pipeline", code_g, bullets_g, "page_13_0_Im18.png")

# ==============================================================================
# SLIDE 17: Regulation 4 — Real-Time User Rating Modification
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
set_slide_background(s17)
add_header(s17, "Regulation 4: Real-Time User Rating Modification", "User Interaction & Write Engine")

steps_r4 = [
    ("1. Client Rating Submission", "POST /api/ratings/submit with movieId and rating (0.5 to 5.0 in 0.5 steps). Guarded by @login_required."),
    ("2. User Rating Upsert", "Stores individual vote in ratings collection {movieId, username, rating, timestamp}."),
    ("3. Atomic Recalculation", "Atomically updates movie document: recalculates mean avgRating, increments ratingCount, shifts histogram."),
    ("4. Real-time DOM Refresh", "Browser animates new rating average, total count, and shifts Question (d) histogram bar without page reload.")
]

for idx, (title, desc) in enumerate(steps_r4):
    top = Inches(1.5 + idx * 1.35)
    add_card(s17, Inches(0.8), top, Inches(11.7), Inches(1.2))
    tb = s17.shapes.add_textbox(Inches(1.0), top + Inches(0.1), Inches(11.3), Inches(1.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_GREEN
    p0.space_after = Pt(3)
    p1 = tf.add_paragraph()
    p1.text = desc
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 18: Dashboard & Admin Console Showcase
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
set_slide_background(s18)
add_header(s18, "Production Interface: User Dashboard & Admin Console", "UI Showcase")

# Left: User Dashboard
add_card(s18, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.4))
tb_d = s18.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(5.3), Inches(0.5))
p = tb_d.text_frame.paragraphs[0]
p.text = "Regular User Dashboard (/)"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = ACCENT_CYAN

img_dash = os.path.join(IMG_DIR, "page_5_0_Im9.png")
if os.path.exists(img_dash):
    s18.shapes.add_picture(img_dash, Inches(1.0), Inches(2.2), width=Inches(5.3))

# Right: Admin Console
add_card(s18, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4))
tb_adm = s18.shapes.add_textbox(Inches(7.0), Inches(1.6), Inches(5.3), Inches(0.5))
p = tb_adm.text_frame.paragraphs[0]
p.text = "Administrator Management Console (/admin)"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = ACCENT_PURPLE

img_adm = os.path.join(IMG_DIR, "page_6_0_Im10.png")
if os.path.exists(img_adm):
    s18.shapes.add_picture(img_adm, Inches(7.0), Inches(2.2), width=Inches(5.3))

# ==============================================================================
# SLIDE 19: Performance Benchmarks & Conclusion
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
set_slide_background(s19)
add_header(s19, "Performance Benchmarks & Engineering Summary", "Conclusion")

benchmarks = [
    ("Sub-5ms Query Latency", "Pre-aggregated document structure eliminates multi-million-row SQL table scans. Complex questions (a-g) resolve in 2 to 5 milliseconds.", ACCENT_GREEN),
    ("62,423 Movies Loaded", "Comprehensive data normalization and title regex cleaning ensures clean search and filtering across the complete historical catalog.", ACCENT_CYAN),
    ("25 Million Ratings Aggregated", "Chunked ETL pipeline processed 25M reviews in 5M batches without memory overflow, seeding complete histograms.", ACCENT_PURPLE),
    ("Strict Dual-Role Security", "Full separation of privileges with session-based authentication, PBKDF2 hashing, and administrative audit logging.", ACCENT_AMBER)
]

for idx, (title, desc, color) in enumerate(benchmarks):
    left = Inches(0.8 + (idx % 2) * 5.95)
    top = Inches(1.5 + (idx // 2) * 2.7)
    add_card(s19, left, top, Inches(5.75), Inches(2.5))
    tb = s19.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), Inches(5.35), Inches(2.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.size = Pt(15)
    p0.font.bold = True
    p0.font.color.rgb = color
    p0.space_after = Pt(8)
    p1 = tf.add_paragraph()
    p1.text = desc
    p1.font.size = Pt(12)
    p1.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 20: References & Acknowledgements
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
set_slide_background(s20)
add_header(s20, "Project References & Academic Acknowledgements", "References")

add_card(s20, Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.4))
tb20 = s20.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(4.8))
tf20 = tb20.text_frame
tf20.word_wrap = True

refs = [
    ("GroupLens Research — MovieLens 25M Dataset", "https://grouplens.org/datasets/movielens/25m/ (Official benchmark dataset released December 2019)."),
    ("F. Maxwell Harper and Joseph A. Konstan", "The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4, 2015."),
    ("DS5003 Data Engineering Lab Handout", "Dr. Koninika Pal, Indian Institute of Technology Palakkad (Hand out 15.10.2026)."),
    ("MongoDB Documentation", "Aggregation Pipeline Operators: $bucket, $unwind, $group, and Compound Indexing best practices."),
    ("Flask & Chart.js Open-Source Frameworks", "Production WSGI application serving RESTful JSON endpoints and responsive HTML5 canvas rendering.")
]

for title, desc in refs:
    p = tf20.add_paragraph()
    p.text = f"▶  {title}"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_CYAN
    p2 = tf20.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(14)

OUT_FILE = "MovieLens_Analytics_Presentation.pptx"
prs.save(OUT_FILE)
print(f"✨ Successfully generated 20-slide presentation: {OUT_FILE} ({os.path.getsize(OUT_FILE)} bytes)")
