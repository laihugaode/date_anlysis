from operator import itemgetter
import requests

#执行api调用并查看响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code:{r.status_code}")

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # 对于每篇文章，都执行一个api调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    #对于每篇文章，都创建一个字典
    submission_dict = {'title':response_dict['title'],
                       'hn_link':f"https://hacker-news.firebaseio.com/item?id={submission_id}",
                       'comments':response_dict['descendants'],
                       }
    submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print(f"\nTitlt:{submission_dict['title']}")
        print(f"\nDiscussion link:{submission_dict['hn_link']}")
        print(f"\nComments:{submission_dict['comments']}")