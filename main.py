from read_csv_pos import DistanceMatrix

test1 = DistanceMatrix("input.csv", header=0)

resp = test1.calc_distance_matrix()

print(resp)
