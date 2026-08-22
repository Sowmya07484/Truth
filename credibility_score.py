def final_score(news_score, image_score, video_score):

    final = (news_score + image_score + video_score) / 3

    return round(final,2)