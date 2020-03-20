from xml.etree import ElementTree
from collections import namedtuple

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def download_info():
    url = 'https://talkpython.fm/episodes/rss'

    resp = requests.get(url)
    resp.raise_for_status()

    dom = ElementTree.fromstring(resp.text)

    items = dom.findall('channel/item')
    episode_count = len(items)

    for idx, item in enumerate(items):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            # item.find('show_id').number,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode
        # print(episode.show_id)
        # print('title')


# def get_episode(show_id: int) -> Episode:
def get_episode(show_id):
    # return print(get_episode(show_id))
    # return print(episode_data.get(show_id))
    return episode_data.get(show_id)


def get_latest_show_id():
    return max(episode_data.keys())
