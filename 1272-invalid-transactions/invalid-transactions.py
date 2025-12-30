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
        invalidTrxIdx = set()
        nameToMetaData = defaultdict(list) # name: (idx, time, city)


        for idx, trx in enumerate(transactions):
            name, time, amt, city = trx.split(",")
            if int(amt) > 1000:
                invalidTrxIdx.add(idx)
                
            prevNamedTrx = nameToMetaData[name]
            for pTrx in prevNamedTrx:
                gIdx, gTime, gCity = pTrx
                if gCity != city and abs(int(time) - int(gTime)) <= 60:
                    invalidTrxIdx.add(gIdx)
                    invalidTrxIdx.add(idx)

            nameToMetaData[name].append((idx, time, city))
        
        return [transactions[i] for i in invalidTrxIdx]
