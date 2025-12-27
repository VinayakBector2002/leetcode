from collections import defaultdict

'''
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

Naïve soln 
    -> If 1000< invalid
    -> For each trx go over all the (other) trx in front to check if the transactions are valid 
'''

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalidIdx = set()
        groupedTrx = defaultdict(list) # name: (time, city, idx)

        for idx, trx in enumerate(transactions):
            name, time, amount, city = trx.split(",")
            time, amount = int(time), int(amount)
            
            if amount > 1000:
                invalidIdx.add(idx)
            
            for gTrx in groupedTrx[name]:
                gTime, gCity, gIdx = gTrx
                if gCity != city and abs(gTime - time) <= 60:
                    invalidIdx.add(idx)
                    invalidIdx.add(gIdx)
            
            groupedTrx[name].append((time, city, idx))
        
        return [transactions[i] for i in invalidIdx]

        