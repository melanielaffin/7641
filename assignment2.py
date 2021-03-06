import mlrose
import pandas
import numpy
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score
import time




print("tsp")
# Create list of city coordinates
coords_list = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]

# Initialize fitness function object using coords_list
fitness_coords = mlrose.TravellingSales(coords = coords_list)

# Create list of distances between pairs of cities
dist_list = [(0, 1, 3.1623), (0, 2, 4.1231), (0, 3, 5.8310), (0, 4, 4.2426), \
             (0, 5, 5.3852), (0, 6, 4.0000), (0, 7, 2.2361), (1, 2, 1.0000), \
             (1, 3, 2.8284), (1, 4, 2.0000), (1, 5, 4.1231), (1, 6, 4.2426), \
             (1, 7, 2.2361), (2, 3, 2.2361), (2, 4, 2.2361), (2, 5, 4.4721), \
             (2, 6, 5.0000), (2, 7, 3.1623), (3, 4, 2.0000), (3, 5, 3.6056), \
             (3, 6, 5.0990), (3, 7, 4.1231), (4, 5, 2.2361), (4, 6, 3.1623), \
             (4, 7, 2.2361), (5, 6, 2.2361), (5, 7, 3.1623), (6, 7, 2.2361)]

# Initialize fitness function object using dist_list
fitness_dists = mlrose.TravellingSales(distances = dist_list)


# Define optimization problem object
problem_fit = mlrose.TSPOpt(length = 8, fitness_fn = fitness_coords, maximize=False)

# Create list of city coordinates
coords_list = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]

# Define optimization problem object
problem_no_fit = mlrose.TSPOpt(length = 8, coords = coords_list, maximize=False)

# Solve problem using the genetic algorithm
start_time = time.time()

best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
print("genetic")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 100, random_state = 2)
print("genetic: 100")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print("simulated annealing")
best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 10, random_state = 2)
print("genetic: 10")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print("simulated annealing")
best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 50, random_state = 2)
print("genetic: 50")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print("simulated annealing")
best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

################################################################
print("max k coloring")
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4),(3,5),(4,5)]
fitness = mlrose.MaxKColor(edges)
problem_fit = mlrose.DiscreteOpt(length = 9, fitness_fn=fitness)

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
print("genetic")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 10, random_state = 2)
print("genetic: 10, tuned")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("simulated annealing")
best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 50, random_state = 2)
print("genetic: 50")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
#
#
# print("simulated annealing")
# best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
#                                               max_attempts = 50, random_state = 2)
# print(best_state)
# print(best_fitness)
# print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 100, random_state = 2)
print("genetic: 100")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
#
#
# print("simulated annealing")
# best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
#                                               max_attempts = 100, random_state = 2)
# print(best_state)
# print(best_fitness)
# print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

################################################################
print("knapsack")
weights = [1, 5, 2, 8, 10]
values = [1, 2, 3, 4, 5]
max_weight_pct = 0.5
fitness = mlrose.Knapsack(weights, values, max_weight_pct)
problem_fit = mlrose.DiscreteOpt(length = 5, fitness_fn=fitness)

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)
print("genetic")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

# Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 10, random_state = 2)
print("genetic: 10")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print("simulated annealing")
best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 10, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

 ##Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 50, random_state = 2)
print("genetic: 50")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
#
#
# print("simulated annealing")
# best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
#                                               max_attempts = 50, random_state = 2)
# print(best_state)
# print(best_fitness)
# print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 50, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

 #Solve problem using the genetic algorithm
best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2,
                                              max_attempts = 100, random_state = 2)
print("genetic: 100")
print(best_state)

print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("random hill")
best_state, best_fitness = mlrose.random_hill_climb(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
#
#
# print("simulated annealing")
# best_state, best_fitness = mlrose.simulated_annealing(problem_fit,
#                                               max_attempts = 100, random_state = 2)
# print(best_state)
# print(best_fitness)
# print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

print("mimic")
best_state, best_fitness = mlrose.mimic(problem_fit,
                                              max_attempts = 100, random_state = 2)
print(best_state)
print(best_fitness)
print("--- %s seconds ---" % (time.time() - start_time))

####################################
print("NN-digits")
data = load_digits()

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, \
                                                    test_size = 0.2, random_state = 3)

# Normalize feature data
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# One hot encode target values
one_hot = OneHotEncoder()

y_train_hot = one_hot.fit_transform(y_train.reshape(-1, 1)).todense()
y_test_hot = one_hot.transform(y_test.reshape(-1, 1)).todense()

# Initialize neural network object and fit object


def neural(hn,lr,ma):

    print("random hill")
    start_time = time.time()

    nn_model2 = mlrose.NeuralNetwork(hidden_nodes = [hn], activation = 'relu', \
                                     algorithm = 'random_hill_climb', max_iters = ma, \
                                     bias = True, is_classifier = True, learning_rate = lr, \
                                     early_stopping = True, clip_max = 5, max_attempts = 100, \
                                     random_state = 3)

    print(nn_model2.fit(X_train_scaled, y_train_hot))

    # Predict labels for train set and assess accuracy
    y_train_pred = nn_model2.predict(X_train_scaled)

    y_train_accuracy = accuracy_score(y_train_hot, y_train_pred)

    print(y_train_accuracy)

    # Predict labels for test set and assess accuracy
    y_test_pred = nn_model2.predict(X_test_scaled)

    y_test_accuracy = accuracy_score(y_test_hot, y_test_pred)

    print(y_test_accuracy)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()


    # Initialize neural network object and fit object
    nn_model1 = mlrose.NeuralNetwork(hidden_nodes = [hn], activation = 'relu', \
                                     algorithm = 'simulated_annealing', max_iters = ma, \
                                     bias = True, is_classifier = True, learning_rate = lr, \
                                     early_stopping = True, clip_max = 5, max_attempts = 100, \
                                     random_state = 3)

    print(nn_model1.fit(X_train_scaled, y_train_hot))

    # Predict labels for train set and assess accuracy
    y_train_pred = nn_model1.predict(X_train_scaled)

    y_train_accuracy = accuracy_score(y_train_hot, y_train_pred)
    print("simulated")
    print(y_train_accuracy)

    # Predict labels for test set and assess accuracy
    y_test_pred = nn_model1.predict(X_test_scaled)

    y_test_accuracy = accuracy_score(y_test_hot, y_test_pred)

    print(y_test_accuracy)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # Initialize neural network object and fit object
    nn_model = mlrose.NeuralNetwork(hidden_nodes = [hn], activation = 'relu', \
                                     algorithm = 'genetic_alg', max_iters = ma, \
                                     bias = True, is_classifier = True, learning_rate = lr, \
                                     early_stopping = True, clip_max = 5, max_attempts = 100, \
                                     random_state = 3)

    print(nn_model.fit(X_train_scaled, y_train_hot))
    print("genetic")
    # Predict labels for train set and assess accuracy
    y_train_pred = nn_model.predict(X_train_scaled)

    y_train_accuracy = accuracy_score(y_train_hot, y_train_pred)

    print(y_train_accuracy)

    # Predict labels for test set and assess accuracy
    y_test_pred = nn_model.predict(X_test_scaled)

    y_test_accuracy = accuracy_score(y_test_hot, y_test_pred)

    print(y_test_accuracy)
    print("--- %s seconds ---" % (time.time() - start_time))

print("2,0001,100")
neural(2,0.0001,100)
print("2,0001,1000")

neural(2,0.0001,1000)
print("2,01,100")

neural(2,0.01,100)
print("2,01,1000")

neural(2,0.01,1000)
print("50,0001,100")

neural(50,0.0001,100)
print("50,0001,1000")

neural(50,0.0001,1000)
print("50,01,100")

neural(50,0.01,100)
print("50,01,100")

# neural(50,0.01,1000)

neural(100,0.01,1000)
neural(100,0.01,10000)
