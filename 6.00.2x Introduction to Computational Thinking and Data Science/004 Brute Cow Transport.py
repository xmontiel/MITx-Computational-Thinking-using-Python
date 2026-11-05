# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:20:50 2026

@author: Xuan
"""
# Enter your code for the Brute Force Cow Transport here 

from ps1_partitions import get_partitions

def brute_force_cow_transport(cows, limit=10):
    cow_list = list(cows.keys())
    best_partition = None

    for partition in get_partitions(cow_list):
        valid = True

        for trip in partition:
            total_weight = 0

            for cow in trip:
                total_weight += cows[cow]

            if total_weight > limit:
                valid = False
                break

        if valid:
            if best_partition is None or len(partition) < len(best_partition):
                best_partition = partition

    return best_partition