import requests
import random

BASE_URL = 'http://127.0.0.1:5000'  # Adjust based on your Flask app's URL

NAMES_LIST = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Krishna", "Sai", "Aryan", "Dhruv", 
    "Karthik", "Shreyas", "Nikhil", "Rohan", "Siddharth", "Yash", "Rudra", "Ishaan", 
    "Om", "Arjun", "Ananya", "Aditi", "Meera", "Pooja", "Priya", "Sana", "Riya", 
    "Naina", "Tara", "Aishwarya", "Diya", "Tanvi", "Isha", "Kavya", "Sneha", "Maya", 
    "Sanya", "Lakshmi", "Radhika", "Sakshi", "Neha", "Anjali", "Ashwin", "Raghav", 
    "Harsh", "Manish", "Pranav", "Saurabh", "Akash", "Bhavesh", "Kunal", "Aniket", 
    "Ajay", "Vikas", "Sanjay", "Chirag", "Gaurav", "Rajesh", "Amit", "Rahul", 
    "Suresh", "Pavan", "Varun", "Ravi", "Bharat", "Mohit", "Jay", "Mahesh", 
    "Vikram", "Tarun", "Sunil", "Kiran", "Ritu", "Swati", "Rashmi", "Geeta", 
    "Suman", "Shilpa", "Rekha", "Vidya", "Manisha", "Sunita", "Jaya", "Alka", 
    "Divya", "Bhavana", "Monika", "Komal", "Pallavi", "Seema", "Meenakshi", 
    "Sheetal", "Payal", "Sonali", "Rajiv", "Naveen", "Rakesh", "Mohan", "Balaji"
]

BLOG_TITLES = [
    "10 Tips to Boost Your Productivity at Work",
    "The Ultimate Guide to Mindfulness for Beginners",
    "How to Create a Successful Side Hustle",
    "Top 5 Coding Languages to Learn in 2024",
    "Exploring the World of Sustainable Fashion",
    "How to Build a Morning Routine for Success",
    "The Benefits of Yoga for Mental Health",
    "A Beginner’s Guide to Cryptocurrency",
    "How to Travel on a Budget: 20 Expert Tips",
    "The Science of Building Healthy Habits",
    "Mastering Time Management: Strategies That Work",
    "The Future of Artificial Intelligence in Healthcare",
    "How to Start a Profitable Blog in 2024",
    "Essential Tools for Remote Work Success",
    "Exploring the Benefits of a Plant-Based Diet",
    "The Psychology Behind Decision Making",
    "A Guide to Freelancing: How to Get Started",
    "How to Create an Effective Marketing Strategy",
    "The Art of Negotiation: Tips for Better Deals",
    "How to Stay Motivated When Working From Home",
    "The Importance of Sleep for Mental and Physical Health",
    "Top 10 Fitness Trends to Watch Out For",
    "How to Improve Your Focus and Concentration",
    "The Benefits of Learning a New Language",
    "How to Overcome Procrastination and Get Things Done",
    "The Power of Positive Thinking: A Complete Guide",
    "10 Easy Steps to Start Your Own Business",
    "How to Improve Your Leadership Skills",
    "The Role of Technology in Education Today",
    "How to Invest in Real Estate: A Beginner’s Guide",
    "Tips for Building a Strong Professional Network",
    "The Importance of Emotional Intelligence in the Workplace",
    "How to Create a Digital Marketing Plan",
    "10 Essential Life Skills You Need to Succeed",
    "The Impact of Social Media on Mental Health",
    "How to Plan a Solo Travel Adventure",
    "The Pros and Cons of Remote Work",
    "The Future of Virtual Reality in Entertainment",
    "How to Start a Career in Web Development",
    "A Complete Guide to Time Blocking for Productivity",
    "How to Build a Personal Brand Online",
    "The Benefits of Reading for Personal Growth",
    "How to Set and Achieve Your Long-Term Goals",
    "Top 5 Skills Every Entrepreneur Should Have",
    "How to Effectively Manage Stress in Daily Life",
    "A Beginner’s Guide to Stock Market Investing",
    "How to Stay Creative in a Fast-Paced World",
    "The Power of Networking: How to Build Valuable Connections",
    "How to Improve Your Public Speaking Skills",
    "The Importance of Financial Literacy for Young Adults",
    "How to Create a Social Media Content Calendar",
    "The Benefits of Volunteering for Personal Development",
    "How to Build a Strong Online Community",
    "A Guide to Self-Care for Busy Professionals",
    "How to Create a Minimalist Lifestyle",
    "The Role of Ethics in Modern Technology",
    "How to Improve Your Problem-Solving Skills",
    "The Benefits of Meditation for Stress Relief",
    "How to Achieve Work-Life Balance in a Hectic World",
    "The Evolution of E-Commerce: Trends and Innovations",
    "How to Create a Successful Online Course",
    "The Importance of Soft Skills in the Workplace",
    "How to Build Confidence and Overcome Self-Doubt",
    "The Future of Renewable Energy: What You Need to Know",
    "How to Master the Art of Delegation",
    "The Impact of Climate Change on Global Economies",
    "How to Write Engaging and Shareable Blog Posts",
    "The Science Behind Effective Goal Setting",
    "How to Handle Criticism Like a Pro",
    "Top 10 Books Every Entrepreneur Should Read",
    "The Benefits of Journaling for Personal Growth",
    "How to Start a Podcast: A Step-by-Step Guide",
    "The Future of Work: Trends Shaping the Job Market",
    "How to Develop a Growth Mindset for Success",
    "The Role of Innovation in Business Growth",
    "How to Create a Personal Development Plan",
    "The Importance of Diversity and Inclusion in the Workplace",
    "How to Make Money with Affiliate Marketing",
    "Top 5 Ways to Improve Your Mental Health",
    "The Art of Writing Compelling Product Descriptions",
    "How to Master the Gig Economy: Tips for Freelancers",
    "The Impact of 5G Technology on Businesses",
    "How to Use Data Analytics to Grow Your Business",
    "The Benefits of Taking Regular Breaks at Work",
    "How to Improve Your Customer Service Skills",
    "The Role of AI in Enhancing Customer Experience",
    "How to Start a Nonprofit Organization: A Step-by-Step Guide",
    "The Importance of Continuous Learning in Your Career",
    "How to Manage Your Finances as a Freelancer",
    "Top 5 Marketing Strategies for Small Businesses",
    "How to Create Engaging Video Content for Social Media",
    "The Benefits of Implementing a CRM System",
    "How to Build a Strong Email Marketing Campaign",
    "The Role of Blockchain in the Future of Finance",
    "How to Create a Sustainable Business Model",
    "Top 10 Creative Ways to Generate Passive Income",
    "How to Build Strong Relationships with Your Clients",
    "The Future of Remote Collaboration Tools",
    "How to Leverage Influencer Marketing for Your Business",
    "A Beginner’s Guide to Dropshipping in 2024",
    "How to Plan and Execute a Successful Event",
    "The Power of Gratitude in Personal and Professional Life",
    "How to Build and Scale a Startup in 2024"
]

BLOG_CONTENT = [
    """
    <p>In today’s fast-paced world, productivity is essential. Here are <strong>10 tips</strong> that can help you get more done in less time.</p>
    <ul>
        <li>Plan your day in advance.</li>
        <li>Use time blocking to manage tasks.</li>
        <li>Take regular breaks.</li>
    </ul>
    <p>Implement these tips, and you’ll notice a significant boost in your <em>productivity</em>.</p>
    """,
    
    """
    <p>Meditation has numerous benefits for mental health. Here's how to start:</p>
    <ol>
        <li>Find a quiet place.</li>
        <li>Focus on your breath.</li>
        <li>Let go of any distractions.</li>
    </ol>
    <p>Try meditating for just <strong>10 minutes</strong> a day, and see how it changes your mind and body.</p>
    """,
    
    """
    <p>Coding can be an enjoyable journey when you have the right resources. Below are some useful tips:</p>
    <ul>
        <li>Practice daily, even for 30 minutes.</li>
        <li>Join coding communities.</li>
        <li>Work on real-life projects.</li>
    </ul>
    <p>By following these steps, you'll become a better programmer and enjoy the process more!</p>
    """,
    
    """
    <p>Healthy eating is the foundation of a good life. Here are some tips to keep in mind:</p>
    <ul>
        <li>Include more fruits and vegetables in your meals.</li>
        <li>Avoid processed foods as much as possible.</li>
        <li>Drink plenty of water throughout the day.</li>
    </ul>
    <p>Remember, your body is your temple, and nourishing it properly is key to a happy life.</p>
    """,
    
    """
    <p>Freelancing offers many benefits like flexible working hours, but it can also come with challenges. Here’s how to make it work for you:</p>
    <ul>
        <li>Create a dedicated workspace.</li>
        <li>Set clear boundaries with clients.</li>
        <li>Manage your time effectively.</li>
    </ul>
    <p>By maintaining discipline, you can have a successful freelance career with a balanced life.</p>
    """,
    
    """
    <p>Traveling on a budget doesn’t mean missing out on great experiences. Here are some strategies to help:</p>
    <ul>
        <li>Book flights in advance.</li>
        <li>Stay in budget accommodations like hostels or Airbnbs.</li>
        <li>Use public transportation instead of taxis.</li>
    </ul>
    <p>With these tips, you can travel the world without breaking the bank!</p>
    """,
    
    """
    <p>Starting a blog can be overwhelming, but following these steps will help you get started:</p>
    <ol>
        <li>Choose a niche you are passionate about.</li>
        <li>Select a blogging platform (like WordPress or Blogger).</li>
        <li>Write engaging and informative content.</li>
    </ol>
    <p>Once you have these basics in place, you’ll be well on your way to becoming a successful blogger.</p>
    """,
    
    """
    <p>When managing stress, it’s important to practice self-care regularly. Here’s how:</p>
    <ul>
        <li>Practice mindfulness or meditation.</li>
        <li>Exercise regularly, even if it’s a short walk.</li>
        <li>Take time to disconnect from technology.</li>
    </ul>
    <p>By focusing on self-care, you can reduce stress and improve your overall well-being.</p>
    """,
    
    """
    <p>Investing in real estate can be a smart financial decision. Consider these factors before getting started:</p>
    <ul>
        <li>Research the market thoroughly.</li>
        <li>Start small with affordable properties.</li>
        <li>Work with experienced agents and investors.</li>
    </ul>
    <p>Real estate is a long-term investment, so be patient and plan for the future.</p>
    """,
    
    """
    <p>Public speaking is a vital skill that can boost your career. Here are a few techniques to improve:</p>
    <ul>
        <li>Practice in front of a mirror or record yourself.</li>
        <li>Know your audience and tailor your message accordingly.</li>
        <li>Focus on your body language and tone.</li>
    </ul>
    <p>With practice and confidence, you’ll become a powerful and engaging speaker.</p>
    """
]


def get_random_name():
    return NAMES_LIST[random.randint(0,95)]

def get_random_title():
    return BLOG_TITLES[random.randint(0,99)]

def get_random_caption():
    return BLOG_CONTENT[random.randint(0,9)]

 
def register_user(email, password):
    response = requests.post(f"{BASE_URL}/register", json={"email": email, "password": password, "role" : "user"})
    return response.json()

def login_user(email, password):
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password })
    return response.json()

def create_blog(auth_token, title, caption, image_url='https://picsum.photos/200'):
    headers = {
        'Authentication-Token': f'{auth_token}'  # Assuming you're using Bearer token
    }
    response = requests.post(f"{BASE_URL}/api/blogs", json={
        "title": title,
        "caption": caption,
        "image_url": image_url
    }, headers=headers)
    return response.json()

def follow_user(auth_token, follower_id, followed_id):
    headers = {
        'Authentication-Token': f'{auth_token}'  # Assuming you're using Bearer token
    }
    response = requests.get(f"{BASE_URL}/follow/{followed_id}", headers=headers)
    return response.json()

def seed_database():
    users = []
    # Register 10 users and log them in
    for i in range(10):
        email = f"{get_random_name()}@example.com"
        password = "1234"
        register_user(email, password)
        login_response = login_user(email, password)
        if 'token' in login_response:
            users.append({"id": i + 1, "email": email, "token": login_response['token']})

    
    # Create blogs for each user
    for user in users:
        user_id = user['id']
        auth_token = user['token']
        for i in range(3):  # Create 3 blogs per user
            title = get_random_title()
            caption = get_random_caption()
            create_blog(auth_token, title, caption)

    # Create followers
    for user in users:
        followed_users = random.sample([u for u in users if u['id'] != user['id']], k=random.randint(1, len(users) - 1))
        for followed in followed_users:
            follow_user(user['token'], user['id'], followed['id'])

if __name__ == "__main__":
    seed_database()
