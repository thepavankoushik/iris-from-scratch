# -*- coding: utf-8 -*-
"""Proj3HemaFuzzyLloyd.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IC1yjv1GFJDW9X7YEUHP-sCaSPkRK-cZ
"""

import sys
import numpy as np
from numpy.random import seed
import math
seed(12)

def eud(ss, dd):
  b = (ss-dd) * (ss - dd)
  su = 0
  for i in range(len(b)):
    su += b[i]
  return np.sqrt(su)

class IrisFuzzyLloyd:
  def __init__(self, X, k, r, m):
    self.X = X
    self.k = k
    self.r = r
    self.m = m
    self.n_rows, self.n_cols = X.shape
    self.k_clusters = None
    self.mem_matrix = None

  def _init_k_random_centers(self):
    k_random_indices = np.random.choice(self.n_rows, self.k, replace=False)
    self.k_centers = []
    for random_index in k_random_indices:
      self.k_centers.append(self.X[random_index])
  
  def _init_mem_matrix(self):
    self.mem_matrix = list()
    for i in range(self.n_rows):
      empty_list = [None for x in range(self.k)]
      self.mem_matrix.append(empty_list)
  
  def _get_mem_matrix(self):
    ratio=float(2/(m-1))
    for i in range(self.n_rows):
      distances = list()
      for j in range(self.k):
        distances.append(eud(self.X[i], self.k_centers[j]))
      for j in range(self.k):
        den = sum(math.pow(float(distances[j]/max(distances[q], 1)), ratio) for q in range(self.k))
        self.mem_matrix[i][j] = float(1/max(den))

  def _get_k_hard_clusters(self):
    self.k_clusters=list()
    for i in range(self.n_rows):
        max_val, idx = max((val, idx) for (idx, val) in enumerate(self.mem_matrix[i]))
        self.k_clusters.append(idx)

  def run(self):
    self._init_k_random_centers()
    self._init_mem_matrix()
    for i in range(self.r):
      self._get_mem_matrix()
    self._get_k_hard_clusters()
    return self.k_clusters, self.k_centers, self.mem_matrix

def qerror_hard_cluster(k, X, y):
  res = 0
  for i in range(1, k+1):
    a = []
    for index in range(len(y)):
      if(y[index] == i):
        a.append(X[index])
    a_su = sum(a)
    a_mean = a_su/max(len(a), 1)
    dist = []
    for j in a:
      dist.append((j-a_mean)**2)
    for d in dist:
      res += sum(d)
  return res

def qerror_soft_cluster(k, X, mem_matrix, cluster_centers):
  res = 0
  for i in range(len(X)):
    for j in range(k):
      res += mem_matrix[i][j] * np.linalg.norm(X[i] - cluster_centers[j])**2
  return res

X = np.loadtxt('./iris-data.csv', delimiter=',')
k = 3
r = 1
m = 2
iris_lloyd = IrisFuzzyLloyd(X, k, r, m)
clusters, centers, matrix = iris_lloyd.run()

qerror_hard_cluster(k, X, clusters)

qerror_soft_cluster(k, X, matrix, centers)

clusters
