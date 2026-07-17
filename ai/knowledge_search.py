from knowledge.models import KnowledgeArticle



def search_solution(query):


    query = query.lower()


    articles = KnowledgeArticle.objects.all()


    for article in articles:


        text = (
            article.title +
            " " +
            article.problem
        ).lower()



        keywords = query.split()



        matches = 0


        for word in keywords:

            if word in text:

                matches += 1



        if matches >= 2:

            return {

                "solution": article.solution,

                "title": article.title

            }



    return None