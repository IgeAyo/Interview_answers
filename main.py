import re
import psycopg2

# Web page data with the colors
web_page_data = """
<table>
    <thead>
        <th>DAY</th><th>COLOURS</th>
    </thead>
    <tbody>
        <tr>
            <td>MONDAY</td>
            <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
        </tr>
        <tr>
            <td>TUESDAY</td>
            <td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
        </tr>
        <tr>
            <td>WEDNESDAY</td>
            <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
        </tr>
        <tr>
            <td>THURSDAY</td>
            <td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
        </tr>
        <tr>
            <td>FRIDAY</td>
            <td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
        </tr>
    </tbody>
</table>
"""

# Extract colors from web page data
colors = re.findall(r'[A-Z]+', web_page_data)

# 1. Which color of shirt is the mean color?
mean_color = max(set(colors), key=colors.count)
print("Mean Color:", mean_color)

# 2. Which color is mostly worn throughout the week?
most_common_color = max(set(colors), key=colors.count)
print("Most Common Color:", most_common_color)

# 3. Which color is the median?
sorted_colors = sorted(colors)
n = len(sorted_colors)
median_color = sorted_colors[n // 2]
print("Median Color:", median_color)

# 4. BONUS: Get the variance of the colors

color_frequencies = {color: colors.count(color) for color in set(colors)}
mean_frequency = sum(color_frequencies.values()) / len(color_frequencies)
variance = sum((frequency - mean_frequency) ** 2 for frequency in color_frequencies.values()) / len(color_frequencies)
print("Variance of Colors:", variance)
# 5. BONUS: If a color is chosen at random, what is the probability that the color is red?
red_count = colors.count("RED")
total_count = len(colors)
red_probability = red_count / total_count
print("Probability of choosing red color:", red_probability)

# 6. Save the colors and their frequencies in PostgreSQL database
conn = psycopg2.connect(database="Bincom_colors", user="Ayo", password="Ayom1po1", host="localhost", port="5432")
cursor = conn.cursor()

# Create a table to store the color frequencies
cursor.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(20) PRIMARY KEY,
        frequency INTEGER
    );
""")

# Insert color frequencies into the table
for color in set(colors):
    frequency = colors.count(color)
    cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

conn.commit()
conn.close()
