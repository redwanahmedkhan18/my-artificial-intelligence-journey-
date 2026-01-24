def calculate_metrics(*values, normalize=False, round_digits=2):
    if not values:
        raise ValueError("At least one numeric value is required")

    data = list(values)

    # Optional normalization
    if normalize:
        min_val = min(data)
        max_val = max(data)

        if max_val != min_val:
            data = list(map(
                lambda x: (x - min_val) / (max_val - min_val),
                data
            ))
        else:
            data = [0 for _ in data]  # all values same

    mean = sum(data) / len(data)

    return {
        "mean": round(mean, round_digits),
        "min": round(min(data), round_digits),
        "max": round(max(data), round_digits)
    }
print(calculate_metrics(10, 20, 30))
