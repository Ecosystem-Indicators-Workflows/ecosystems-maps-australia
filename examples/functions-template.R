# Create a membership table in long format from a membership table in wide format
# parameters: 
# target: target class code or NULL for full matrix
# xref: crossreferencing table
# original_codes: columns with original class codes
# target_codes: columns with target class codes
# membership_value: membership columns

# 1) if target is not NULL: filter xref for any target_codes in target
# 2) pivot longer xref 

 library(dplyr)
 library(tidyr)


membership_table <- function(xref, original_names, target_names, membership_values, target=NULL) {
    if (!is.null(target)) {
       xref <-  filter(xref, 
        if_any(starts_with(target_names), ~ .x == target))
    }
    
    xref |>
        dplyr::select(
            all_of(original_names),
            starts_with(target_names),
            starts_with(membership_values)
        ) |> 
    tidyr::pivot_longer(
        c(starts_with(target_names),starts_with(membership_values)),
        cols_vary = "slowest",
        names_to = c(".value"),
        names_pattern = "([[:alpha:]]+)")
}

fake <- data.frame(
    re1 = c("A","B","C","N"),
    efg1 = c("T1.1", "T1.2", "T1.1", "T1.2"),
    memb1 = c(80,80,70,50),
    efg2 = c("T1.2", "T1.1", "T1.3", "T1.3"),
    memb2 = c(20,20,30,50)
)



membership_table(fake, "re1","efg","memb")

membership_table(fake, "re1","efg","memb","T1.1")


membership_table <- function(xref, original_names, target_names, membership_values, target=NULL) {
    if (!is.null(target)) {
       xref <-  filter(xref, 
        if_any(any_of(target_names), ~ .x == target))
    }
    
    xref |>
        dplyr::select(
            any_of(original_names),
            any_of(target_names),
            any_of(membership_values)
        ) |> 
    tidyr::pivot_longer(
        any_of(c(target_names,membership_values)),
        cols_vary = "slowest",
        names_to = c(".value"),
        names_pattern = "([[:alpha:]]+)")
}

membership_table(
    fake, 
    "re1",
    starts_with("efg"),
    starts_with("memb"),
    target="T1.3")


# this is challenging because column names have the same root, 
fake2 <- tibble(
    re1_raw = c("A","B","C","N"),
    GET1 = c("T1.1", "T1.2", "T1.1", "T1.2"),
    GET1p = c(80,80,70,50),
    GET2 = c("T1.2", "T1.1", "T1.3", "T1.3"),
    GET2p = c(20,20,30,50)
)


membership_table(
    fake2, 
    "re1_raw",
    c("GET1","GET2"),
    c("GET1p","GET2p"),
    target="T1.3")
