import streamlit as st
from PIL import Image



#===>add profile image<====

# Set the title for the sidebar
st.sidebar.title("Profile")

# Use markdown to add a custom image with CSS styling
st.sidebar.markdown(
    """
    <style>
    .sidebar .avatar {
        width: 100px;
        height: 100px;
        border-radius: 25%;
        object-fit: cover;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True
)

# Path to your image
image_path = "kushal.jpg"  # Replace with your image path

# Display the image with circular shape in the sidebar
st.sidebar.image(image_path, width=150, caption="Kushal Vishwakarma")

#=========<<


# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Skills", "Projects", "Education", "Contact"])

# Header Section
def header():
    st.title("Data Scientist Portfolio")
    st.subheader("👋 Hi, I'm Kushal Vishwakarma")
    st.write("""
    I am aspiring data scientist passionate about solving problems with data. I specialize in building machine learning models, analyzing datasets, and delivering actionable insights.
    """)

# About Section
def about():
    st.header("About Me")
    st.write(""""I am an aspiring data scientist with a strong foundation in mathematics, statistics, and programming. Recently graduated with a degree in "B.Sc. in Computer Science" from "Mahatma Gandhi Kashi Vidyapith University" Varanasi,Utter Pradesh , I have developed a keen interest in using data to solve real-world problems.

During my studies, I completed realtime projects on 'Sentimental Analysis','face detection'/'face recognition attendace system','Movies recommandation system'..etc and earned certifications in "Data Science" by "Ducat India Institute" Noida.

I am skilled in Python, SQL,data manupulation and data visualization tools like Power BI, Matplotlib. My passion lies in exploring data patterns and leveraging machine learning algorithms to generate actionable insights. I am eager to contribute to challenging projects that push the boundaries of innovation in data science.
""")
    






# Skills Section
def skills():
    st.header("Skills")
    st.write("""
    ### Programming
    - Python ,SQL

    ### Data Analysis
    - Pandas, NumPy, Scikit-learn(sklearn)

    ### Visualization
    - Matplotlib, Seaborn, Power BI

    ### Machine Learning
    - Regression, Classification, Clustering, Deep Learning

    ### Tools & Technologies
    - Jupyter notebook,Github
    """)

# Projects Section
def projects():
    st.header("Projects")
    st.header(">>>>>Machine Learning Projects<<<<<")
    project_list = [
        {
            "title": "Sentiment Analysis",
            "description": "This code is a Sentiment Analysis Web Application built using Streamlit and TextBlob. It analyzes the sentiment of user-provided text and classifies it as positive, negative, or neutral. The application displays appropriate images and messages based on the sentiment detected.",
            "link": "https://github.com/kushal70001/Sentiment.git"
        },
        {
            "title": "face-detection/face-recognition-system",
            "description": "A Face Recognition System built using Python and OpenCV, designed for real-time face detection, recognition, and attendance management. This project demonstrates the use of computer vision techniques to recognize faces and automate attendance processes efficiently.",
            "link": "https://github.com/kushal70001/face-detection-face-recognition-system.git"
        },
        {
            "title": "content-based-movie-recommendation-system",
            "description": "content-based movie recommendation system that uses TF-IDF Vectorization and Nearest Neighbors to recommend movies based on the description similarity.",
            "link": "https://github.com/kushal70001/content-based-movie-recommendation-system.git"
        },
        {
            "title": "Collaborative-Filtering-movie-recommendation-system-",
            "description": "This code implements a Collaborative Filtering movie recommendation system based on user-user similarity using Nearest Neighbors. The system recommends movies for a specific user (in this case, user ID 122) based on the ratings provided by similar users",
            
            "link": "https://github.com/kushal70001/Collaborative-Filtering-movie-recommendation-system-.git"
        }



        
    ]
    for project in project_list:
        st.write(f"#### {project['title']}")
        st.write(project["description"])
        st.markdown(f"[View on GitHub]({project['link']})")


# Education Section
def education():
    st.header("Education")
    st.write("""
    ### Certification in Data Science
    - Ducat India Institute,Noida, - 2024

    ### Bachelor of Science(B.sc in cs)
    - Mahatma Gandhi Kashi Vidyapith,Varanasi, - 2022
    """)

# Contact Section
def contact():
    st.header("Contact Me")
    st.write("Feel free to reach out to me through any of the platforms below:")
    st.write("- 📧 Email: kushal17796@gmail.com")
    st.write("- 💼 LinkedIn: www.linkedin.com/in/kushal-vishwakarma-525289293")

    st.write("- 📂 GitHub: https://github.com/kushal70001")

# Navigation
if menu == "Home":
    header()
elif menu == "About":
    about()
elif menu == "Skills":
    skills()
elif menu == "Projects":
    projects()
elif menu == "Education":
    education()
elif menu == "Contact":
    contact()
