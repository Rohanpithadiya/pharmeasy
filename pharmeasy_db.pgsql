--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: doctors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.doctors (
    id bigint NOT NULL,
    name text,
    org text,
    qulification text
);


ALTER TABLE public.doctors OWNER TO postgres;

--
-- Name: doctors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.doctors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.doctors_id_seq OWNER TO postgres;

--
-- Name: doctors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.doctors_id_seq OWNED BY public.doctors.id;


--
-- Name: medical_records; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medical_records (
    patient_id bigint,
    doctor_id bigint,
    prescription_id bigint,
    updated_at bigint
);


ALTER TABLE public.medical_records OWNER TO postgres;

--
-- Name: patients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patients (
    id bigint NOT NULL,
    name text,
    dob bigint,
    address text,
    mr_permission jsonb
);


ALTER TABLE public.patients OWNER TO postgres;

--
-- Name: patients_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patients_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_id_seq OWNER TO postgres;

--
-- Name: patients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.patients_id_seq OWNED BY public.patients.id;


--
-- Name: permission_requests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permission_requests (
    patient_id bigint,
    requester_id bigint,
    requester_type text,
    doc_type text
);


ALTER TABLE public.permission_requests OWNER TO postgres;

--
-- Name: permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.permissions (
    patient_id bigint,
    requester_id bigint,
    prescription_id bigint,
    requester_type text,
    ttl bigint
);


ALTER TABLE public.permissions OWNER TO postgres;

--
-- Name: pharmacists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pharmacists (
    id bigint NOT NULL,
    org_name text,
    licence text,
    address text
);


ALTER TABLE public.pharmacists OWNER TO postgres;

--
-- Name: pharmacists_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pharmacists_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pharmacists_id_seq OWNER TO postgres;

--
-- Name: pharmacists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pharmacists_id_seq OWNED BY public.pharmacists.id;


--
-- Name: prescriptions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prescriptions (
    id bigint NOT NULL,
    type text,
    meta text
);


ALTER TABLE public.prescriptions OWNER TO postgres;

--
-- Name: prescriptions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prescriptions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prescriptions_id_seq OWNER TO postgres;

--
-- Name: prescriptions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prescriptions_id_seq OWNED BY public.prescriptions.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctors ALTER COLUMN id SET DEFAULT nextval('public.doctors_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients ALTER COLUMN id SET DEFAULT nextval('public.patients_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pharmacists ALTER COLUMN id SET DEFAULT nextval('public.pharmacists_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prescriptions ALTER COLUMN id SET DEFAULT nextval('public.prescriptions_id_seq'::regclass);


--
-- Data for Name: doctors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.doctors (id, name, org, qulification) FROM stdin;
1	Umaprasad	Dictum Eu Eleifend Inc.	MBBS
2	Yashpal	Congue Incorporated	MD
3	Janak	Aliquam Eros Industries	MBBS
4	Timirbaran	Tempor Corp.	MBBS
5	Sohan	Laoreet Associates	MBBS
6	Jenya	Sagittis Augue Eu Inc.	MD
7	Sameena	Iaculis Inc.	MD
8	Sarbani	Ipsum Suspendisse Sagittis Corporation	MD
9	Devahuti	Vel Corporation	MBBS
10	Trigun	Suspendisse Corporation	MD
\.


--
-- Name: doctors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.doctors_id_seq', 10, true);


--
-- Data for Name: medical_records; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medical_records (patient_id, doctor_id, prescription_id, updated_at) FROM stdin;
3	4	1	1534188919000
3	3	2	1534275526000
1	1	1	1534188919000
1	2	2	1534188919000
\.


--
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patients (id, name, dob, address, mr_permission) FROM stdin;
4	Josiah	1503382844	Renlies	\N
5	Oscar	1504194063	San Lorenzo Nuovo	\N
6	Jillian	1503194479	Aliano	\N
7	Emi	1504102857	Darion	\N
8	Deanna	1503134106	St. Pölten	\N
9	Donna	1503222384	Kakisa	\N
10	Elijah	1502871648	Leerbeek	\N
3	Merrill	1504216110	Borghetto di Borbera	{"doc_list": {"4": {"ttl": 1534278486000}, "5": {"ttl": 1534278400000}}}
1	Rinah	1503447303	Lowell	\N
2	Imani	1503365369	Tarbes	\N
\.


--
-- Name: patients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patients_id_seq', 10, true);


--
-- Data for Name: permission_requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permission_requests (patient_id, requester_id, requester_type, doc_type) FROM stdin;
1	1	DR	PR
1	1	PH	PR
\.


--
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.permissions (patient_id, requester_id, prescription_id, requester_type, ttl) FROM stdin;
1	1	1	DR	\N
1	1	1	DR	\N
\.


--
-- Data for Name: pharmacists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pharmacists (id, org_name, licence, address) FROM stdin;
1	Imperdiet Ullamcorper Industries	FDD78F6C-5E8C-C35A-6631-DF463419D2C8	3127 Et Rd.
2	Egestas Urna Justo Foundation	F60D5446-1B87-66C6-71A8-D8C55A7641F7	155-1171 A, Rd.
3	Fringilla Mi Company	90D78892-4A9D-B06D-341D-22C93A1058F6	P.O. Box 337, 6231 Justo Rd.
4	Congue Turpis In Limited	2C182B97-67E8-7217-5AA1-173B7E3F7A8D	Ap #444-1660 Turpis Avenue
5	Dui Nec Consulting	036208E1-733A-89D2-620D-B98D440FF1EC	597-4882 Risus. Av.
6	Erat In Corp.	0C09A23B-AB82-EACA-CA94-7034B1BADA0D	Ap #280-7996 Dolor. Rd.
7	Dictum Associates	423C600E-4165-2C32-77A1-501424D40244	6462 Volutpat Ave
8	Auctor Nunc Limited	8A166609-EE98-CBCD-0B32-FDA110AB1E24	236-9510 Dictum Street
9	Nunc Mauris Associates	D1F8E391-A3F3-B2EF-02E2-1F3725D8F459	890-9347 Sem, Rd.
10	Auctor Velit PC	030052B9-AD22-45A0-6FF6-7C0A0FDA30D3	P.O. Box 390, 3775 Auctor St.
\.


--
-- Name: pharmacists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pharmacists_id_seq', 10, true);


--
-- Data for Name: prescriptions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.prescriptions (id, type, meta) FROM stdin;
2	image	http://somes3url
1	text	abc 50mg, xyx.10mg, etc..
\.


--
-- Name: prescriptions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.prescriptions_id_seq', 2, true);


--
-- Name: doctors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (id);


--
-- Name: no_duplicate_tag; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permission_requests
    ADD CONSTRAINT no_duplicate_tag UNIQUE (requester_id, patient_id, requester_type, doc_type);


--
-- Name: patients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (id);


--
-- Name: pharmacists_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pharmacists
    ADD CONSTRAINT pharmacists_pkey PRIMARY KEY (id);


--
-- Name: prescriptions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prescriptions
    ADD CONSTRAINT prescriptions_pkey PRIMARY KEY (id);


--
-- Name: medical_records_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_records
    ADD CONSTRAINT medical_records_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(id) ON DELETE CASCADE;


--
-- Name: medical_records_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_records
    ADD CONSTRAINT medical_records_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(id) ON DELETE CASCADE;


--
-- Name: medical_records_prescription_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_records
    ADD CONSTRAINT medical_records_prescription_id_fkey FOREIGN KEY (prescription_id) REFERENCES public.prescriptions(id) ON DELETE CASCADE;


--
-- Name: permission_requests_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permission_requests
    ADD CONSTRAINT permission_requests_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(id) ON DELETE CASCADE;


--
-- Name: permissions_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(id) ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

