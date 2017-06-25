
if __name__ == "__main__":

    # Load data, split into training and validation
    total = 
    train, validation = 

    # determine all the reducuction and clustering algorithms
    reducers = []
    clusterers = []

    for reductionModel in reducers:
        # Find reduction
        reducer = reductionModel()
        reducer.fit(train)

        # Print Errors
        # print(reducer.trainError())
        # print(reducer.validationError())

        for clusterAlgorithm in clusterers:
            reducedTrain = reducer.transform(train)
            clusterer = clusterAlgorithm()
            clusterer.cluster(reducedTrain)

            # Print Errors
            # print(clusterer.trainError())
            # print(clusterer.validationError())
