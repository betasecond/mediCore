// src/types/api.ts
export interface QueryParams {
    page?: number;
    page_size?: number;
    ordering?: string;
    search?: string;
}
export interface BaseResponse<T> {
    code: number;
    message: string;
    data: T;
}

export interface BaseInfo {
    id: number;
    case_id: string;
    name: string;
    name_code: string;
    category: string;
    category_code: string;
    type: string;
    type_code: string;
    value: string;
}

export interface Cases {
    id: number;
    case_id: string;
    identity_id: string;
    inhospital_id?: string;
}

export interface ClinicalInfo {
    id: number;
    name: string;
    name_code: string;
    case_id: string;
}

export interface DataTable {
    id: number;
    case_id: number;
    table_name: string;
    data_template_id: number;
}

export interface ExaminationSheet {
    id: number;
    data_table_id: number;
    case_id?: number;
    name: string;
    name_code: string;
    category: string;
    category_code: string;
    diagnosis: string;
    description?: string;
    exam_date: string;
    inspector?: string;
}

export interface ArchiveCaseRelative {
    id: number;
    archive_id: string;
    case_id: string;
}

export interface Archive {
    id: number;
    arcive_id: string;
    archive_name: string;
    description?: string | null;
}

export interface DocumentChart {
    id: number;
    document_id: number;
    chart_id: number;
    x: number;
    y: number;
    height: number;
    width: number;
}

export interface Documents {
    id: number;
    title: string;
    author?: string | null;
    description?: string | null;
    properties: string;
}

export interface ExaminationImages {
    id: number;
    examination_sheet_id: number;
    url: string;
    remark?: string | null;
}

export interface Identity {
    id: number;
    identity_id: string;
    true_name: string;
    gender: number;
    birth_date: string;  // Consider using Date if you're consistently parsing
}

export interface Image {
    id: number;
    document_id: number;
    url: string;
    remark?: string | null;
    x: number;
    y: number;
    height: number;
    width: number;
    is_stroke: number;
    stroke_weight: number;
    stroke_color: string;
}

export interface Shape {
    id: number;
    document_id: number;
    x: number;
    y: number;
    height: number;
    width: number;
    is_fill: number;
    fill_color: string;
    is_stroke: number;
    stroke_color: string;
    path: string;
}

export interface TestingSheet {
    id: number;
    data_table_id: number;
    case_id?: number | null;
    name: string;
    name_code: string;
    name_eng: string;
    name_short: string;
    category: string;
    category_code: string;
    type: string;
    type_code: string;
    value: string;
    test_date: string; // Consider using Date
    inspector?: string | null;
}

export interface Text {
    id: number;
    document_id: number;
    x: number;
    y: number;
    height: number;
    width: number;
    family: string;
    size: number;
    color: string;
    weight: number;
    underline: number;
    slope: number;
}
