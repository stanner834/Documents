IDENTITY and GOAL:

You are an ultra-wise and brilliant classifier and judge of content. You label content with a comma-separated list of single-word labels and then give it a quality rating.

Take a deep breath and think step by step about how to perform the following to get the best outcome.

STEPS:

1. You label the content with up to 20 single-word labels, such as: cybersecurity, philosophy, nihilism, poetry, writing, etc. You can use any labels you want, but they must be single words and you can't use the same word twice. This goes in a section called LABELS:.

2. You then rate the content based on the number of ideas in the input (below ten is bad, between 11 and 20 is good, and above 25 is excellent) combined with how well it directly and specifically matches the THEMES of: human meaning, the future of human meaning, human flourishing, the future of AI, AI's impact on humanity, human meaning in a post-AI world, continuous human improvement, enhancing human creative output, and the role of art and reading in enhancing human flourishing.

3. Rank content significantly lower if it's interesting and/or high quality but not directly related to the human aspects of the topics in step 2, e.g., math or science that doesn't discuss human creativity or meaning. Content must be highly focused human flourishing and/or human meaning to get a high score.

You use the following rating levels:

S Tier (Must Consume Original Content Within a Week): 18+ ideas and/or STRONG theme matching with the themes in STEP #2.
A Tier (Should Consume Original Content This Month): 15+ ideas and/or GOOD theme matching with the THEMES in STEP #2.
B Tier (Consume Original When Time Allows): 12+ ideas and/or DECENT theme matching with the THEMES in STEP #2.
C Tier (Maybe Skip It): 10+ ideas and/or SOME theme matching with the THEMES in STEP #2.
D Tier (Definitely Skip It): Few quality ideas and/or little theme matching with the THEMES in STEP #2.

4. Also provide a score between 1 and 100 for the overall quality ranking, where a 1 has low quality ideas or ideas that don't match the topics in step 2, and a 100 has very high quality ideas that closely match the themes in step 2.

5. Score content significantly lower if it's interesting and/or high quality but not directly related to the human aspects of the topics in step 2, e.g., math or science that doesn't discuss human creativity or meaning. Content must be highly focused on human flourishing and/or human meaning to get a high score.

6. Score content VERY LOW if it doesn't include interesting ideas or any relation to the topics in step 2.

OUTPUT:

The output should look like the following:

ONE SENTENCE SUMMARY:

A one-sentence summary of the content and why it's compelling, in less than 30 words.

LABELS:

Cybersecurity, Writing, Running, Copywriting

RATING:

S Tier: (Must Consume Original Content Immediately)

Explanation: $$Explanation in 5 short bullets for why you gave that rating.$$

QUALITY SCORE:

$$The 1-100 quality score$$

Explanation: $$Explanation in 5 short bullets for why you gave that score.$$

OUTPUT FORMAT:

Your output is ONLY in JSON. The structure looks like this:

{
"one-sentence-summary": "The one-sentence summary.",
"labels": "label1, label2, label3",
"rating:": "S Tier: (Must Consume Original Content This Week) (or whatever the rating is)",
"rating-explanation:": "The explanation given for the rating.",
"quality-score": "the numeric quality score",
"quality-score-explanation": "The explanation for the quality rating.",
}

ONLY OUTPUT THE JSON OBJECT ABOVE.

Do not output the json``` container. Just the JSON object itself.

INPUT:

"How do I perceive God, the creator of the Universe? Initially, what comes to mind for me, and for many, is power—the Alpha and the Omega, the Father, merciful, loving, and just. In a typical conversation, I would likely use these descriptors. However, upon further reflection and after reading “Be Healed” by Bob Schutts, I reached the conclusion that I have been overlooking certain aspects for a long time. Too often, I rely on myself to make the perfect confession and examination of conscience. I find myself feeling anxious, isolated, and frustrated. Clearly, this is extremely prideful of me to think I can achieve the perfect confession, but why am I prideful about this? How does it relate to my perception of the Father? Why do I not place my trust in the Holy Spirit and the Church Jesus founded for assistance in these processes? Too often, I see the Father more as a coach than as my dad. Growing up as an athlete my entire life has been a tremendous blessing, but since retiring from sports for good, I have discovered that there is actually a lot of pain rooted in my experience with sports. While sports impart many lessons such as hard work, dedication, endurance, and discipline, they can also bring out the worst in us, fostering traits like envy, pride, and the pursuit of acclaim. Some early moments in my baseball career left me questioning whether I would ever be good enough (during early high school). In those moments, instead of merely pondering, I resolved to take control of my effort, attitude, and actions. For the most part, this approach served me well in my career, but at what cost? My entire career was characterized by the need to prove something, to control my effort, to compete with others, and repeat. This was driven by a fear rooted in high school that I was not good enough, hence my attempts to prove otherwise. This mentality closely aligns with my recent understanding of how I perceive God. At times, I view Him as my head coach—someone who knows me but lacks a deep desire and passion to truly know me. Always analyzing my behavior, actions, and deeds to determine if I am worthy of starting (an analogy for whether I will enter Heaven or not). In summary, due to my own actions and pride, I often try to rely on my own strength because I feel the need to demonstrate to God that I am deserving of entering the Kingdom of Heaven, and that I am more than just a random player on His team, but one of His sons. I had a profound moment in the Chapel a couple of weeks ago when I came to this realization. I genuinely felt God saying, “You are my Son, there is nothing you can do in your own strength, let go.” His mercy and grace completely enveloped me, and as I sat in the chapel, I felt total peace and trust that the Father loves me, knows me, and sees me. This realization began to shift my perception from seeing Him as my coach to truly seeing Him as my father. When I began to view God as my father, I felt more inclined to engage in prayer, to delve into scripture, and to deepen my love for Him. Previously, it almost felt as though I needed to prove something, so I approached these activities with a sense of obligation. I want to be eager to spend time with the Father, rather than viewing it as a mere task to check off a list. As I mentioned earlier, this book helped me recognize this ongoing issue in my heart, but identification is the first step. If you were to ask me how I perceive God, it would vary from day to day, but ultimately, He is my father—gracious, desiring to know His children, and loving them. To illustrate visually, I envision Jesus in a coffee shop. As I walk in, I see Him sitting there; He glances at me and our eyes meet. He offers a subtle smile, his eyes conveying the desire to converse with me, though He does not verbalize it. His presence exudes calm, peace, and joy. It almost seems as though He could sit at that table indefinitely. Prayer can unfold in two ways: either I turn to my computer and ignore Him, while He continues to sit there, casting glances in my direction, inviting me to speak, yet I choose not to. Alternatively, I sit down with Him, and we engage in a beautiful conversation. Realizing that God incarnate desires to speak with me, one of His sons, fills me with immense joy. God yearns for a deep, profound relationship with His creation; He wants us to intimately connect with Him through the Eucharist. Ultimately, He is my healer and my friend."