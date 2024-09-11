import requests

class PexelsAPI():
    def __init__(self) -> None:
        self.api_key = 'Ob9g5imJ9ssEzFkuxYjQ4j2KhyXzHedJVXxkOp2clpGi5WNkrhcWQXD7'
        self.baseURL = 'https://api.pexels.com/v1/'
        self.headers = {'Authorization': self.api_key}

    def getBackgroundFromCollections(self):
        response = requests.get(self.baseURL + 'collections/h2ikby7', headers=self.headers)
        x = response.json()

        name = 'video?.mp4'
        index = 1
        for vid in x['media']:
            v = vid['video_files'][-1]
            outfile = name.replace('?', str(index))

            with open(f'backgroundVids/{outfile}', 'w') as f:
                f.write(v['link'])
                index += 1
            pass
        pass