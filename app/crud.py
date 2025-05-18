from database import SessionLocal
# crud.py
from sqlalchemy.orm import Session
from models import (
    TipoDispositivo,
    GrupoDispositivos,
    Dispositivo,
    Sensor,
    LecturaDato,
    LogEstadoDispositivo,
    dispositivo_grupo
)

# ————————————————————————————————
# Gestión de Tipos de Dispositivo
# ————————————————————————————————

def create_tipo_dispositivo(db: Session, fabricante: str, modelo: str, descripcion: str = None) -> TipoDispositivo:
    nuevo = TipoDispositivo(fabricante=fabricante, modelo=modelo, descripcion=descripcion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_all_tipos_dispositivo(db: Session) -> list[TipoDispositivo]:
    return db.query(TipoDispositivo).all()

# ————————————————————————————————
# Gestión de Grupos de Dispositivos
# ————————————————————————————————

def create_grupo_dispositivo(db: Session, nombre: str, descripcion: str = None) -> GrupoDispositivos:
    nuevo = GrupoDispositivos(nombre=nombre, descripcion=descripcion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_all_grupos_dispositivo(db: Session) -> list[GrupoDispositivos]:
    return db.query(GrupoDispositivos).all()

# ————————————————————————————————
# Gestión de Dispositivos
# ————————————————————————————————

def create_dispositivo(db: Session,numero_serie: str,mac_address: str,version_firmware: str,ubicacion: str,tipo_dispositivo_id: int) -> Dispositivo:
    nuevo = Dispositivo(numero_serie=numero_serie,mac_address=mac_address,version_firmware=version_firmware,ubicacion=ubicacion,tipo_dispositivo_id=tipo_dispositivo_id)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_all_dispositivos(db: Session) -> list[Dispositivo]:
    return db.query(Dispositivo).all()

def get_dispositivos_by_tipo(db: Session, tipo_id: int) -> list[Dispositivo]:
    return (
        db.query(Dispositivo)
        .filter(Dispositivo.tipo_dispositivo_id == tipo_id)
        .all()
    )

def get_dispositivos_by_grupo(db: Session, grupo_id: int) -> list[Dispositivo]:
    return (
        db.query(Dispositivo)
        .join(dispositivo_grupo)
        .filter(dispositivo_grupo.c.grupo_id == grupo_id)
        .all()
    )

def get_grupos_by_dispositivo(db: Session, dispositivo_id: int) -> list[GrupoDispositivos]:
    disp = db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()
    return disp.grupos if disp else []

def associate_dispositivo_to_grupos(
    db: Session,
    dispositivo_id: int,
    grupo_ids: list[int]
) -> Dispositivo | None:
    disp = db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()
    if not disp:
        return None
    grupos = db.query(GrupoDispositivos).filter(GrupoDispositivos.id.in_(grupo_ids)).all()
    disp.grupos.extend(grupos)
    db.commit()
    db.refresh(disp)
    return disp

def disassociate_dispositivo_from_grupo(
    db: Session,
    dispositivo_id: int,
    grupo_id: int
) -> Dispositivo | None:
    disp = db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()
    if not disp:
        return None
    disp.grupos = [g for g in disp.grupos if g.id != grupo_id]
    db.commit()
    db.refresh(disp)
    return disp

# ————————————————————————————————
# Gestión de Sensores
# ————————————————————————————————

def add_sensor_to_dispositivo(
    db: Session,
    dispositivo_id: int,
    tipo_sensor: str,
    unidad_medida: str
) -> Sensor | None:
    disp = db.query(Dispositivo).filter(Dispositivo.id == dispositivo_id).first()
    if not disp:
        return None
    sensor = Sensor(dispositivo_id=dispositivo_id, tipo_sensor=tipo_sensor, unidad_medida=unidad_medida)
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor

def get_sensores_by_dispositivo(db: Session, dispositivo_id: int) -> list[Sensor]:
    return (
        db.query(Sensor)
        .filter(Sensor.dispositivo_id == dispositivo_id)
        .all()
    )

# ————————————————————————————————
# Gestión de Lecturas de Datos
# ————————————————————————————————

def create_lectura_dato(
    db: Session,
    sensor_id: int,
    valor_leido
) -> LecturaDato:
    lectura = LecturaDato(sensor_id=sensor_id, valor_leido=valor_leido)
    db.add(lectura)
    db.commit()
    db.refresh(lectura)
    return lectura

def get_last_lecturas_by_sensor(
    db: Session,
    sensor_id: int,
    limit: int = 10
) -> list[LecturaDato]:
    return (
        db.query(LecturaDato)
        .filter(LecturaDato.sensor_id == sensor_id)
        .order_by(LecturaDato.timestamp.desc())
        .limit(limit)
        .all()
    )

# ————————————————————————————————
# Gestión de Logs de Estado
# ————————————————————————————————

def create_log_estado_dispositivo(
    db: Session,
    dispositivo_id: int,
    estado: str,
    mensaje_opcional: str = None
) -> LogEstadoDispositivo:
    log = LogEstadoDispositivo(
        dispositivo_id=dispositivo_id,
        estado=estado,
        mensaje_opcional=mensaje_opcional
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_logs_estado_by_dispositivo(
    db: Session,
    dispositivo_id: int
) -> list[LogEstadoDispositivo]:
    return (
        db.query(LogEstadoDispositivo)
        .filter(LogEstadoDispositivo.dispositivo_id == dispositivo_id)
        .order_by(LogEstadoDispositivo.timestamp.desc())
        .all()
    )
