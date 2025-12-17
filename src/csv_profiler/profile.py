def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"rows": 0, "columns": [], "notes": ["Empty dataset"]}

    columns = list(rows[0].keys())
    missing = {c: 0 for c in columns}
    non_empty = {c: 0 for c in columns}
    dtype = {}
    stats: dict[str, dict] = {}

    # حساب missing و non_empty
    for row in rows:
        for c in columns:
            v = (row.get(c) or "").strip()
            if v == "":
                missing[c] += 1
            else:
                non_empty[c] += 1

    # تحديد نوع البيانات وحساب الإحصائيات
    for c in columns:
        values = [row[c] for row in rows]
        try:
            s = numeric_stats(values)
            dtype[c] = "numeric"
        except ValueError:
            s = text_stats(values)
            dtype[c] = "text"
        stats[c] = s

    return {
        "rows": len(rows),
        "n_cols": len(columns),
        "columns": columns,
        "missing": missing,
        "non_empty": non_empty,
        "dtype": dtype,
        "stats": stats
    }


def numeric_stats(values: list[str]) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    nums: list[float] = []
    for v in usable:
        x = try_float(v)
        if x is None:
            raise ValueError(f"Non-numeric value found: {v!r}")
        nums.append(x)

    count = len(nums)
    unique = len(set(nums))
    nums_sorted = sorted(nums)

    # حساب median بدقة للأعداد الزوجية والفردية
    if count:
        mid = count // 2
        if count % 2 == 0:
            median_val = (nums_sorted[mid - 1] + nums_sorted[mid]) / 2
        else:
            median_val = nums_sorted[mid]
    else:
        median_val = None

    return {
        "count": count,
        "unique": unique,
        "missing": missing,
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
        "mean": sum(nums)/count if count else None,
        "median": median_val
    }

def is_missing(value: str | None) -> bool:
    missing = ["", "na", "n/a", "null", "none", "nan"]
    return value is None or str(value).strip().lower() in missing

def try_float(value: str):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def text_stats(values: list[str], top_k: int = 5) -> dict:
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)

    counts: dict[str, int] = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1

    # ترتيب القيم حسب التكرار
    top_items = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    top = [{"value": v, "count": c} for v, c in top_items[:top_k]]  # أعلى top_k قيم

    return {
        "count": len(usable),
        "missing": missing,
        "unique": len(counts),
        "top_values": top
    }
