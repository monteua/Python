#!/bin/python3

from itertools import combinations


def count_topics(mem1, mem2):
    known_topics = 0
    for topic_num in range(len(mem1)):
        if mem1[topic_num] == "1":
            known_topics += 1
        elif mem1[topic_num] == "0" and mem2[topic_num] == "1":
            known_topics += 1
    return known_topics


def acmTeam(topic):
    team_result = []
    teams = list(combinations(topic, 2))

    for team in teams:
        calc = count_topics(team[0], team[1])
        team_result.append(calc)

    max_known_topics = max(team_result)
    team_with_max_topics = team_result.count(max_known_topics)

    return [max_known_topics, team_with_max_topics]


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]

    topics = []
    topic_i = 0

    for topic_i in range(n):
        topic_t = str(input().strip())
        topics.append(topic_t)
    result = acmTeam(topics)
    print("\n".join(map(str, result)))