import sys

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError:
    print()
    print("Required libraries are missing.")
    print("Install them by running this command:")
    print("pip install scikit-learn")
    print()
    sys.exit()


def print_section(title):
    print()
    print("=" * 75)
    print(title)
    print("=" * 75)


def build_role_dataset():
    return [
        {
            "role": "Data Scientist",
            "category": "Data and AI",
            "description": "Analyzes data, builds predictive models, creates insights, and uses statistics and machine learning.",
            "skills": "python statistics machine learning data analysis pandas numpy visualization sql regression classification probability matplotlib seaborn jupyter"
        },
        {
            "role": "Machine Learning Engineer",
            "category": "Artificial Intelligence",
            "description": "Builds, trains, evaluates, and deploys machine learning models for real-world applications.",
            "skills": "python machine learning deep learning neural networks tensorflow pytorch scikit learn model training deployment mlops data preprocessing algorithms"
        },
        {
            "role": "AI Engineer",
            "category": "Artificial Intelligence",
            "description": "Builds AI-powered applications using machine learning, NLP, recommendation systems, and model integration.",
            "skills": "python artificial intelligence machine learning nlp recommendation systems transformers llm prompt engineering vector embeddings api automation"
        },
        {
            "role": "Backend Developer",
            "category": "Software Development",
            "description": "Builds server-side applications, APIs, databases, authentication systems, and application logic.",
            "skills": "python java nodejs django flask fastapi sql databases api backend authentication server logic docker git postgresql mongodb"
        },
        {
            "role": "Frontend Developer",
            "category": "Web Development",
            "description": "Builds user interfaces and interactive websites using modern frontend technologies.",
            "skills": "html css javascript react frontend ui ux responsive design typescript web development bootstrap tailwind nextjs"
        },
        {
            "role": "Full Stack Developer",
            "category": "Web Development",
            "description": "Works on both frontend and backend development to build complete web applications.",
            "skills": "html css javascript react nodejs python backend frontend databases api full stack django flask mongodb sql git deployment"
        },
        {
            "role": "DevOps Engineer",
            "category": "Cloud and Infrastructure",
            "description": "Manages deployment pipelines, cloud infrastructure, containers, automation, and system reliability.",
            "skills": "linux docker kubernetes aws cloud ci cd automation devops pipelines git github actions monitoring terraform bash networking"
        },
        {
            "role": "Cloud Engineer",
            "category": "Cloud and Infrastructure",
            "description": "Designs and manages cloud-based systems, services, storage, networking, and deployments.",
            "skills": "aws azure google cloud linux networking docker kubernetes serverless storage cloud security terraform deployment scalability"
        },
        {
            "role": "Cybersecurity Analyst",
            "category": "Security",
            "description": "Protects systems by identifying threats, monitoring networks, analyzing vulnerabilities, and improving security.",
            "skills": "cybersecurity network security ethical hacking linux penetration testing firewalls cryptography risk analysis vulnerability scanning security monitoring"
        },
        {
            "role": "Mobile App Developer",
            "category": "App Development",
            "description": "Builds mobile applications for Android and iOS using native or cross-platform technologies.",
            "skills": "android kotlin java flutter dart react native mobile app development firebase ui api ios swift"
        },
        {
            "role": "Database Administrator",
            "category": "Data Management",
            "description": "Manages databases, optimizes queries, protects data, and ensures reliable database performance.",
            "skills": "sql database postgresql mysql mongodb oracle data modeling query optimization backup recovery indexing transactions"
        },
        {
            "role": "UI UX Designer",
            "category": "Design",
            "description": "Designs user-friendly digital experiences, wireframes, prototypes, and visual interfaces.",
            "skills": "ui ux design figma wireframes prototyping user research usability accessibility visual design interaction design product design"
        },
        {
            "role": "Software Engineer",
            "category": "Software Development",
            "description": "Builds reliable software using programming, problem solving, data structures, algorithms, and engineering practices.",
            "skills": "programming python java c++ data structures algorithms software engineering object oriented programming git testing debugging problem solving"
        },
        {
            "role": "NLP Engineer",
            "category": "Artificial Intelligence",
            "description": "Builds language-based AI systems such as chatbots, text classifiers, summarizers, and search systems.",
            "skills": "python nlp natural language processing transformers llm text classification tokenization embeddings sentiment analysis chatbots huggingface"
        },
        {
            "role": "Computer Vision Engineer",
            "category": "Artificial Intelligence",
            "description": "Builds systems that process images and videos using deep learning and vision algorithms.",
            "skills": "python computer vision opencv image processing deep learning cnn pytorch tensorflow object detection segmentation classification"
        }
    ]


def get_user_preferences():
    print_section("User Preference Input")
    print("Enter at least three skills or interests.")
    print("Example: Python, Cloud Computing, Automation")
    print()

    while True:
        raw_input_text = input("Enter your skills or interests separated by commas: ").strip()

        preferences = []
        for item in raw_input_text.split(","):
            cleaned_item = item.strip().lower()
            if cleaned_item != "":
                preferences.append(cleaned_item)

        if len(preferences) >= 3:
            return preferences

        print()
        print("Please enter at least three valid skills or interests.")
        print()


def build_user_profile(preferences):
    return " ".join(preferences)


def create_tfidf_vectors(user_profile, role_dataset):
    role_documents = []

    for role in role_dataset:
        combined_text = role["role"] + " " + role["category"] + " " + role["description"] + " " + role["skills"]
        role_documents.append(combined_text)

    documents = [user_profile] + role_documents

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    user_vector = tfidf_matrix[0]
    role_vectors = tfidf_matrix[1:]

    return vectorizer, user_vector, role_vectors


def calculate_similarity_scores(user_vector, role_vectors, role_dataset):
    similarity_values = cosine_similarity(user_vector, role_vectors).flatten()

    scored_roles = []

    for index, score in enumerate(similarity_values):
        scored_roles.append({
            "rank": 0,
            "role": role_dataset[index]["role"],
            "category": role_dataset[index]["category"],
            "description": role_dataset[index]["description"],
            "skills": role_dataset[index]["skills"],
            "score": score
        })

    return scored_roles


def sort_and_filter_recommendations(scored_roles, top_n):
    sorted_roles = sorted(scored_roles, key=lambda item: item["score"], reverse=True)
    top_roles = sorted_roles[:top_n]

    for index, role in enumerate(top_roles, start=1):
        role["rank"] = index

    return top_roles


def show_dataset_summary(role_dataset):
    print_section("Recommendation Dataset Overview")
    print("Total career roles available:", len(role_dataset))
    print()

    categories = {}

    for role in role_dataset:
        category = role["category"]
        if category not in categories:
            categories[category] = 0
        categories[category] += 1

    print("Role categories:")
    for category, count in categories.items():
        print(category + ":", count)


def show_user_profile(preferences):
    print_section("User Profile")
    print("User selected interests:")
    for index, preference in enumerate(preferences, start=1):
        print(str(index) + ".", preference)

    print()
    print("User profile text:")
    print(build_user_profile(preferences))


def show_recommendations(recommendations):
    print_section("Top Career Recommendations")

    for recommendation in recommendations:
        percentage_score = recommendation["score"] * 100

        print("Rank:", recommendation["rank"])
        print("Career Path:", recommendation["role"])
        print("Category:", recommendation["category"])
        print("Similarity Score:", str(round(percentage_score, 2)) + "%")
        print("Why this matches:", recommendation["description"])
        print()


def show_all_scores(scored_roles):
    print_section("All Role Similarity Scores")

    sorted_roles = sorted(scored_roles, key=lambda item: item["score"], reverse=True)

    for role in sorted_roles:
        print(role["role"] + ":", str(round(role["score"] * 100, 2)) + "%")


def show_skill_suggestions():
    print_section("Example Skills You Can Try")
    examples = [
        "Python, Machine Learning, Data Analysis",
        "HTML, CSS, JavaScript",
        "AWS, Docker, Kubernetes",
        "Linux, Cybersecurity, Networking",
        "Figma, UI Design, User Research",
        "NLP, Transformers, Chatbots",
        "Android, Kotlin, Firebase"
    ]

    for example in examples:
        print("-", example)


def run_recommender():
    print_section("DecodeLabs Project 3")
    print("AI Recommendation Logic")
    print("Project: Tech Stack Recommender")
    print("Method: Content-Based Filtering with TF-IDF and Cosine Similarity")

    role_dataset = build_role_dataset()

    show_dataset_summary(role_dataset)
    show_skill_suggestions()

    preferences = get_user_preferences()
    user_profile = build_user_profile(preferences)

    show_user_profile(preferences)

    vectorizer, user_vector, role_vectors = create_tfidf_vectors(user_profile, role_dataset)

    print_section("Vector Mapping")
    print("User preferences and career roles were converted into TF-IDF vectors.")
    print("Total vocabulary size:", len(vectorizer.get_feature_names_out()))

    scored_roles = calculate_similarity_scores(user_vector, role_vectors, role_dataset)
    recommendations = sort_and_filter_recommendations(scored_roles, 3)

    show_recommendations(recommendations)
    show_all_scores(scored_roles)

    print_section("Project Completed")
    print("The recommendation system successfully matched user interests with career paths.")


if __name__ == "__main__":
    run_recommender()