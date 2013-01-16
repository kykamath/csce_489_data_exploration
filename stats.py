'''
Created on Jan 16, 2013

@author: krishnakamath
'''
from bs4 import BeautifulSoup
from operator import itemgetter
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def get_data():
    def get_entry_dict(entry):
        entry_dict = dict([(key, entry.find(key).get_text().strip())
                                                for key in ['id', 'title', 'updated', 'georss:point', 'georss:elev']])
        entry_dict['point'] = map(float, entry_dict['georss:point'].split()); del entry_dict['georss:point']
        entry_dict['size'] = float(entry_dict['title'].split()[1][:-1]) 
        entry_dict['depth'] =  float(entry.find('summary').get_text().split()[-2][1:])
        return entry_dict
    return map(get_entry_dict, BeautifulSoup(file('7day-M2.5.xml').read()).find_all('entry'))

def print_central_tendancies():
    sizes = map(itemgetter('size'), get_data())
    print 'mean: ', np.mean(sizes)
    print 'median: ', np.median(sizes)
    print 'variance: ', np.var(sizes)
    print 'standard deviation: ', np.std(sizes)

def boxplot():
    plt.boxplot(map(itemgetter('size'), get_data()))
    plt.show()

def histogram():
    plt.hist(map(itemgetter('size'), get_data()))
    plt.show()

def correlation():
    sizes = map(itemgetter('size'), get_data())
    depths = map(itemgetter('depth'), get_data())
    print stats.pearsonr(sizes, depths)
    plt.scatter(sizes, depths)
    plt.xlabel('Richter scale (M)')
    plt.ylabel('Depth (mi)')
    plt.show()

if __name__ == '__main__':
#    print_central_tendancies()
#    boxplot()
#    histogram()
    correlation()