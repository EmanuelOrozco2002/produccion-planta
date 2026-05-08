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

CREATE TABLE corte_laser_detalle (
	id SERIAL PRIMARY KEY,
	registro_produccion_id INTEGER UNIQUE NOT NULL,
	cantidad_lamina DECIMAL(10,2),
	minutor_corte INTEGER,

	CONSTRAINT fk_registro_corte
		FOREIGN KEY(registro_produccion_id)
		REFERENCES registros_produccion(id)
);

CREATE TABLE pintura_detalle (
    id SERIAL PRIMARY KEY,

    registro_produccion_id INTEGER UNIQUE NOT NULL,

    color VARCHAR(50),

    CONSTRAINT fk_registro_pintura
        FOREIGN KEY(registro_produccion_id)
        REFERENCES registros_produccion(id)
);

