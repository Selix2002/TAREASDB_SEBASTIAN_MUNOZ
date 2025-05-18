--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4 (Debian 17.4-2)
-- Dumped by pg_dump version 17.4 (Debian 17.4-2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: dispositivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dispositivo (
    id integer NOT NULL,
    numero_serie character varying NOT NULL,
    mac_address character varying,
    version_firmware character varying NOT NULL,
    ubicacion character varying NOT NULL,
    fecha_registro timestamp with time zone DEFAULT now() NOT NULL,
    tipo_dispositivo_id integer NOT NULL
);


ALTER TABLE public.dispositivo OWNER TO postgres;

--
-- Name: dispositivo_grupo_association; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dispositivo_grupo_association (
    dispositivo_id integer NOT NULL,
    grupo_id integer NOT NULL
);


ALTER TABLE public.dispositivo_grupo_association OWNER TO postgres;

--
-- Name: dispositivo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dispositivo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.dispositivo_id_seq OWNER TO postgres;

--
-- Name: dispositivo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dispositivo_id_seq OWNED BY public.dispositivo.id;


--
-- Name: grupo_dispositivos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.grupo_dispositivos (
    id integer NOT NULL,
    nombre character varying NOT NULL,
    descripcion text
);


ALTER TABLE public.grupo_dispositivos OWNER TO postgres;

--
-- Name: grupo_dispositivos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.grupo_dispositivos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.grupo_dispositivos_id_seq OWNER TO postgres;

--
-- Name: grupo_dispositivos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.grupo_dispositivos_id_seq OWNED BY public.grupo_dispositivos.id;


--
-- Name: lectura_dato; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lectura_dato (
    id integer NOT NULL,
    sensor_id integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT now() NOT NULL,
    valor_leido numeric
);


ALTER TABLE public.lectura_dato OWNER TO postgres;

--
-- Name: lectura_dato_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lectura_dato_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.lectura_dato_id_seq OWNER TO postgres;

--
-- Name: lectura_dato_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lectura_dato_id_seq OWNED BY public.lectura_dato.id;


--
-- Name: log_estado_dispositivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.log_estado_dispositivo (
    id integer NOT NULL,
    dispositivo_id integer NOT NULL,
    "timestamp" timestamp with time zone DEFAULT now() NOT NULL,
    estado character varying NOT NULL,
    mensaje_opcional text
);


ALTER TABLE public.log_estado_dispositivo OWNER TO postgres;

--
-- Name: log_estado_dispositivo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.log_estado_dispositivo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.log_estado_dispositivo_id_seq OWNER TO postgres;

--
-- Name: log_estado_dispositivo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.log_estado_dispositivo_id_seq OWNED BY public.log_estado_dispositivo.id;


--
-- Name: sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensor (
    id integer NOT NULL,
    dispositivo_id integer NOT NULL,
    tipo_sensor character varying NOT NULL,
    unidad_medida character varying NOT NULL
);


ALTER TABLE public.sensor OWNER TO postgres;

--
-- Name: sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sensor_id_seq OWNER TO postgres;

--
-- Name: sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensor_id_seq OWNED BY public.sensor.id;


--
-- Name: tipo_dispositivo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_dispositivo (
    id integer NOT NULL,
    fabricante character varying NOT NULL,
    modelo character varying NOT NULL,
    descripcion text
);


ALTER TABLE public.tipo_dispositivo OWNER TO postgres;

--
-- Name: tipo_dispositivo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_dispositivo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tipo_dispositivo_id_seq OWNER TO postgres;

--
-- Name: tipo_dispositivo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_dispositivo_id_seq OWNED BY public.tipo_dispositivo.id;


--
-- Name: dispositivo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo ALTER COLUMN id SET DEFAULT nextval('public.dispositivo_id_seq'::regclass);


--
-- Name: grupo_dispositivos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_dispositivos ALTER COLUMN id SET DEFAULT nextval('public.grupo_dispositivos_id_seq'::regclass);


--
-- Name: lectura_dato id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lectura_dato ALTER COLUMN id SET DEFAULT nextval('public.lectura_dato_id_seq'::regclass);


--
-- Name: log_estado_dispositivo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.log_estado_dispositivo ALTER COLUMN id SET DEFAULT nextval('public.log_estado_dispositivo_id_seq'::regclass);


--
-- Name: sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor ALTER COLUMN id SET DEFAULT nextval('public.sensor_id_seq'::regclass);


--
-- Name: tipo_dispositivo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dispositivo ALTER COLUMN id SET DEFAULT nextval('public.tipo_dispositivo_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
87d09239bb04
\.


--
-- Data for Name: dispositivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dispositivo (id, numero_serie, mac_address, version_firmware, ubicacion, fecha_registro, tipo_dispositivo_id) FROM stdin;
\.


--
-- Data for Name: dispositivo_grupo_association; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dispositivo_grupo_association (dispositivo_id, grupo_id) FROM stdin;
\.


--
-- Data for Name: grupo_dispositivos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.grupo_dispositivos (id, nombre, descripcion) FROM stdin;
\.


--
-- Data for Name: lectura_dato; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lectura_dato (id, sensor_id, "timestamp", valor_leido) FROM stdin;
\.


--
-- Data for Name: log_estado_dispositivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.log_estado_dispositivo (id, dispositivo_id, "timestamp", estado, mensaje_opcional) FROM stdin;
\.


--
-- Data for Name: sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor (id, dispositivo_id, tipo_sensor, unidad_medida) FROM stdin;
\.


--
-- Data for Name: tipo_dispositivo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_dispositivo (id, fabricante, modelo, descripcion) FROM stdin;
\.


--
-- Name: dispositivo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dispositivo_id_seq', 1, false);


--
-- Name: grupo_dispositivos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.grupo_dispositivos_id_seq', 1, false);


--
-- Name: lectura_dato_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lectura_dato_id_seq', 1, false);


--
-- Name: log_estado_dispositivo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.log_estado_dispositivo_id_seq', 1, false);


--
-- Name: sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_id_seq', 1, false);


--
-- Name: tipo_dispositivo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_dispositivo_id_seq', 1, false);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: dispositivo_grupo_association dispositivo_grupo_association_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo_grupo_association
    ADD CONSTRAINT dispositivo_grupo_association_pkey PRIMARY KEY (dispositivo_id, grupo_id);


--
-- Name: dispositivo dispositivo_mac_address_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo
    ADD CONSTRAINT dispositivo_mac_address_key UNIQUE (mac_address);


--
-- Name: dispositivo dispositivo_numero_serie_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo
    ADD CONSTRAINT dispositivo_numero_serie_key UNIQUE (numero_serie);


--
-- Name: dispositivo dispositivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo
    ADD CONSTRAINT dispositivo_pkey PRIMARY KEY (id);


--
-- Name: grupo_dispositivos grupo_dispositivos_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_dispositivos
    ADD CONSTRAINT grupo_dispositivos_nombre_key UNIQUE (nombre);


--
-- Name: grupo_dispositivos grupo_dispositivos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.grupo_dispositivos
    ADD CONSTRAINT grupo_dispositivos_pkey PRIMARY KEY (id);


--
-- Name: lectura_dato lectura_dato_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lectura_dato
    ADD CONSTRAINT lectura_dato_pkey PRIMARY KEY (id);


--
-- Name: log_estado_dispositivo log_estado_dispositivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.log_estado_dispositivo
    ADD CONSTRAINT log_estado_dispositivo_pkey PRIMARY KEY (id);


--
-- Name: sensor sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_pkey PRIMARY KEY (id);


--
-- Name: tipo_dispositivo tipo_dispositivo_modelo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dispositivo
    ADD CONSTRAINT tipo_dispositivo_modelo_key UNIQUE (modelo);


--
-- Name: tipo_dispositivo tipo_dispositivo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_dispositivo
    ADD CONSTRAINT tipo_dispositivo_pkey PRIMARY KEY (id);


--
-- Name: dispositivo_grupo_association dispositivo_grupo_association_dispositivo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo_grupo_association
    ADD CONSTRAINT dispositivo_grupo_association_dispositivo_id_fkey FOREIGN KEY (dispositivo_id) REFERENCES public.dispositivo(id);


--
-- Name: dispositivo_grupo_association dispositivo_grupo_association_grupo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo_grupo_association
    ADD CONSTRAINT dispositivo_grupo_association_grupo_id_fkey FOREIGN KEY (grupo_id) REFERENCES public.grupo_dispositivos(id);


--
-- Name: dispositivo dispositivo_tipo_dispositivo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivo
    ADD CONSTRAINT dispositivo_tipo_dispositivo_id_fkey FOREIGN KEY (tipo_dispositivo_id) REFERENCES public.tipo_dispositivo(id);


--
-- Name: lectura_dato lectura_dato_sensor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lectura_dato
    ADD CONSTRAINT lectura_dato_sensor_id_fkey FOREIGN KEY (sensor_id) REFERENCES public.sensor(id);


--
-- Name: log_estado_dispositivo log_estado_dispositivo_dispositivo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.log_estado_dispositivo
    ADD CONSTRAINT log_estado_dispositivo_dispositivo_id_fkey FOREIGN KEY (dispositivo_id) REFERENCES public.dispositivo(id);


--
-- Name: sensor sensor_dispositivo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_dispositivo_id_fkey FOREIGN KEY (dispositivo_id) REFERENCES public.dispositivo(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

