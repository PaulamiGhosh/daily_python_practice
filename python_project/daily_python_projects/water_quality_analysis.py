import numpy as np
import pandas as pd

np.random.seed(24)

stations = ["Hooghly_A", "Hooghly_B", "Damodar_A", "Damodar_B", "Rupnarayan"]
months = pd.date_range("2025-01-01", "2025-08-01", freq="MS")

rows = []

for month in months:
    for station in stations:
        rows.append({
            "date": month,
            "station": station,
            "temperature": np.random.normal(27, 3),
            "dissolved_oxygen": np.random.normal(6, 1.2),
            "bod": np.random.normal(4, 1.5),
            "nitrate": np.random.normal(3.5, 1.5),
            "sampling_depth": np.random.uniform(0.5, 3.0)
        })

water = pd.DataFrame(rows)

# Introduce realistic missing measurements
missing_idx = np.random.choice(
    water.index,
    size=10,
    replace=False
)

water.loc[missing_idx, "dissolved_oxygen"] = np.nan
water.loc[
    np.random.choice(water.index, 6, replace=False),
    "nitrate"
] = np.nan

print(water)
