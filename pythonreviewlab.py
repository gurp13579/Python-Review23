def create_youtube_video(title,description):
	video = {"title": title, "description": description, "like": 0, "dislikes": 0, "comments":{}}
def like(video):
	if 'like' in video:
		video["like"] += 1
		return video
def dislike(video):
	if 'dislikes' in video
	video["dislikes"] += 1
	return video
def comments(username,video,comment_txt):
	video['comments'][username] = comment_txt
	return video 

vid = create_youtube_video("ffs", "fs2242")
for i in range(495):
	like(vid)

print(vid)

comments("sa", vid, "darsra")

print(vid)