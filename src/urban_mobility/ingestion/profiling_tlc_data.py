from pathlib import Path

import pandas as pd


SOURCE_FILE = Path(
    "data",
    "bronze",
    "yellow_taxi",
    "year=2009",
    "month=01",
    "source.parquet",
)


def profile_dataset(file_path: Path) -> None:
    print(f"Reading: {file_path}")

    df = pd.read_parquet(file_path)

    print("\n=== DATASET SIZE ===")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

    print("\n=== COLUMNS ===")
    for column in df.columns:
        print(column)

    print("\n=== DATA TYPES ===")
    print(df.dtypes)

    print("\n=== MISSING VALUES ===")
    missing = df.isna().sum()
    missing_percentage = (missing / len(df) * 100).round(2)

    missing_report = pd.DataFrame(
        {
            "missing_count": missing,
            "missing_percentage": missing_percentage,
        }
    )

    print(missing_report[missing_report["missing_count"] > 0])

    print("\n=== DUPLICATES ===")
    print(f"Duplicate rows: {df.duplicated().sum():,}")

    print("\n=== UNIQUE SOURCE VALUES ===")

    for column in [
        "vendor_name",
        "Payment_Type",
        "Rate_Code",
        "store_and_forward",
    ]:
        if column in df.columns:
            print(f"\n{column}:")
            print(df[column].value_counts(dropna=False).head(20))

    print("\n=== DATETIME ANALYSIS ===")

    df["pickup_datetime"] = pd.to_datetime(
        df["Trip_Pickup_DateTime"],
        errors="coerce",
    )

    df["dropoff_datetime"] = pd.to_datetime(
        df["Trip_Dropoff_DateTime"],
        errors="coerce",
    )

    print(
        "Invalid pickup timestamps:",
        df["pickup_datetime"].isna().sum(),
    )

    print(
        "Invalid dropoff timestamps:",
        df["dropoff_datetime"].isna().sum(),
    )

    print("Earliest pickup:", df["pickup_datetime"].min())
    print("Latest pickup:", df["pickup_datetime"].max())

    df["trip_duration_minutes"] = (
        df["dropoff_datetime"] - df["pickup_datetime"]
    ).dt.total_seconds() / 60

    print("\n=== TRIP DURATION ===")
    print(df["trip_duration_minutes"].describe())

    print(
        "Negative durations:",
        (df["trip_duration_minutes"] < 0).sum(),
    )

    print(
        "Zero-minute trips:",
        (df["trip_duration_minutes"] == 0).sum(),
    )

    print("\n=== DISTANCE AND FARE CHECKS ===")

    checks = {
        "negative_distance": (df["Trip_Distance"] < 0).sum(),
        "zero_distance": (df["Trip_Distance"] == 0).sum(),
        "negative_fare": (df["Fare_Amt"] < 0).sum(),
        "negative_tip": (df["Tip_Amt"] < 0).sum(),
        "negative_tolls": (df["Tolls_Amt"] < 0).sum(),
        "negative_total": (df["Total_Amt"] < 0).sum(),
        "zero_total": (df["Total_Amt"] == 0).sum(),
    }

    for check_name, count in checks.items():
        print(f"{check_name}: {count:,}")

    print("\n=== COORDINATE CHECKS ===")

    print(
        "Invalid pickup longitude:",
        ((df["Start_Lon"] < -180) | (df["Start_Lon"] > 180)).sum(),
    )

    print(
        "Invalid pickup latitude:",
        ((df["Start_Lat"] < -90) | (df["Start_Lat"] > 90)).sum(),
    )

    print(
        "Invalid dropoff longitude:",
        ((df["End_Lon"] < -180) | (df["End_Lon"] > 180)).sum(),
    )

    print(
        "Invalid dropoff latitude:",
        ((df["End_Lat"] < -90) | (df["End_Lat"] > 90)).sum(),
    )

    print("\n=== NUMERIC SUMMARY ===")
    numeric_columns = [
        "Passenger_Count",
        "Trip_Distance",
        "Fare_Amt",
        "surcharge",
        "mta_tax",
        "Tip_Amt",
        "Tolls_Amt",
        "Total_Amt",
    ]

    print(df[numeric_columns].describe().transpose())

    print("\n=== SAMPLE RECORDS ===")
    print(df.head())


if __name__ == "__main__":
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(
            f"Source file was not found: {SOURCE_FILE}"
        )

    profile_dataset(SOURCE_FILE)