# Movie Ratings Analysis

## **Overview**

In this assignment, you will leverage Spark Structured APIs to analyze a dataset containing employee information from various departments within an organization. Your goal is to extract meaningful insights related to employee satisfaction, engagement, concerns, and job titles. This exercise is designed to enhance your data manipulation and analytical skills using Spark's powerful APIs.

## **Objectives**

By the end of this assignment, you should be able to:

1. **Data Loading and Preparation**: Import and preprocess data using Spark Structured APIs.
2. **Data Analysis**: Perform complex queries and transformations to address specific business questions.
3. **Insight Generation**: Derive actionable insights from the analyzed data.

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

4. **Docker & Docker Compose** (Optional):
   - If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## **Setup Instructions**

### **1. Project Structure**

Ensure your project directory follows the structure below:

```
MovieRatingsAnalysis/
├── input/
│   └── movie_ratings_data.csv
├── outputs/
│   ├── binge_watching_patterns.csv
│   ├──churn_risk_users.csv
│   └── movie_watching_trends.csv
├── src/
│   ├── task1_binge_watching_patterns.py
│   ├── task2_churn_risk_users.py
│   └── task3_movie_watching_trends.py
├── docker-compose.yml
└── README.md
```




- **input/**: Contains the `movie_ratings_data.csv` dataset.
- **outputs/**: Directory where the results of each task will be saved.
- **src/**: Contains the individual Python scripts for each task.
- **docker-compose.yml**: Docker Compose configuration file to set up Spark.
- **README.md**: Assignment instructions and guidelines.

### **2. Running the Analysis Tasks**

You can run the analysis tasks either locally or using Docker.

#### **a. Running Locally**

1. **Navigate to the Project Directory**:
   ```bash
   cd MovieRatingsAnalysis/
   ```

2. **Execute Each Task Using `spark-submit`**:
   ```bash
   spark-submit src/task1_binge_watching_patterns.py
   spark-submit src/task2_churn_risk_users.py
   spark-submit src/task3_movie_watching_trends.py
   ```

3. **Verify the Outputs**:
   Check the `outputs/` directory for the resulting files:
   ```bash
   ls outputs/
   ```
   You should see:
   - `binge_watching_patterns.txt`
   - `churn_risk_users.csv`
   - `movie_watching_trends.csv`

#### **Approach**

1. Data Loading
Objective: Load the movie ratings data into a Spark DataFrame for further analysis.
Process:
The movie ratings data is loaded from a CSV file using Spark's read.csv() method.
A schema is defined explicitly to match the structure of the data, ensuring that each column is read correctly.

2. Task 1: Identifying Binge-Watching Patterns
Objective: Identify users who binge-watch content based on certain criteria.
Process:
Filter users who have watched more than a specified threshold.
Aggregate the data to calculate the percentage of binge-watchers relative to the total users.
The result includes binge-watcher counts and their percentage.

3. Task 2: Identifying Churn-Risk Users
Objective: Identify users with canceled subscriptions and low watch time (<100 minutes).
Process:
Filter users who have SubscriptionStatus = 'Canceled' and WatchTime < 100.
Count the number of churn-risk users.
Generate a result CSV containing the churn-risk user count.

4. Task 3: Movie Ratings Trends
Objective: Analyze the trends of movie ratings over time, including top-rated movies per year and rating distributions.
Process:
Group data by WatchedYear and calculate the average rating per year.
Identify the top-rated movies for each year.
Generate a trend analysis based on average ratings and insights into rating distributions over time.
   

8. **Verify the Outputs**:
   On your host machine, check the `outputs/` directory for the resulting files.

## **Dataset**

## **Dataset: Advanced Movie Ratings & Streaming Trends**

You will work with a dataset containing information about **100+ users** who rated movies across various streaming platforms. The dataset includes the following columns:

| **Column Name**         | **Data Type**  | **Description** |
|-------------------------|---------------|----------------|
| **UserID**             | Integer       | Unique identifier for a user |
| **MovieID**            | Integer       | Unique identifier for a movie |
| **MovieTitle**         | String        | Name of the movie |
| **Genre**             | String        | Movie genre (e.g., Action, Comedy, Drama) |
| **Rating**            | Float         | User rating (1.0 to 5.0) |
| **ReviewCount**       | Integer       | Total reviews given by the user |
| **WatchedYear**       | Integer       | Year when the movie was watched |
| **UserLocation**      | String        | User's country |
| **AgeGroup**          | String        | Age category (Teen, Adult, Senior) |
| **StreamingPlatform** | String        | Platform where the movie was watched |
| **WatchTime**        | Integer       | Total watch time in minutes |
| **IsBingeWatched**    | Boolean       | True if the user watched 3+ movies in a day |
| **SubscriptionStatus** | String        | Subscription status (Active, Canceled) |

---



## **Findings**

**Churn Risk Users:** Successfully identified 11 churn-risk users who have canceled subscriptions and low watch time.
**Binge-Watching Patterns:** These statistics reveal that seniors have the highest proportion of binge-watchers, followed closely by adults and teens.
**Movie Ratings Trends:** The data shows a fluctuating pattern of movie consumption over the years, with 2020 seeing the highest number of movies watched (19), followed by 2018 and 2022.

## **Outputs**

**Task1**

![image](https://github.com/user-attachments/assets/0c09fa7d-2984-4472-8df8-7a3895096188)

**Task2**

![image](https://github.com/user-attachments/assets/8fe2c25f-b74c-413e-8da7-25d487fdc30b)

**Task3**

![image](https://github.com/user-attachments/assets/3c1c2ab6-d4ba-4db9-82e9-ce7d6c91c14a)




## **Grading Criteria**

Your assignment will be evaluated based on the following criteria:

- **Question 1**: Correct identification of departments with over 50% high satisfaction and engagement (1 mark).
- **Question 2**: Accurate analysis of employees who feel valued but didn’t suggest improvements, including proportion (1 mark).
- **Question 3**: Proper comparison of engagement levels across job titles and correct identification of the top-performing job title (1 mark).

**Total Marks: 3**

---

## **Submission Guidelines**

- **Code**: Submit all your PySpark scripts located in the `src/` directory.
- **Report**: Include a report summarizing your findings for each task. Ensure that your report is well-structured, with clear headings and explanations.
- **Data**: Ensure that the `movie_ratings_data.csv` used for analysis is included in the `data/` directory or provide a script for data generation if applicable.
- **Format**: Submit your work in a zipped folder containing all necessary files.
- **Deadline**: [Insert Deadline Here]

---

Good luck, and happy analyzing!
