from datetime import date

from app.services import ja_recebeu_no_mes, mes_referencia


def test_mes_referencia_formata_ano_e_mes():
    assert mes_referencia(date(2026, 11, 3)) == "2026-11"


def test_sem_entregas_pode_registrar():
    assert ja_recebeu_no_mes([], date(2026, 11, 16)) is None


def test_entrega_no_mesmo_mes_bloqueia():
    assert ja_recebeu_no_mes([date(2026, 11, 3)], date(2026, 11, 16)) == date(2026, 11, 3)


def test_entrega_em_mes_anterior_nao_bloqueia():
    assert ja_recebeu_no_mes([date(2026, 10, 3)], date(2026, 11, 16)) is None
