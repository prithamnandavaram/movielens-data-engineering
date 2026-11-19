
#set page(
  width: 29.7cm,
  height: 16.7cm,
  margin: (x: 1.6cm, y: 1.2cm),
  fill: rgb("#0f141f"),
  header: none,
  footer: text(fill: rgb("#8c96aa"), size: 8.5pt)[
    #grid(
      columns: (1fr, 1fr),
      align(left)[DS5003 Data Engineering Lab | IIT Palakkad | MovieLens 25M Analytics Platform],
      align(right)[Project Presentation]
    )
  ]
)

#set text(font: "Helvetica", fill: rgb("#f5f7fa"), size: 10.5pt)

#let card(title: none, category: "DATA ENGINEERING | DS5003", body) = {
  if title != none {
    v(0.1cm)
    text(fill: rgb("#7c5cff"), weight: "bold", size: 9pt)[#upper(category)]
    v(-0.25cm)
    text(fill: rgb("#f5f7fa"), weight: "bold", size: 17pt)[#title]
    v(0.2cm)
  }
  body
}

#let codebox(title, code, bullets: ()) = {
  rect(
    fill: rgb("#161b28"),
    stroke: 1pt + rgb("#2d374e"),
    radius: 8pt,
    width: 100%,
    inset: 10pt,
    [
      #text(fill: rgb("#00c0f0"), weight: "bold", size: 9.5pt)[#upper(title)]
      #v(4pt)
      #rect(
        fill: rgb("#0e121b"),
        stroke: 0.5pt + rgb("#2d374e"),
        radius: 4pt,
        width: 100%,
        inset: 6pt,
        [
          #set text(font: "Courier", size: 7.5pt, fill: rgb("#f5f7fa"))
          #raw(code)
        ]
      )
      #v(4pt)
      #for b in bullets [
        #text(fill: rgb("#8c96aa"), size: 8.5pt)[▶ #b]       ]
    ]
  )
}

// ==============================================================================
// SLIDE 1: Title Slide
// ==============================================================================
#align(center + horizon)[
  #rect(
    fill: rgb("#161b28"),
    stroke: 1.5pt + rgb("#7c5cff"),
    radius: 12pt,
    inset: 24pt,
    width: 90%,
    [
      #text(fill: rgb("#7c5cff"), weight: "bold", size: 11pt)[DS5003 DATA ENGINEERING LAB • PROJECT PRESENTATION] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 26pt)[MovieLens 25M Analytics Platform] \       #text(fill: rgb("#00c0f0"), size: 13pt)[High-Performance NoSQL Data Pipeline, Role-Based Access & Interactive Visualizations] \       #v(0.6cm)
      #text(fill: rgb("#8c96aa"), size: 11pt)[Presented by:]       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 12pt)[
        Ben George (142613005)  •  Nandavaram Shashi Pritham (142602010)  •  Paltasingi Abhishek Sonu (142602013)
      ] \       #v(0.3cm)
      #text(fill: rgb("#ffb72b"), size: 10.5pt)[Faculty: Dr. Koninika Pal  •  Indian Institute of Technology Palakkad]
    ]
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 2: Problem Statement & Objectives
// ==============================================================================
#card(title: "Problem Statement & Project Objectives", category: "Lab Specifications")[
  #grid(
    columns: (1fr, 1fr),
    gutter: 16pt,
    rect(
      fill: rgb("#161b28"),
      stroke: 1pt + rgb("#2d374e"),
      radius: 8pt,
      inset: 14pt,
      [
        #text(fill: rgb("#00c0f0"), weight: "bold", size: 13pt)[The Challenge] \         #text(fill: rgb("#8c96aa"), size: 10pt)[
          The MovieLens dataset spans 6 CSV files with *25 million ratings* and *15.5 million genome scores*. Performing runtime SQL joins across these massive relational files introduces severe query latency and CPU bottlenecks, making real-time dashboard analytics unresponsive.
        ] \         #text(fill: rgb("#00e5a3"), weight: "bold", size: 13pt)[The Solution] \         #text(fill: rgb("#8c96aa"), size: 10pt)[
          Build an end-to-end Data Engineering pipeline using *MongoDB NoSQL*, pre-aggregating metrics and denormalizing schemas for instant *(\< 5ms)* retrieval. Deliver an interactive Flask + Chart.js web dashboard with dual-role access control.
        ]
      ]
    ),
    rect(
      fill: rgb("#161b28"),
      stroke: 1pt + rgb("#2d374e"),
      radius: 8pt,
      inset: 14pt,
      [
        #text(fill: rgb("#7c5cff"), weight: "bold", size: 13pt)[Core Lab Deliverables] \         #list(
          [Ingest & clean 6 raw CSV files with year extraction & genre normalization.],
          [Reorganize schema into 5 query-optimized MongoDB collections.],
          [Address all 7 Analytical Scenarios (a through g) with interactive charts.],
          [Implement Role-Based Access Control (RBAC): Administrators & Users.],
          [Support Regulation 4: Real-time user rating modification & live recalculation.],
          [Ensure sub-5ms query response times using compound and text indexes.]
        )
      ]
    )
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 3: Technologies Used
// ==============================================================================
#card(title: "Technology Stack & Engineering Architecture", category: "System Design")[
  #grid(
    columns: (1fr, 1fr),
    gutter: 14pt,
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, [
      #text(fill: rgb("#7c5cff"), weight: "bold", size: 12pt)[DATA PIPELINE & ETL]       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 11pt)[Python 3.12, Pandas, NumPy] \       #list(
        [In-memory zip stream extraction without disk unzipping],
        [Chunked processing of 25M ratings in 5M-row batches],
        [Regex parsing of release years and array normalization],
        [Batch insertion of 5,000 documents per write cycle]
      )
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, [
      #text(fill: rgb("#00e5a3"), weight: "bold", size: 12pt)[DATABASE TIER]       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 11pt)[MongoDB 7.0 (NoSQL) & PyMongo] \       #list(
        [Denormalized document store for rich movie records],
        [Sub-5ms query response on pre-aggregated collections],
        [Compound indexing on (year, ratingCount) and rating metrics],
        [Full-text search indexing on movie titles for autocomplete]
      )
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, [
      #text(fill: rgb("#00c0f0"), weight: "bold", size: 12pt)[APPLICATION BACKEND]       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 11pt)[Flask 3.1 & Werkzeug] \       #list(
        [REST API serving all 7 analytical lab scenarios],
        [PBKDF2 cryptographic password hashing for security],
        [Session-based RBAC (`@login_required`, `@admin_required`)],
        [Atomic recalculation logic for live user rating modifications]
      )
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, [
      #text(fill: rgb("#ffb72b"), weight: "bold", size: 12pt)[FRONTEND UI & ANALYTICS]       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 11pt)[Chart.js 4.4, Vanilla JS & CSS3] \       #list(
        [Dynamic autocomplete movie search across 62,423 titles],
        [Interactive Chart.js visualizations (bar, histogram, doughnut)],
        [Real-time DOM updates without full page reloads],
        [Custom responsive dark-theme design system]
      )
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 4: Why NoSQL (MongoDB) vs Relational SQL
// ==============================================================================
#card(title: "Why NoSQL (MongoDB) Over Relational SQL?", category: "Architectural Decision")[
  #v(4pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#00c0f0"), weight: "bold", size: 12pt)[1. Scale & Query Latency at 25 Million Rows]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[
      • In a normalized SQL database, answering Question (a) or (b) requires joining tables with 25M ratings and 15.5M genome scores at runtime.       • Runtime SQL JOINs on this scale take several seconds, bottlenecking an interactive web dashboard.       • MongoDB pre-aggregation aggregates ratings once during ETL, reducing dashboard queries to simple O(1) find_one lookups in *\< 5ms*.
    ]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#7c5cff"), weight: "bold", size: 12pt)[2. Natural Denormalization for Multi-Attribute Movies]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[
      • Movies naturally contain multi-valued attributes: genres array, topTags array, and 10-bin rating distribution dictionary.       • In SQL, this requires 3+ junction tables (movie_genres, movie_tags, rating_bins) and multiple expensive joins per query.       • MongoDB document schemas store nested arrays and objects natively inside a single unified document.
    ]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#00e5a3"), weight: "bold", size: 12pt)[3. High-Throughput User Rating Updates (Regulation 4)]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[
      • Regulation 4 requires live user rating updates. In SQL, updating a rating triggers database-level locking or expensive VIEW recomputations.       • In MongoDB, our backend performs an atomic update (\$set) on the movie document, updating the mean and distribution instantly.
    ]
  ])
]

#pagebreak()

// ==============================================================================
// SLIDE 5: Architectural Trade-offs
// ==============================================================================
#card(title: "Architectural Trade-offs of Choosing NoSQL", category: "Design Evaluation")[
  #v(4pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#ffb72b"), weight: "bold", size: 12pt)[⚖️ Heavier Initial ETL Ingestion Phase]     #text(fill: rgb("#f5f7fa"), size: 10pt)[*Trade-off:* To gain \< 5ms dashboard queries, load_data.py must spend ~15-20s pre-aggregating 25M ratings upfront.]     #text(fill: rgb("#00e5a3"), size: 9.5pt)[*✓ Solution:* This is an offline one-time batch job. Once loaded, the operational database never suffers runtime join penalties.]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#ffb72b"), weight: "bold", size: 12pt)[⚖️ Storage Redundancy (Denormalized Data)]     #text(fill: rgb("#f5f7fa"), size: 10pt)[*Trade-off:* Embedding rating distributions and top tags inside movie documents consumes more disk space than 3NF normalization.]     #text(fill: rgb("#00e5a3"), size: 9.5pt)[*✓ Solution:* Disk storage is cheap; user latency is expensive. Denormalizing 62K movies requires \< 100MB of RAM/disk, an optimal trade-off.]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#ffb72b"), weight: "bold", size: 12pt)[⚖️ Application-Managed Consistency]     #text(fill: rgb("#f5f7fa"), size: 10pt)[*Trade-off:* MongoDB does not enforce SQL foreign-key constraints across collections automatically.]     #text(fill: rgb("#00e5a3"), size: 9.5pt)[*✓ Solution:* Flask backend handles atomic consistency in app.py (/api/ratings/submit), updating ratings collection and movies document simultaneously.]
  ])
]

#pagebreak()

// ==============================================================================
// SLIDE 6: System Architecture (4-Tier Clean Tree)
// ==============================================================================
#card(title: "System Architecture: 4-Tier Data Pipeline", category: "Architecture Blueprint")[
  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    gutter: 10pt,
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#7c5cff"), radius: 8pt, inset: 10pt, [
      #text(fill: rgb("#7c5cff"), weight: "bold", size: 11pt)[Tier 1: ETL Pipeline]       #text(fill: rgb("#8c96aa"), size: 8.5pt)[load_data.py] \       #list(
        [6 MovieLens CSV files],
        [Regex year extraction],
        [25M ratings chunked aggregation],
        [Top-5 genome extraction],
        [User tag x genre join]
      )
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#00e5a3"), radius: 8pt, inset: 10pt, [
      #text(fill: rgb("#00e5a3"), weight: "bold", size: 11pt)[Tier 2: MongoDB Store]       #text(fill: rgb("#8c96aa"), size: 8.5pt)[port 27017 (movielens)] \       #list(
        [movies (stats, dist, tags)],
        [genre_tags (popular tags)],
        [genome_tags (lookup)],
        [ratings (live reviews)],
        [users (PBKDF2 hashes)]
      )
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#00c0f0"), radius: 8pt, inset: 10pt, [
      #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[Tier 3: Backend API]       #text(fill: rgb("#8c96aa"), size: 8.5pt)[Flask 3.1 & PyMongo] \       #list(
        [RBAC: `@login_required`],
        [RBAC: `@admin_required`],
        [12 REST query endpoints],
        [Atomic rating write engine],
        [Admin user role manager]
      )
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#ffb72b"), radius: 8pt, inset: 10pt, [
      #text(fill: rgb("#ffb72b"), weight: "bold", size: 11pt)[Tier 4: Presentation]       #text(fill: rgb("#8c96aa"), size: 8.5pt)[Chart.js & Web UI] \       #list(
        [User Dashboard (/)],
        [Autocomplete movie search],
        [Interactive charts (a-g)],
        [Admin Console (/admin)],
        [Live rating feedback loop]
      )
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 7: RBAC User vs Administrator Features
// ==============================================================================
#card(title: "Role-Based Access Control (RBAC): User vs. Admin Features", category: "Security & Permissions")[
  #grid(
    columns: (1fr, 1fr),
    gutter: 16pt,
    rect(fill: rgb("#161b28"), stroke: 1.5pt + rgb("#00e5a3"), radius: 8pt, inset: 14pt, [
      #text(fill: rgb("#00e5a3"), weight: "bold", size: 13pt)[👤 Regular User Role ('user')] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[✔ Movie Search Autocomplete]       #text(fill: rgb("#8c96aa"), size: 9pt)[Type any title to instantly find movies across 62,423 titles with real-time suggestions.] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[✔ Explore All Analytical Scenarios]       #text(fill: rgb("#8c96aa"), size: 9pt)[View all 7 interactive charts (Questions a–g) with dynamic filters for release years.] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[✔ Submit & Modify Ratings (Regulation 4)]       #text(fill: rgb("#8c96aa"), size: 9pt)[Select 0.5 to 5.0 stars and submit ratings. Updates average rating, count, and histogram live.] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[✔ Personal Rating Persistence]       #text(fill: rgb("#8c96aa"), size: 9pt)[See your saved rating highlighted whenever you revisit any movie.]
    ]),
    rect(fill: rgb("#161b28"), stroke: 1.5pt + rgb("#7c5cff"), radius: 8pt, inset: 14pt, [
      #text(fill: rgb("#7c5cff"), weight: "bold", size: 13pt)[🛡️ Administrator Role ('admin')] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[★ Full User Capabilities Included]       #text(fill: rgb("#8c96aa"), size: 9pt)[Inherits all regular user capabilities including search, exploration, and rating submissions.] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[★ Exclusive Admin Console (/admin)]       #text(fill: rgb("#8c96aa"), size: 9pt)[Dedicated management console guarded by `@admin_required` server decorator.] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[★ System Database KPI Cards]       #text(fill: rgb("#8c96aa"), size: 9pt)[Live counters: Total Movies (62,423), Baseline Ratings (25M), Registered Users, Live Ratings.] \       #text(fill: rgb("#f5f7fa"), weight: "bold", size: 10.5pt)[★ User Role Management & Audit Trail]       #text(fill: rgb("#8c96aa"), size: 9pt)[Toggle privileges (USER ⟷ ADMIN) and view audit history of all live rating submissions.]
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 8: Complete REST API Reference Matrix
// ==============================================================================
#card(title: "Complete REST API Reference Matrix", category: "Backend Endpoints")[
  #set text(size: 8pt)
  #table(
    columns: (2.2fr, 4.5fr, 1.8fr),
    fill: (x, y) => if y == 0 { rgb("#161b28") } else if calc.even(y) { rgb("#121621") } else { rgb("#161b28") },
    stroke: 0.5pt + rgb("#2d374e"),
    inset: 4pt,
    [*Endpoint Route*], [*Description & Analytical Question*], [*Access Level*],
    [GET /api/movies/search?q=], [Dynamic movie title autocomplete search (Limit 15)], [`@login_required`],
    [GET /api/tags/top/\<id\>], [Question (a): Returns top 5 tags by relevance for selected movie], [`@login_required`],
    [GET /api/movies/top_rated?year=], [Question (b): Top 10 movies overall (min 500) or by year (min 20)], [`@login_required`],
    [GET /api/tags/genre], [Question (c): Returns top 5 popular user tags for each movie genre], [`@login_required`],
    [GET /api/ratings/distribution/\<id\>], [Question (d): Returns 10-bin rating histogram (0.5 to 5.0 stars)], [`@login_required`],
    [GET /api/ratings/total_distribution], [Question (e): Bucketed distribution of total reviews across 62K movies], [`@login_required`],
    [GET /api/genres/releases?year=], [Question (f): Returns genre with highest releases for a specified year], [`@login_required`],
    [GET /api/genres/coverage], [Question (g): Overall proportional genre representation in catalog], [`@login_required`],
    [POST /api/ratings/submit], [Regulation 4: Submits rating (0.5-5.0★) & atomically updates movie stats], [`@login_required`],
    [GET /api/admin/stats], [System KPIs: Total movies, baseline ratings, users, live ratings], [`@admin_required`],
    [GET /api/admin/users], [Lists registered accounts and assigned roles (admin vs user)], [`@admin_required`],
    [POST /api/admin/toggle_role], [Toggles privileges between USER and ADMIN roles], [`@admin_required`]
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 9: User Dashboard & Admin Console
// ==============================================================================
#card(title: "Production Interface: User Dashboard & Admin Console", category: "UI Showcase")[
  #grid(
    columns: (1fr, 1fr),
    gutter: 14pt,
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 10pt, [
      #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[Regular User Dashboard (/)]       #v(6pt)
      #image("screenshots/extracted/page_5_0_Im9.png", width: 100%)
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 10pt, [
      #text(fill: rgb("#7c5cff"), weight: "bold", size: 11pt)[Administrator Console (/admin)]       #v(6pt)
      #image("screenshots/extracted/page_6_0_Im10.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 10: Question (a) — Top 5 Relevant Tags for a Selected Movie
// ==============================================================================
#card(title: "Question (a) — Top 5 Relevant Tags for a Movie", category: "ANALYTICS SCENARIO: QUESTION (A)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "PyMongo Query Implementation",
      "db.movies.find_one(\n  {\"movieId\": movie_id},\n  {\"_id\": 0, \"movieId\": 1, \"title\": 1, \"topTags\": 1}\n)",
      bullets: (
        "Pre-aggregated during ETL from 15.5M genome scores.",
        "Embedded directly into movie documents for O(1) retrieval in \< 2ms.",
        "Relevance scores range from 0.0 to 1.0 (higher = greater relevance).",
        "Visualization: Horizontal bar chart with animated gradients."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_7_0_Im11.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 11: Question (d) — Rating Distribution for a Selected Movie
// ==============================================================================
#card(title: "Question (d) — Rating Distribution for a Movie (0.5–5.0★)", category: "ANALYTICS SCENARIO: QUESTION (D)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "PyMongo Query Implementation",
      "movie = db.movies.find_one(\n  {\"movieId\": movie_id},\n  {\"_id\": 0, \"ratingDistribution\": 1, \n   \"avgRating\": 1, \"ratingCount\": 1}\n)\n# Returns 10-bin histogram: 0.5 to 5.0 stars",
      bullets: (
        "Stores exact vote counts across all 10 star tiers (0.5 to 5.0).",
        "Pre-computed from 25M reviews during ETL batch processing.",
        "Dynamically shifts in real-time when a logged-in user submits a rating.",
        "Visualization: High-DPI bar chart histogram with vote tooltips."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_8_0_Im12.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 12: Question (b) — Top 10 Movies by Average Rating
// ==============================================================================
#card(title: "Question (b) — Overall & Year-wise Top 10 Movies", category: "ANALYTICS SCENARIO: QUESTION (B)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "PyMongo Query Implementation",
      "query = {\"ratingCount\": {\"$gte\": 500}}\nif year:\n    query = {\"year\": year, \"ratingCount\": {\"$gte\": 20}}\n\nresults = db.movies.find(query).sort([\n    (\"avgRating\", -1), (\"ratingCount\", -1)\n]).limit(10)",
      bullets: (
        "Minimum review threshold prevents single 5-star review outliers.",
        "Dynamic release year filter dropdown on dashboard.",
        "Fast execution via compound index: (ratingCount, avgRating).",
        "Visualization: Horizontal ranked bar chart with mean scores."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_9_0_Im13.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 13: Question (c) — Most Popular Tags for Each Genre
// ==============================================================================
#card(title: "Question (c) — Most Popular Tags Given for Each Genre", category: "ANALYTICS SCENARIO: QUESTION (C)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "PyMongo Query Implementation",
      "results = list(\n    db.genre_tags.find(\n        {},\n        {\"_id\": 0, \"genre\": 1, \"topTag\": 1, \n         \"count\": 1, \"topTags\": 1}\n    ).sort(\"genre\", 1)\n)",
      bullets: (
        "Computed during ETL by exploding movie genres and cross-joining 1.09M tags.",
        "Returns top 5 popular tags per genre with exact application counts.",
        "Stored in dedicated genre_tags collection with unique genre index.",
        "Visualization: Table with rank #1 tag highlighted in purple with star badge."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_10_0_Im14.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 14: Question (e) — Distribution of Total Ratings for Movies
// ==============================================================================
#card(title: "Question (e) — Distribution of Total Ratings for Movies", category: "ANALYTICS SCENARIO: QUESTION (E)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "MongoDB Aggregation Pipeline",
      "pipeline = [\n  {\"\$match\": {\"ratingCount\": {\"$gt\": 0}}},\n  {\"\$bucket\": {\n      \"groupBy\": \"$ratingCount\",\n      \"boundaries\": [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000],\n      \"default\": \"50000+\",\n      \"output\": {\"count\": {\"$sum\": 1}}\n  }}\n]",
      bullets: (
        "Groups all 62,423 titles into popularity brackets (1-9, 10-49, ..., 50,000+).",
        "Uses MongoDB \$bucket aggregation operator for logarithmic binning.",
        "Reveals long-tail distribution: few blockbusters, many niche movies.",
        "Visualization: Categorical bar chart showing catalog popularity curve."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_11_0_Im15.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 15: Question (f) — Genre with Highest Releases in a Selected Year
// ==============================================================================
#card(title: "Question (f) — Genre with Highest Releases by Year", category: "ANALYTICS SCENARIO: QUESTION (F)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "MongoDB Aggregation Pipeline",
      "pipeline = [\n  {\"\$match\": {\"year\": year}},\n  {\"\$unwind\": \"$genres\"},\n  {\"\$group\": {\"_id\": \"$genres\", \"count\": {\"$sum\": 1}}},\n  {\"\$sort\": {\"count\": -1}},\n  {\"$project\": {\"_id\": 0, \"genre\": \"$_id\", \"count\": 1}}\n]",
      bullets: (
        "Dynamic filter selects any release year (e.g. landmark year 1995).",
        "Unrolls genres array (\$unwind) and aggregates movie count per genre.",
        "First item in sorted array identifies the dominant genre of that year.",
        "Visualization: Sorted horizontal bar chart with peak genre highlighted."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_12_0_Im16.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 16: Question (g) — Genre-wise Movie Coverage
// ==============================================================================
#card(title: "Question (g) — Genre-wise Movie Coverage", category: "ANALYTICS SCENARIO: QUESTION (G)")[
  #grid(
    columns: (1.1fr, 1fr),
    gutter: 16pt,
    codebox(
      "MongoDB Aggregation Pipeline",
      "pipeline = [\n  {\"\$unwind\": \"$genres\"},\n  {\"\$group\": {\"_id\": \"$genres\", \"count\": {\"$sum\": 1}}},\n  {\"\$sort\": {\"count\": -1}},\n  {\"$project\": {\"_id\": 0, \"genre\": \"$_id\", \"count\": 1}}\n]",
      bullets: (
        "Calculates total catalogue share for every cinematic genre.",
        "A movie with multiple genres contributes proportionally to each.",
        "Indexed on genres field for rapid pipeline aggregation.",
        "Visualization: Multi-colored interactive doughnut chart with percentage legends."
      )
    ),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 8pt, [
      #image("screenshots/extracted/page_13_0_Im18.png", width: 100%)
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 17: Regulation 4 — Real-Time User Rating Modification
// ==============================================================================
#card(title: "Regulation 4: Real-Time User Rating Modification", category: "User Interaction & Write Engine")[
  #v(4pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#00e5a3"), weight: "bold", size: 12pt)[1. Client Rating Submission]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[User selects 0.5 to 5.0 stars on dashboard. Browser sends POST /api/ratings/submit with movieId and rating. Guarded by `@login_required`.]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#00e5a3"), weight: "bold", size: 12pt)[2. User Rating Upsert]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[Stores individual vote in ratings collection {movieId, username, rating, timestamp} using upsert=True.]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#00e5a3"), weight: "bold", size: 12pt)[3. Atomic Recalculation in MongoDB]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[Atomically updates movie document: recalculates mean avgRating, increments ratingCount, and shifts 10-bin histogram distribution.]
  ])
  #v(8pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 12pt, width: 100%, [
    #text(fill: rgb("#00e5a3"), weight: "bold", size: 12pt)[4. Real-time DOM Animation]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[Browser dynamically updates rating banner, vote count, and shifts Question (d) histogram bar without full page reload.]
  ])
]

#pagebreak()

// ==============================================================================
// SLIDE 18: Performance Benchmarks & Conclusion
// ==============================================================================
#card(title: "Performance Benchmarks & Engineering Summary", category: "Conclusion")[
  #grid(
    columns: (1fr, 1fr),
    gutter: 14pt,
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 14pt, [
      #text(fill: rgb("#00e5a3"), weight: "bold", size: 13pt)[⚡ Sub-5ms Query Latency] \       #text(fill: rgb("#8c96aa"), size: 10pt)[Pre-aggregated document structure eliminates multi-million-row SQL table scans. Complex questions (a-g) resolve in 2 to 5 milliseconds.]
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 14pt, [
      #text(fill: rgb("#00c0f0"), weight: "bold", size: 13pt)[🎬 62,423 Movies Loaded] \       #text(fill: rgb("#8c96aa"), size: 10pt)[Comprehensive data normalization and title regex cleaning ensures clean search and filtering across the complete historical catalog.]
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 14pt, [
      #text(fill: rgb("#7c5cff"), weight: "bold", size: 13pt)[📊 25 Million Ratings Aggregated] \       #text(fill: rgb("#8c96aa"), size: 10pt)[Chunked ETL pipeline processed 25M reviews in 5M batches without memory overflow, seeding complete histograms.]
    ]),
    rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 14pt, [
      #text(fill: rgb("#ffb72b"), weight: "bold", size: 13pt)[🔒 Strict Dual-Role Security] \       #text(fill: rgb("#8c96aa"), size: 10pt)[Full separation of privileges with session-based authentication, PBKDF2 hashing, and administrative audit logging.]
    ])
  )
]

#pagebreak()

// ==============================================================================
// SLIDE 19: References & Acknowledgements
// ==============================================================================
#card(title: "Project References & Academic Acknowledgements", category: "References")[
  #v(6pt)
  #rect(fill: rgb("#161b28"), stroke: 1pt + rgb("#2d374e"), radius: 8pt, inset: 16pt, width: 100%, [
    #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[▶ GroupLens Research — MovieLens 25M Dataset]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[https://grouplens.org/datasets/movielens/25m/ (Official benchmark dataset released December 2019).] \     #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[▶ F. Maxwell Harper and Joseph A. Konstan]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4, 2015.] \     #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[▶ DS5003 Data Engineering Lab Handout]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[Dr. Koninika Pal, Indian Institute of Technology Palakkad (Hand out 15.10.2026).] \     #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[▶ MongoDB Documentation & Aggregation Framework]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[Aggregation Pipeline Operators: \$bucket, \$unwind, \$group, and Compound Indexing best practices.] \     #text(fill: rgb("#00c0f0"), weight: "bold", size: 11pt)[▶ Flask & Chart.js Open-Source Frameworks]     #text(fill: rgb("#8c96aa"), size: 9.5pt)[Production WSGI application serving RESTful JSON endpoints and responsive HTML5 canvas rendering.]
  ])
]
