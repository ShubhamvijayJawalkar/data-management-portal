import duckdb
import random
import string

DB_PATH = r"C:\Users\CW230503\Desktop\flask_app\portal_master.db"

FIRST_NAMES = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Christopher", "Karen", "Charles", "Lisa", "Daniel", "Nancy",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Paul", "Emily", "Andrew", "Donna", "Joshua", "Michelle",
    "Kenneth", "Carol", "Kevin", "Amanda", "Brian", "Dorothy", "George", "Melissa",
    "Timothy", "Deborah", "Ronald", "Stephanie", "Edward", "Rebecca", "Jason", "Sharon",
    "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy",
    "Nicholas", "Angela", "Eric", "Shirley", "Jonathan", "Anna", "Stephen", "Brenda",
    "Larry", "Pamela", "Justin", "Emma", "Scott", "Nicole", "Brandon", "Helen",
    "Benjamin", "Samantha", "Samuel", "Katherine", "Raymond", "Christine", "Gregory", "Debra",
    "Frank", "Rachel", "Alexander", "Carolyn", "Patrick", "Janet", "Jack", "Catherine",
    "Dennis", "Maria", "Jerry", "Heather", "Tyler", "Diana", "Aaron", "Julie",
    "Jose", "Joyce", "Nathan", "Victoria", "Henry", "Kelly", "Douglas", "Lauren",
    "Aisha", "Kwame", "Mei", "Raj", "Chen", "Wei", "Yuki", "Satoshi",
    "Priya", "Arjun", "Fatima", "Omar", "Ahmed", "Hassan", "Ling", "Xiu",
    "Olga", "Dmitri", "Mohammed", "Ali", "Sofia", "Elena", "Carlos", "Miguel",
    "Aiko", "Takeshi", "Nadia", "Vladimir", "Sanjay", "Deepak", "Ananya", "Ravi",
    "Liam", "Noah", "Ethan", "Mason", "Logan", "Lucas", "Jackson", "Aiden",
    "Oliver", "Elijah", "Grayson", "Sebastian", "Carter", "Wyatt", "Jayden", "Gabriel",
    "Julian", "Mateo", "Adrian", "Miles", "Leo", "Ezra", "Luca", "Isaiah",
    "Charlotte", "Amelia", "Sophia", "Mia", "Isabella", "Evelyn", "Harper", "Luna",
    "Chloe", "Ella", "Avery", "Sofia", "Aria", "Scarlett", "Ellie", "Layla",
    "Nora", "Riley", "Zoey", "Hannah", "Lily", "Grace", "Zara", "Aurora",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
    "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
    "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
    "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Cruz",
    "Edwards", "Collins", "Reyes", "Choi", "Patel", "Singh", "Kumar", "Sharma",
    "Chen", "Wang", "Li", "Zhang", "Liu", "Tanaka", "Suzuki", "Yamamoto",
    "Watanabe", "Ito", "Kim", "Park", "Chung", "Chang", "Yang", "Wu",
    "Huang", "Zhou", "Gupta", "Das", "Shah", "Joshi", "Okafor", "Nwachukwu",
    "Osei", "Mensah", "Adebayo", "Olaniyan", "Johansson", "Andersson", "Nilsson", "Karlsson",
    "Karim", "Abdullah", "Hussein", "Rahman", "Khalid", "Benitez", "Castillo", "Ramos",
    "Ortiz", "Moreno", "Iglesias", "Navarro", "Mendoza", "Vargas", "Santiago", "Delgado",
    "Aguilar", "Kimura", "Sato", "Nakamura", "Kobayashi", "Yoshida", "Takahashi", "Hayashi",
    "Ivanov", "Petrov", "Volkov", "Sokolov", "Popov", "Lebedev", "Kuznetsov", "Novikov",
    "Khan", "Ahmad", "Chaudhry", "Iqbal", "Khalil", "Saleh", "Youssef", "Hassan",
]

SALUTATIONS = ["Mr.", "Ms.", "Mrs.", "Dr.", ""]

JOB_TITLES = [
    "Software Engineer", "Senior Developer", "Project Manager", "Product Manager",
    "Data Analyst", "Data Scientist", "Marketing Manager", "Sales Director",
    "CEO", "CTO", "CFO", "COO", "VP of Engineering", "VP of Sales",
    "Business Analyst", "Consultant", "Account Executive", "Customer Success Manager",
    "HR Manager", "Operations Manager", "Financial Analyst", "UX Designer",
    "Solutions Architect", "DevOps Engineer", "QA Engineer", "Technical Lead",
    "Engineering Manager", "Product Owner", "Scrum Master", "IT Director",
    "Digital Marketing Specialist", "Content Strategist", "Brand Manager",
    "Supply Chain Manager", "Business Development Manager", "Research Scientist",
    "Machine Learning Engineer", "Full Stack Developer", "Frontend Developer",
    "Backend Developer", "Cloud Architect", "Security Engineer", "Database Administrator",
    "Network Engineer", "Systems Administrator", "Technical Writer", "Graphic Designer",
    "Art Director", "Creative Director", "Communications Manager", "PR Specialist",
    "Legal Counsel", "Compliance Officer", "Risk Analyst", "Investment Analyst",
    "Auditor", "Tax Consultant", "Management Consultant", "Strategy Manager",
]

COMPANIES = [
    "TechNova Solutions", "GlobalPeak Industries", "Quantum Dynamics", "Apex Innovations",
    "BrightPath Systems", "CoreVault Technologies", "DataForge Inc", "EliteSoft Corp",
    "FusionWorks Labs", "GreenLeaf Analytics", "Horizon Ventures", "IronClad Security",
    "Jade Mountain Consulting", "Kingsway Global", "Lighthouse Digital", "Meridian Group",
    "NorthStar Partners", "OakTree Solutions", "Pinnacle Strategies", "Questronix",
    "Redwood Tech", "Silverline Systems", "Titan Enterprises", "Unity Technologies",
    "Vertex Solutions", "WaveFront Digital", "Zenith Group", "AccelPoint Consulting",
    "BlueRiver Analytics", "Crestview Partners", "DawnBreak Tech", "Everest Systems",
    "FirstBridge Solutions", "GoldenGate Software", "HighPeak Ventures", "Infinity Labs",
    "Jupiter Innovations", "KeyStone Global", "Lakeside Tech", "Matrix Digital",
    "NexGen Solutions", "OmniTech Corp", "Pacific Rim Systems", "Quantum Leap Analytics",
    "Rising Tide Partners", "Skyline Technologies", "TrueNorth Solutions", "UltraViolet Labs",
    "Velocity Partners", "WestWind Digital", "Xenith Corp", "YellowStone Analytics",
    "ArcLight Systems", "Beacon Hill Technologies", "Crimson Dynamics", "DeepBlue Analytics",
    "EagleView Consulting", "Frontline Systems", "Gravity Solutions", "Helix Digital",
]

COUNTRIES = [
    "United States", "Canada", "United Kingdom", "Germany", "France",
    "India", "Japan", "Australia", "Brazil", "Singapore",
    "United Arab Emirates", "South Africa", "Mexico", "Italy", "Spain",
]

EMAIL_DOMAINS = [
    "gmail.com", "outlook.com", "yahoo.com", "hotmail.com", "icloud.com",
    "protonmail.com", "live.com", "mail.com", "company.com", "corp.net",
]

def random_email(first, last):
    domain = random.choice(EMAIL_DOMAINS)
    num = random.randint(1, 999)
    variants = [
        f"{first.lower()}.{last.lower()}@{domain}",
        f"{first.lower()}{last.lower()}@{domain}",
        f"{first[0].lower()}{last.lower()}@{domain}",
        f"{first.lower()}{num}@{domain}",
        f"{last.lower()}.{first.lower()}@{domain}",
    ]
    return random.choice(variants)


def main():
    conn = duckdb.connect(DB_PATH)
    inserted = 0
    try:
        for country in COUNTRIES:
            for _ in range(500):
                salutation = random.choice(SALUTATIONS)
                first = random.choice(FIRST_NAMES)
                last = random.choice(LAST_NAMES)
                email = random_email(first, last)
                job = random.choice(JOB_TITLES)
                company = random.choice(COMPANIES)

                conn.execute("""
                    INSERT INTO Leads ("Salutation", "First Name", "Last Name", "Email", "Job Titles", "Company Name", "Country")
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, [salutation, first, last, email, job, company, country])
                inserted += 1

        conn.commit()
        total = conn.execute("SELECT COUNT(*) FROM Leads").fetchone()[0]
        print(f"Inserted {inserted} leads successfully!")
        print(f"Total leads now: {total}")
        countries_list = conn.execute("""
            SELECT Country, COUNT(*) as cnt FROM Leads
            WHERE Country IS NOT NULL GROUP BY Country ORDER BY cnt DESC LIMIT 20
        """).fetchall()
        print("\nCountry breakdown:")
        for c, cnt in countries_list:
            print(f"  {c}: {cnt}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
