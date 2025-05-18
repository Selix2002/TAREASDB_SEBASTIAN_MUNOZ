# example_usage.py

from database import SessionLocal
import crud
from models import Base

def delete_tables(db):
    # Eliminar todas las tablas
    Base.metadata.drop_all(db.bind)
    # Crear nuevamente las tablas
    #Base.metadata.create_all(db.bind)
def main():
    # Abrimos una sesión
    with SessionLocal() as db:

        # ——————————————————————————————————————————
        # Gestión de Tipos de Dispositivo
        # ——————————————————————————————————————————
        print("=== Tipos de Dispositivo ===")
        tipo1 = crud.create_tipo_dispositivo(db, fabricante="AcmeCorp", modelo="X100", descripcion="Sensor genérico")
        tipo2 = crud.create_tipo_dispositivo(db, fabricante="BetaTech", modelo="Z200")
        all_tipos = crud.get_all_tipos_dispositivo(db)
        for t in all_tipos:
            print(f"Tipo {t.id}: {t.fabricante} {t.modelo} ({t.descripcion})")

        # ——————————————————————————————————————————
        # Gestión de Grupos de Dispositivos
        # ——————————————————————————————————————————
        print("\n=== Grupos de Dispositivos ===")
        grupoA = crud.create_grupo_dispositivo(db, nombre="Laboratorio", descripcion="Equipo de laboratorio")
        grupoB = crud.create_grupo_dispositivo(db, nombre="Campo", descripcion="Equipos de campo")
        all_grupos = crud.get_all_grupos_dispositivo(db)
        for g in all_grupos:
            print(f"Grupo {g.id}: {g.nombre} ({g.descripcion})")

        # ——————————————————————————————————————————
        # Gestión de Dispositivos
        # ——————————————————————————————————————————
        print("\n=== Dispositivos ===")
        disp1 = crud.create_dispositivo(
            db,
            numero_serie="SN-001",
            mac_address="AA:BB:CC:DD:EE:01",
            version_firmware="v1.0",
            ubicacion="Sala 1",
            tipo_dispositivo_id=tipo1.id
        )
        disp2 = crud.create_dispositivo(
            db,
            numero_serie="SN-002",
            mac_address="AA:BB:CC:DD:EE:02",
            version_firmware="v1.2",
            ubicacion="Sala 2",
            tipo_dispositivo_id=tipo2.id
        )

        # Listado general
        print("Todos los dispositivos:", [d.numero_serie for d in crud.get_all_dispositivos(db)])
        # Filtros por tipo
        print("Por tipo X100:", [d.numero_serie for d in crud.get_dispositivos_by_tipo(db, tipo1.id)])
        print("Por tipo Z200:", [d.numero_serie for d in crud.get_dispositivos_by_tipo(db, tipo2.id)])

        # Asociar y desasociar grupos para disp1
        crud.associate_dispositivo_to_grupos(db, disp1.id, [grupoA.id, grupoB.id])
        print("Grupos de SN-001:", [g.nombre for g in crud.get_grupos_by_dispositivo(db, disp1.id)])
        crud.disassociate_dispositivo_from_grupo(db, disp1.id, grupoB.id)
        print("Después de quitar 'Campo' de SN-001:", [g.nombre for g in crud.get_grupos_by_dispositivo(db, disp1.id)])
        print("Dispositivos en 'Laboratorio':", [d.numero_serie for d in crud.get_dispositivos_by_grupo(db, grupoA.id)])

        # ——————————————————————————————————————————
        # Ejemplos usando disp2
        # ——————————————————————————————————————————
        print("\n=== Operaciones con SN-002 ===")
        # Asociar disp2 solo al grupo 'Campo'
        crud.associate_dispositivo_to_grupos(db, disp2.id, [grupoB.id])
        print("Grupos de SN-002:", [g.nombre for g in crud.get_grupos_by_dispositivo(db, disp2.id)])
        # Consultar dispositivos en cada grupo
        print("Dispositivos en 'Campo':", [d.numero_serie for d in crud.get_dispositivos_by_grupo(db, grupoB.id)])

        # ——————————————————————————————————————————
        # Gestión de Sensores
        # ——————————————————————————————————————————
        print("\n=== Sensores de SN-001 ===")
        sensor1 = crud.add_sensor_to_dispositivo(db, dispositivo_id=disp1.id, tipo_sensor="Temperatura", unidad_medida="°C")
        sensor2 = crud.add_sensor_to_dispositivo(db, dispositivo_id=disp1.id, tipo_sensor="Humedad", unidad_medida="%RH")
        print("Sensores SN-001:", [(s.id, s.tipo_sensor) for s in crud.get_sensores_by_dispositivo(db, disp1.id)])

        print("\n=== Sensores de SN-002 ===")
        sensor3 = crud.add_sensor_to_dispositivo(db, dispositivo_id=disp2.id, tipo_sensor="Presión", unidad_medida="kPa")
        print("Sensores SN-002:", [(s.id, s.tipo_sensor) for s in crud.get_sensores_by_dispositivo(db, disp2.id)])

        # ——————————————————————————————————————————
        # Gestión de Lecturas de Datos
        # ——————————————————————————————————————————
        print("\n=== Lecturas de Datos SN-001 (Temperatura) ===")
        for valor in [22.5, 23.0, 22.8]:
            crud.create_lectura_dato(db, sensor_id=sensor1.id, valor_leido=valor)
        ultimas1 = crud.get_last_lecturas_by_sensor(db, sensor_id=sensor1.id, limit=2)
        print("Últimas lecturas SN-001: Temperatura:",[(l.valor_leido, l.timestamp.strftime("%Y-%m-%d %H:%M:%S"))for l in ultimas1])

        print("\n=== Lecturas de Datos SN-002 (Presión) ===")
        crud.create_lectura_dato(db, sensor_id=sensor3.id, valor_leido=101.3)
        ultimas2 = crud.get_last_lecturas_by_sensor(db, sensor_id=sensor3.id, limit=1)
        print("Últimas lecturas SN-002: Presión:", [(l.valor_leido, l.timestamp.strftime("%Y-%m-%d %H:%M:%S")) for l in ultimas2])
                                                                               
        # ——————————————————————————————————————————
        # Gestión de Logs de Estado
        # ——————————————————————————————————————————
        print("\n=== Logs de Estado SN-001 ===")
        crud.create_log_estado_dispositivo(db, dispositivo_id=disp1.id, estado="ONLINE", mensaje_opcional="Arrancó correctamente")
        crud.create_log_estado_dispositivo(db, dispositivo_id=disp1.id, estado="ERROR", mensaje_opcional="Fallo de comunicación")
        logs1 = crud.get_logs_estado_by_dispositivo(db, dispositivo_id=disp1.id)
        print("Historial SN-001:",[(log.estado, log.timestamp.strftime("%Y-%m-%d %H:%M:%S")) for log in logs1])

        print("\n=== Logs de Estado SN-002 ===")
        crud.create_log_estado_dispositivo(db, dispositivo_id=disp2.id, estado="OFFLINE", mensaje_opcional="Apagado manualmente")
        logs2 = crud.get_logs_estado_by_dispositivo(db, dispositivo_id=disp2.id)
        print("Historial SN-002:", [(log.estado, log.timestamp.strftime("%Y-%m-%d %H:%M:%S")) for log in logs2])

if __name__ == "__main__":
    #main()
    delete_tables(SessionLocal())
