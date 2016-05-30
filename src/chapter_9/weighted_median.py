def weighted_median(weights):
    weights.sort()

    weight_sum = 0

    for weight in weights:
        weight_sum += weight

        if weight_sum >= 0.5:
            return weight
