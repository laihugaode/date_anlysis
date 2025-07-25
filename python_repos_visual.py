import requests
import plotly.express as px

# 执行api调用并查看响应
url = 'https://api.github.com/search/repositories'
url += '?q=language:python&sort=stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转换为字典
response_dict = r.json()
print(f"Complete results {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
repo_names, stars, hover_texts, repo_links = [], [], [], []

# 研究每个仓库
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    
    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
fig = px.bar(x=repo_links, y=stars,
             labels={'x': 'Repository', 'y': 'Stars'},
             hover_name=hover_texts)
fig.update_layout(title_font_size=24,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()