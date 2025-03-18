# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, count, round as spark_round

# def initialize_spark(app_name="Task1_Binge_Watching_Patterns"):
#     """
#     Initialize and return a SparkSession.
#     """
#     spark = SparkSession.builder \
#         .appName(app_name) \
#         .getOrCreate()
#     return spark

# def load_data(spark, file_path):
#     """
#     Load the movie ratings data from a CSV file into a Spark DataFrame.
#     """
#     schema = """
#         UserID INT, MovieID INT, MovieTitle STRING, Genre STRING, Rating FLOAT, ReviewCount INT, 
#         WatchedYear INT, UserLocation STRING, AgeGroup STRING, StreamingPlatform STRING, 
#         WatchTime INT, IsBingeWatched BOOLEAN, SubscriptionStatus STRING
#     """
#     df = spark.read.csv(file_path, header=True, schema=schema)
#     return df

# def detect_binge_watching_patterns(df):
#     """
#     Identify the percentage of users in each age group who binge-watch movies.

#     TODO: Implement the following steps:
#     1. Filter users who have `IsBingeWatched = True`.
#     2. Group by `AgeGroup` and count the number of binge-watchers.
#     3. Count the total number of users in each age group.
#     4. Calculate the binge-watching percentage for each age group.
#     """
#     pass  # Remove this line after implementation

# def write_output(result_df, output_path):
#     """
#     Write the result DataFrame to a CSV file.
#     """
#     result_df.coalesce(1).write.csv(output_path, header=True, mode='overwrite')

# def main():
#     """
#     Main function to execute Task 1.
#     """
#     spark = initialize_spark()

#     input_file = "/workspaces/MovieRatingsAnalysis/input/movie_ratings_data.csv"
#     output_file = "/workspaces/MovieRatingsAnalysis/outputs/binge_watching_patterns.csv"

#     df = load_data(spark, input_file)
#     result_df = detect_binge_watching_patterns(df)  # Call function here
#     write_output(result_df, output_file)

#     spark.stop()

# if __name__ == "__main__":
#     main()


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, round as spark_round

def initialize_spark(app_name="Task1_Binge_Watching_Patterns"):
    """
    Initialize and return a SparkSession.
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    return spark

def load_data(spark, file_path):
    """
    Load the movie ratings data from a CSV file into a Spark DataFrame.
    """
    schema = """
        UserID INT, MovieID INT, MovieTitle STRING, Genre STRING, Rating FLOAT, ReviewCount INT, 
        WatchedYear INT, UserLocation STRING, AgeGroup STRING, StreamingPlatform STRING, 
        WatchTime INT, IsBingeWatched BOOLEAN, SubscriptionStatus STRING
    """
    df = spark.read.csv(file_path, header=True, schema=schema)
    return df

def detect_binge_watching_patterns(df):
    """
    Identify the percentage of users in each age group who binge-watch movies.
    """
    # Filter users who have IsBingeWatched = True
    binge_watchers = df.filter(col("IsBingeWatched") == True)

    # Group by AgeGroup and count the number of binge-watchers
    binge_watch_summary = binge_watchers.groupBy("AgeGroup").agg(count("*").alias("BingeWatchers"))

    # Count the total number of users in each age group
    total_users = df.groupBy("AgeGroup").agg(count("*").alias("TotalUsers"))

    # Join the binge-watch summary with the total users
    binge_watch_summary = binge_watch_summary.join(total_users, on="AgeGroup")

    # Calculate the binge-watching percentage for each age group
    binge_watch_summary = binge_watch_summary.withColumn("Percentage", 
                                                         spark_round((col("BingeWatchers") / col("TotalUsers")) * 100, 2))

    # Return the final result
    return binge_watch_summary

def write_output(result_df, output_path):
    """
    Write the result DataFrame to a CSV file.
    """
    result_df.coalesce(1).write.csv(output_path, header=True, mode='overwrite')

def main():
    """
    Main function to execute Task 1.
    """
    spark = initialize_spark()

    input_file = "/workspaces/handson-7-spark-structured-api-movie-ratings-analysis-SriLaxmiPrasannaJoginipelli/input/movie_ratings_data.csv"
    output_file = "/workspaces/handson-7-spark-structured-api-movie-ratings-analysis-SriLaxmiPrasannaJoginipelli/Outputs/binge_watching_patterns.csv"


    df = load_data(spark, input_file)
    result_df = detect_binge_watching_patterns(df)  # Call function here
    write_output(result_df, output_file)

    spark.stop()

if __name__ == "__main__":
    main()


