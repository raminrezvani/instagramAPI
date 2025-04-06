prompt="""
fill this template json based on video. only give json template .
 one item according to its description.  for each key of this json, select one item only and also for each subkey 
 select one item and etc. not select sibling keys together.  the result must be a json.

 {
 "Topics":{
      "Lifestyle & Personal": {
        "Daily Vlogs": "Recording everyday moments and personal activities",
        "Minimalism & Simple Living": "Promoting simple lifestyle and reducing material dependencies",
        "Modern Urban Living": "Apartment living and life in metropolitan areas",
        "Digital Lifestyle": "Balance between technology and real life, digital wellbeing",
        "Rural Living & Self-Sufficiency": "Return to nature and independent living away from cities",
        "Daily Habits": "Introducing effective habits and personal experiences",
        "Immigration & Living Abroad": "Experiences of living in different countries",
        "Remote Work & Digital Nomad Lifestyle": "Flexible work-life arrangements",
        "Home Organization": "Organizing, cleaning, and arranging personal spaces",
        "Mental Self-Care": "Rest, stress management, and mental wellbeing"
      },
      "Food & Cooking": {
        "Home Cooking": "Simple recipes that can be prepared at home",
        "Baking & Desserts": "How to make cakes, pastries, and homemade desserts",
        "Plant-Based & Vegan Food": "Cooking without animal products",
        "International Cuisine": "Foods from different cultures around the world",
        "Traditional & Local Food": "Authentic regional dishes and old recipes",
        "Fast Food & Street Food": "Quick meals and street cuisine",
        "Beverages & Mixology": "How to prepare various drinks, coffee shop and bar culture",
        "Specialized Diet Plans": "Keto, paleo, low-carb, and other diet regimens",
        "Food Photography & Presentation": "Arrangement and decoration of food for professional photography",
        "Restaurant & Café Reviews": "Introduction and reviews of eateries"
      },
      "Travel, Adventure & Nature": {
        "City Guides": "Introduction to attractions and points of interest in cities",
        "Budget Travel & Backpacking": "Economical travel strategies and backpacking",
        "Road Trips & Highways": "Traveling by personal vehicles on intercity roads",
        "Hiking & Mountaineering": "Traversing natural paths and climbing mountains",
        "Camping & Glamping": "Staying in nature with tents or luxury accommodations",
        "Travel Photography": "Capturing travel moments with professional photography techniques",
        "Cultural Tourism": "Exploring customs, foods, and culture of destinations",
        "Ecotourism & Sustainable Travel": "Environmentally compatible trips and local community support",
        "Adventure Travels": "Rafting, paragliding, diving, and thrilling activities",
        "Luxury Travel & Hotel Reviews": "Experiences in upscale hotels and amenities"
      },
      "Fashion & Beauty": {
        "Daily Style": "Outfit combinations for different situations",
        "Sustainable Fashion": "Environmentally friendly clothes and conscious consumption",
        "Skincare": "Skin routines, care products, and treatments",
        "Everyday & Professional Makeup": "Makeup techniques for various occasions",
        "Hair Care": "Styling, coloring, and maintenance of different hairstyles",
        "Nail Design & Manicure": "Techniques and designs for nails",
        "Seasonal Fashion": "Seasonal trends and fashion changes throughout the year",
        "Accessories & Jewelry": "Style complements and jewelry pieces",
        "Fragrance & Perfume": "Introduction to different scents and selection guides",
        "Street Fashion & Street Style": "Casual styles and youth trends"
      },
      "Fitness & Sports": {
        "Strength Training": "Bodybuilding, weightlifting, and muscle strengthening",
        "Cardio Workouts": "Running, cycling, and endurance activities",
        "Team Sports": "Football, basketball, volleyball, and other team activities",
        "Yoga & Pilates": "Stretching exercises, flexibility, and core strengthening",
        "Martial Arts": "Karate, taekwondo, boxing, and other combat sports",
        "Sports Nutrition": "Diet plans for athletes and supplements",
        "Home Workouts": "Exercise without needing gym equipment",
        "Specialized Training Programs": "Workout design for specific goals",
        "Competitions & Sports Events": "Coverage of professional competitions",
        "Recovery & Performance Improvement": "Recovery techniques and injury prevention"
      },
      "Technology & Knowledge": {
        "Smart Gadgets": "Reviews of mobile phones, watches, and other wearable devices",
        "Computers & Laptops": "Hardware introductions, model reviews, and buying guides",
        "Artificial Intelligence & Machine Learning": "AI developments, applications, and impacts",
        "Internet of Things (IoT)": "Smart homes and connected devices",
        "Emerging Technologies": "Virtual reality, 3D printing, and future technologies",
        "Apps & Software": "Introduction to the most useful programs and their reviews",
        "Scientific News": "Latest research findings in various fields",
        "Space & Cosmology": "Space exploration, astronomy, and star science",
        "Cybersecurity": "Digital security, data protection, and privacy",
        "Life Sciences & Medicine": "Advances in health and biotechnology"
      },
      "Business & Finance": {
        "Entrepreneurship & Startups": "Starting businesses and founder experiences",
        "Investment": "Stocks, real estate, cryptocurrencies, and other opportunities",
        "Digital Marketing": "Online marketing strategies and advertising",
        "Freelancing & Independent Work": "Freelance work guides and income-earning consultancy",
        "Personal Branding": "Building personal brands and increasing professional credibility",
        "Personal Financial Management": "Budgeting, saving, and financial planning",
        "Leadership & Management": "Team leadership skills and organizational management",
        "E-Commerce": "Setting up online stores and sales strategies",
        "Business Development": "Growth strategies, negotiation, and networking",
        "Micro & Macro Economics": "Analysis of economic trends and their impact on business"
      },
      "Education & Self-Improvement": {
        "Foreign Languages": "Teaching different languages and learning techniques",
        "Soft Skills": "Effective communication, teamwork, and problem-solving",
        "Programming & Information Technology": "Coding education and digital skills",
        "Art & Crafts Learning": "Learning artistic techniques and creative skills",
        "University Education": "Entrance exams, tests, and academic guidance",
        "Time Management & Productivity": "Methods to increase efficiency and organization",
        "Practical Life Skills": "Teaching everyday and applied skills",
        "Book Reading & Effective Study": "Resource introductions and study techniques",
        "Critical & Creative Thinking": "Developing mental skills and problem-solving",
        "Public Speaking & Presentation": "Speaking skills and confidence in groups"
      },
      "Art, Design & Photography": {
        "Visual Arts": "Painting, drawing, and artistic techniques",
        "Portrait Photography": "Capturing faces, photographing individuals and groups",
        "Landscape Photography": "Nature, city, and wide landscapes",
        "Graphic & Digital Design": "Photoshop, Illustrator, and design tools",
        "Handcrafts & Traditional Arts": "Pottery, weaving, and traditional arts",
        "Calligraphy & Typography": "The art of writing and font design",
        "Sculpture & Three-Dimensional Arts": "Working with various materials and creating 3D works",
        "Street Art & Graffiti": "Art in public and urban spaces",
        "Videography & Cinematography": "Filming and visual techniques",
        "Photo & Video Editing": "Post-production and professional alterations"
      },
      "Entertainment & Media": {
        "Film & TV Series": "Introduction, critique, and analysis of cinematic and television works",
        "Music": "Introduction to albums, artists, and music styles",
        "Video Games": "Game introductions, gameplay, and gaming industry news",
        "Books & Popular Literature": "Introduction and critique of literary works for the general public",
        "Podcasts & Audio Content": "Introduction to audio programs and content production",
        "Humor & Memes": "Entertaining content, jokes, and funny trends",
        "Celebrities & Famous People": "News and lives of well-known individuals",
        "Group Entertainment": "Board games, group games, and social gatherings",
        "Festivals & Cultural Events": "Introduction to festivals and gatherings",
        "Streaming & Live Content Production": "Live broadcasting and interactive content"
      },
      "Culture, Society & Politics": {
        "Cultural & Historical Heritage": "Historical monuments, museums, and cultural identity",
        "Political Analysis": "Analysis of political events, elections, and governance",
        "Applied Sociology": "Analysis of social phenomena and cultural changes",
        "Minorities & Cultural Diversity": "Issues related to different social groups",
        "Citizenship Issues": "Civil rights and responsibilities in society",
        "Crises & Social Challenges": "Analysis of acute social issues",
        "Regional & Global News": "Important events at the international level",
        "National Ceremonies & Celebrations": "Cultural occasions and traditions",
        "Citizen Journalism": "Reporting from ordinary people's perspectives",
        "Social Movements": "Activism and collective movements"
      },
      "Family & Relationships": {
        "Child Rearing": "Methods for raising children and adolescents",
        "Family Psychology": "Dynamics of family relationships",
        "Marital Relationships": "Strengthening communication and resolving conflicts between spouses",
        "Romantic Relationships & Partner Finding": "Recognition, selection, and interaction with romantic partners",
        "Interpersonal Communication Skills": "Effective dialogue, empathy, and mutual understanding",
        "Single Parenting": "Challenges and solutions for single-parent child-rearing",
        "Young Parents": "Guidance for new fathers and mothers",
        "Making & Maintaining Friendships": "Building lasting social relationships",
        "Elderly Care & Intergenerational Relationships": "Interaction with elderly parents and generational connections",
        "Conflict Resolution & Mediation": "Solutions for resolving disputes in various relationships"
      },
      "Spirituality & Religion": {
        "Religious Teachings": "Interpretation of sacred texts and belief concepts",
        "Rituals & Ceremonies": "Guide to performing religious rites and worship",
        "Applied Ethics & Spirituality": "Ethical principles in everyday life",
        "Philosophical Reflections": "Questions and thoughts about the meaning of life",
        "Meditation & Self-Awareness": "Spiritual practices for inner peace",
        "Religious Festivals & Rituals": "Introduction and celebration of religious occasions",
        "Interfaith Dialogue": "Coexistence and mutual understanding between different religions",
        "Modern Spirituality": "Spiritual approaches suitable for today's world",
        "Mysticism & Sufism": "Teachings and mystical traditions",
        "Sacred Places": "Introduction to pilgrimage and religious sites"
      },
      "Architecture, Real Estate & Automotive": {
        "Home Interior Design": "Decoration, arrangement, and renovation of interior spaces",
        "Building Architecture": "Styles and design features of various buildings",
        "Real Estate Buying & Selling": "Housing transaction guides and investment",
        "Renting & Tenancy": "Rights and responsibilities of landlords and tenants",
        "Passenger Cars": "Introduction, review, and comparison of new cars",
        "Motorcycles & Two-Wheeled Vehicles": "Review and introduction to various motorcycles",
        "Green Space & Garden Design": "Gardening and exterior design",
        "Classic & Collectible Cars": "Vintage and valuable automobiles",
        "Furniture & Product Design": "Introduction and review of decoration components",
        "Electric Vehicles & Future Transportation": "New technologies in the automotive industry"
      },
      "Social Activities & Environment": {
        "Volunteering & Charity Work": "Ways to help and participate in charitable activities",
        "Environmental Protection": "Conservation actions and reducing carbon footprint",
        "Animal Rights": "Support for animal species and animal rescue",
        "Sustainable Living & Low Consumption": "Ways to reduce consumption and waste",
        "Social Campaigns": "Collective movements for social change",
        "Education & Social Awareness": "Information about social issues",
        "Social Impact": "Individuals and organizations effective in positive changes",
        "Empowerment of Vulnerable Groups": "Support for disadvantaged groups",
        "Vegetarianism & Sustainable Agriculture Support": "Diet patterns compatible with the environment",
        "Environmental Crises": "Climate change, pollution, and solutions"
      }
    },
  "Language":{
          Persian,
        English,
        Arabic (العربية),
        Spanish (Español),
        Turkish (Türkçe),
        French (Français),
        Hindi (हिन्दी),
        Portuguese (Português),
        Russian (Русский),
        German (Deutsch),
        Chinese (Simplified) (中文简体),
        Japanese (日本語),
        Korean (한국어),
        Italian (Italiano),
        Finnish (Suomi) ,
        Swedish (Svenska), 
        Danish (Dansk) ,
  },
  "Subcategory of Feels and Emotion":{
          Happy 
        Sad 
        Excited 
        Calm 
        Inspired 
        Angry
        Nostalgic
        Relaxed
        Curious
        Motivated
        Peaceful
        Fear
        Hopeful
        Tense
        Neutral
  },
  "Age Range ":{
        Under 13
        13-17 
        18-24 
        25-34 
        35-44 
        45-54 
        55+ 
        All Ages 
  },
  
  "Content Verification":{
          1. Likes  
        2. Comments
        3. Shares 
        4. Views 
        5. Engagement Rate
        6. Follower Count 
        7. Verified Badge 
        8. High Likes  
        9. High Comments  
        10. High Shares
        11. Low Engagement
        12. Recent Activity 
        13. Post Frequency  
        14. Audiesirpostchirr@gmail.comnce Reactions
        15. Trending Status  

  },
  "Sensitivity":{
          Neutral 
        Mild 
        Moderate 
        Unrestricted

  },
  "Gender":{Male 
        Female 
        Other 
    },
    "Audience":{
        1. Education/Students
        2. Fashion & Beauty Enthusiasts
        3. Fitness & Health Focused
        4. Foodies & Lifestyle
        5. Travelers & Adventurers
        6. Creators & Artists
        7. Business & Professionals
        8. Entertainment Fans
    },
    
    
    
    "Fear and Phobias":{
        1. Tokophobia (Pregnancy/Childbirth Fear): Fear of posts about labor pain, birth complications, or cesarean sections.
        2. Obstetric Phobia (Medical Fear): Anxiety from hospital photos, doctor rants, or procedure videos.
        3. Maternity Fear (Motherhood Anxiety): Dread from parenting fails, “mom guilt” posts, or overwhelming baby care tips.
        4. Fear of Miscarriage (Antepartum Anxiety): Panic from stats on pregnancy loss or sad miscarriage stories.
        5. Fear of Postpartum Depression: Worry from PPD confessions or mental health collapse posts.
        6. Fear of Neonatal Disorders: Anxiety from baby health scare stories or disability discussions.
        7. Cacophobia (Fear of Ugly/Disgusting): Disgust from childbirth gore, stretch mark close-ups, or medical waste images.
        8. Sociophobia (Social Judgment Fear): Stress from pregnancy shaming, body image critiques, or mommy wars.
        9. Anthophobia (Flower Fear): Unease from floral posts linked to fertility/loss (niche but possible on social media).
        10. Thanatophobia (Fear of Death): Dread from obituaries, sudden death news, or fatal accident clips.
        11. Trypophobia (Fear of Holes): Discomfort from oddly patterned images (e.g., lotus pod edits) that go viral.
        12. Arachnophobia (Spider Fear): Panic from spider photos/videos shared for shock value.
        13. Claustrophobia (Confined Space Fear): Anxiety from tight space videos (e.g., cave explorations).
        14. Coulrophobia (Clown Fear): Distress from creepy clown memes or circus posts.
        15. Nomophobia (No Mobile Phone Fear): Stress from posts about tech failures or being disconnected.
        16. FOMO-Phobia (Fear of Missing Out): Anxiety from seeing others’ perfect lives or exclusive events.
        17. Cyberphobia (Tech Fear): Unease from AI takeover theories or hacking horror stories.
        18. Misophonia (Sound Sensitivity): Irritation from loud chewing videos, ASMR gone wrong, or sudden screams.

    
    },
    
    "Digital Mental Health":{
        "Harmful behaviors":{
            "Suicide",
            "Self-harm",
            "Severe Depression",
            " Eating Disorders",
            "Chronic Anxiety",
            "Addiction Promotion",
            
            "Mental Health Misinformation",
            "Feels and Emotion":{
                "Deep Hopelessness",
                "Extreme Fear",
                "Emotional Distress",
                "Panic"
            },
            "Sensitivity ":{
                "High Sensitivity (Mental Health)",
                "Psychological Triggers",
            }
            " Fear and Phobias":{
                "Severe Phobia Triggers",
                "Trauma Triggers"
            
            },
            "Age Range":{
                " Child Mental Health Protection",
                " Adolescent Vulnerability"
                }            
        }
    }
  
}

"""