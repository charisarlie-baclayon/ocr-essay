import re

def remove_nextlines(text):
  """
  Removes next lines after sentence-ending punctuations.

  Args:
      text: The text to process.

  Returns:
      The text with next lines removed.
  """
  # Regular expression pattern to match any newline character
  pattern = re.compile(r"\n")

    # Replace matched patterns with an empty string
  return pattern.sub(" ", text)

#   # Regular expression pattern to match sentences and next lines
#   pattern = r"([\.\?!])\n"

#   # Replace matched patterns with a space and punctuation
#   return re.sub(pattern, r"\1 ", text)
  

# # Example usage
# text_with_nextlines = """The Paradox of Social Media: Fostering Connection or Fueling Isolation?
# In the age of constant connectivity, social media platforms have woven themselves into the fabric of our daily lives. They offer a seemingly unparalleled ability to connect with friends, family, and even strangers across the globe. Yet, lurking beneath the surface of endless profiles and curated interactions lies a complex paradox: while social media ostensibly fosters connection, it can also fuel isolation and loneliness.

# On the one hand, social media provides a platform for meaningful interaction. It allows us to share experiences, celebrate milestones, and offer support to loved ones in real-time. We can reconnect with old friends, discover new communities, and engage in discussions with individuals who share our interests. This online interaction can be particularly valuable for those who face geographical or social barriers, fostering a sense of belonging and community.

# However, the curated nature of social media can paint an unrealistic picture of reality. Platforms are often used to showcase the highlights of one's life, carefully filtered and edited to present an idealized version of oneself. This constant exposure to seemingly perfect lives can fuel feelings of inadequacy and social comparison, leading to isolation and loneliness. Additionally, the fleeting nature of online interactions can leave individuals feeling disconnected, craving deeper, more meaningful connections that go beyond the surface-level engagement offered by likes and comments.

# Furthermore, the algorithms that underpin social media platforms often create echo chambers, reinforcing existing biases and limiting exposure to diverse viewpoints. This can lead to polarization and a sense of isolation from those who hold different opinions or beliefs. Moreover, the addictive nature of social media can consume valuable time and energy that could be used for cultivating in-person relationships and engaging in activities that foster genuine connection.

# So, how do we navigate this paradox? The key lies in striking a balance. Embracing the positive aspects of social media – for staying connected, sharing experiences, and discovering new communities – while remaining mindful of its potential pitfalls is crucial. This involves being conscious of the curated nature of online interactions, diversifying our online feeds to expose ourselves to different perspectives, and setting limits on our social media usage to prioritize real-world connections.

# Ultimately, social media is a tool, and like any tool, it can be used for good or for harm. The onus lies on each individual to use it responsibly and intentionally, fostering genuine connection while guarding against the isolation it can paradoxically breed. Only then can we harness the power of social media to truly connect, not isolate, ourselves and each other."""

# text_without_nextlines =  remove_nextlines(text_with_nextlines)

# print(text_without_nextlines)
