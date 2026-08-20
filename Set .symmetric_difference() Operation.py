n = int(input())

english_subscribers = set(input().split())

b = int(input())

french_subscribers = set(input().split())

exclusive_subscribers = english_subscribers.symmetric_difference(french_subscribers)

print(len(exclusive_subscribers))
