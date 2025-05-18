from sqlalchemy import (
    Column, Integer, String, Text, DateTime,
    ForeignKey, Table, Numeric, func
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Tabla de asociación para la relación muchos-a-muchos
dispositivo_grupo = Table(
    'dispositivo_grupo_association',
    Base.metadata,
    Column('dispositivo_id', Integer, ForeignKey('dispositivo.id'), primary_key=True),
    Column('grupo_id', Integer, ForeignKey('grupo_dispositivos.id'), primary_key=True)
)

class TipoDispositivo(Base):
    __tablename__ = 'tipo_dispositivo'

    id = Column(Integer, primary_key=True)
    fabricante = Column(String, nullable=False)
    modelo = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)

    # Un TipoDispositivo puede tener muchos Dispositivos
    dispositivos = relationship('Dispositivo', back_populates='tipo_dispositivo')

class GrupoDispositivos(Base):
    __tablename__ = 'grupo_dispositivos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    descripcion = Column(Text)

    # Un GrupoDispositivos puede agrupar muchos Dispositivos
    dispositivos = relationship(
        'Dispositivo',
        secondary=dispositivo_grupo,
        back_populates='grupos'
    )

class Dispositivo(Base):
    __tablename__ = 'dispositivo'

    id = Column(Integer, primary_key=True)
    numero_serie = Column(String, unique=True, nullable=False)
    mac_address = Column(String, unique=True)
    version_firmware = Column(String, nullable=False)
    descripcion_ubicacion = Column(String, nullable=False)  #MODIFICACIÓN ADICIONAL SOLICITADA
    coordenadas_gps = Column(String, nullable=True)   #MODIFICACIÓN ADICIONAL SOLICITADA
    estado_actual = Column(String, nullable=True) #MODIFICACIÓN ADICIONAL SOLICITADA
    fecha_registro = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    tipo_dispositivo_id = Column(
        Integer,
        ForeignKey('tipo_dispositivo.id'),
        nullable=False
    )

    # Relaciones
    tipo_dispositivo = relationship('TipoDispositivo', back_populates='dispositivos')
    sensores = relationship('Sensor', back_populates='dispositivo', cascade="all, delete-orphan")
    logs = relationship('LogEstadoDispositivo', back_populates='dispositivo', cascade="all, delete-orphan")
    grupos = relationship(
        'GrupoDispositivos',
        secondary=dispositivo_grupo,
        back_populates='dispositivos'
    )

class Sensor(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True)
    dispositivo_id = Column(Integer, ForeignKey('dispositivo.id'), nullable=False)
    tipo_sensor = Column(String, nullable=False)
    unidad_medida = Column(String, nullable=False)
    umblal_alerta = Column(float, nullable=False) #MODIFICACIÓN ADICIONAL SOLICITADA
    # Relaciones
    dispositivo = relationship('Dispositivo', back_populates='sensores')
    lecturas = relationship('LecturaDato', back_populates='sensor', cascade="all, delete-orphan")

class LecturaDato(Base):
    __tablename__ = 'lectura_dato'

    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, ForeignKey('sensor.id'), nullable=False)
    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    valor_leido = Column(Numeric)

    # Relación
    sensor = relationship('Sensor', back_populates='lecturas')

class LogEstadoDispositivo(Base):
    __tablename__ = 'log_estado_dispositivo'

    id = Column(Integer, primary_key=True)
    dispositivo_id = Column(Integer, ForeignKey('dispositivo.id'), nullable=False)
    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    estado = Column(String, nullable=False)
    mensaje_opcional = Column(Text)

    # Relación
    dispositivo = relationship('Dispositivo', back_populates='logs')
