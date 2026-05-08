CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE procesos (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL
);
CREATE TABLE ordenes_produccion (
    id SERIAL PRIMARY KEY,
    numero_op VARCHAR(50) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(30) DEFAULT 'Pendiente',
    fecha_inicio DATE,
    fecha_entrega DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE registros_produccion (
    id SERIAL PRIMARY KEY,

    op_id INTEGER NOT NULL,
    empleado_id INTEGER NOT NULL,
    proceso_id INTEGER NOT NULL,

    hora_inicio TIMESTAMP NOT NULL,
    hora_fin TIMESTAMP,

    observaciones TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_op
        FOREIGN KEY(op_id)
        REFERENCES ordenes_produccion(id),

    CONSTRAINT fk_empleado
        FOREIGN KEY(empleado_id)
        REFERENCES empleados(id),

    CONSTRAINT fk_proceso
        FOREIGN KEY(proceso_id)
        REFERENCES procesos(id)
);