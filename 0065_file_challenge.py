# appends a multiplication table to the jabberwocky poem file

with open('./data/sample.txt', mode='a') as jabberwocky:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{:>4} times {} is {}".format(j, i, i*j), file=jabberwocky)
        print('-' * 20, file=jabberwocky)






    