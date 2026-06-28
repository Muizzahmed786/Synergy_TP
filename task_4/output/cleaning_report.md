# Task 4: Messy CSV Data Cleaning Report

    ## 1. Removal of duplicate values
    - duplicate entries were detected for student `S005 (Rohan)`.
    - duplicate rows were dropped using the`.drop_duplicates()` filter.

    ## 2. Categorical Value Standardization
    - Inconsistent text naming identified in the `domain` field (`ml`, `ML`, `MACHINE LEARNING`, `Web Dev`, `web`, `web development`).
    - Domain values were made consistent through mapping : `ML`, `Web`, `Electronics`, `Mechanical`.

    ## 3. Unit Normalization
    - Meters were normalized to centimeters, and the header was renamed to `height_cm`.
    - The text unit string `kg` was removed, and converted to float values, and the header was renamed to `weight_kg`.

    ## 5. Out-of-Bounds Boundary Rectification
    - attendance percentage were out of bounds for Dev with `-10` and Naina with `105%`.
    - attendance was capped between `[0, 100]`. Negative values were set to 0 and 100 exceeding values wet set to 100.