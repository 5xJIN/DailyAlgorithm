'''
Min : 0.02ms, 10.3MB
Max : 102.80ms, 21.2MB
'''


def solution(enroll: list, referral: list, seller: list, amount: list):
    parents, total = dict(), dict()

    for name, ref in zip(enroll, referral):
        parents[name] = ref
        total[name] = 0

    for seller_name, amt in zip(seller, amount):
        parent = parents[seller_name]
        total_price = amt * 100
        benefit = total_price // 10
        profit = total_price - benefit

        total[seller_name] += profit

        while (parent != "-") and (benefit >= 1):
            share = benefit
            benefit = share // 10
            profit = share - benefit

            total[parent] += profit
            parent = parents[parent]

    return list(total.values())



print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))

