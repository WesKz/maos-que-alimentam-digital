from datetime import date


def mes_referencia(data: date) -> str:
    return f"{data.year:04d}-{data.month:02d}"


def ja_recebeu_no_mes(datas_entregas: list[date], data: date) -> date | None:
    """Retorna a data da última cesta regular no mesmo mês, ou None."""
    mes = mes_referencia(data)
    do_mes = [d for d in datas_entregas if mes_referencia(d) == mes]
    return max(do_mes) if do_mes else None
