from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# ==========================================
# Find Similar Previous Ticket
# ==========================================

def find_similar_ticket(description, tickets):


    if not tickets.exists():

        return None



    ticket_texts = []


    for ticket in tickets:

        ticket_texts.append(
            ticket.description
        )



    # Add current ticket

    all_texts = ticket_texts + [description]



    vectorizer = TfidfVectorizer()



    vectors = vectorizer.fit_transform(
        all_texts
    )



    similarity_scores = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )



    best_score = similarity_scores.max()



    best_index = similarity_scores.argmax()



    # Threshold

    if best_score > 0.5:


        similar_ticket = tickets[
            best_index
        ]


        return {

            "ticket": similar_ticket,

            "score": round(
                float(best_score),
                2
            )

        }



    return None