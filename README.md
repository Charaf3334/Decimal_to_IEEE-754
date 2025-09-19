# IEEE-754 Converter

Convert numbers between decimal and IEEE-754 32-bit floating-point representation.

## Description

This repo contains two python scripts:

- `script.py` — Converts decimal numbers to IEEE-754 32-bit binary.
- `to_decimal.py` — Converts IEEE-754 32-bit binary strings back to decimal.

It allows you to see how floating-point numbers are stored in your computer and supports multiple numbers at once.

## Usage

### 1. Convert Decimal to IEEE-754 Binary

```bash
python script.py "13.37" "0.5" "-42.0"
```

### 2. Convert IEEE-754 Binary to Decimal

```bash
python to_decimal.py "01000100101001110011000000000000"
```
