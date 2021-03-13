print("----------嵌套----------")
#  字典alien_0包含一个外星人的各种信息，但无法存储第二个外星人的信息，
#  创建外星人列表，方便管理，每个外星人都是一个字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n----------现实----------")
#  每个外星人都是使用代码自动生成
#  创建一个用于存储外星人的空列表
aliens = []

#  创建30个绿色的外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#  显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#  显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

print("\n----------修改----------")
#  随着游戏进行，有些外星人会变色且移动速度会加快。 必要时，我们可以
#  使用for循环和if语句来修改某些外星人的颜色
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#  显示5个外星人
for alien in aliens[0:5]:
    print(alien)
print("...")

print("\n----------进一步修改----------")
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['poinst'] = 15

for alien in aliens[:5]:
    print(alien)
