import request from './request';
import type {
    BaseResponse,
    BaseInfo,
    Cases,
    DataTable,
    ExaminationSheet,
    QueryParams,
    ArchiveCaseRelative,
    Archive,
    ClinicalInfo,
    DocumentChart,
    Documents,
    ExaminationImages,
    Identity,
    Image,
    Shape,
    TestingSheet,
    Text
} from '@/types/api';

// --- Base Info API ---
export const baseInfoService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<BaseInfo[]>>('/base-info/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<BaseInfo>>(`/base-info/${id}/`);
    },

    create(data: Omit<BaseInfo, 'id' | 'created_at' | 'updated_at'>) {
        return request.post<BaseResponse<BaseInfo>>('/base-info/', data);
    },

    update(id: number, data: Partial<BaseInfo>) {
        return request.put<BaseResponse<BaseInfo>>(`/base-info/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<BaseInfo>) {
        return request.patch<BaseResponse<BaseInfo>>(`/base-info/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/base-info/${id}/`);
    }
};

// --- Cases API ---
export const casesService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Cases[]>>('/cases/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Cases>>(`/cases/${id}/`);
    },

    create(data: Omit<Cases, 'id' | 'created_at' | 'updated_at'>) {
        return request.post<BaseResponse<Cases>>('/cases/', data);
    },

    update(id: number, data: Partial<Cases>) {
        return request.put<BaseResponse<Cases>>(`/cases/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Cases>) {
        return request.patch<BaseResponse<Cases>>(`/cases/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/cases/${id}/`);
    }
};

// --- Data Tables API ---
export const dataTableService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<DataTable[]>>('/data-tables/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<DataTable>>(`/data-tables/${id}/`);
    },

    create(data: Omit<DataTable, 'id' | 'created_at' | 'updated_at'>) {
        return request.post<BaseResponse<DataTable>>('/data-tables/', data);
    },

    update(id: number, data: Partial<DataTable>) {
        return request.put<BaseResponse<DataTable>>(`/data-tables/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<DataTable>) {
        return request.patch<BaseResponse<DataTable>>(`/data-tables/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/data-tables/${id}/`);
    }
};

// --- Examination Sheets API ---
export const examinationSheetService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<ExaminationSheet[]>>('/examination-sheets/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<ExaminationSheet>>(`/examination-sheets/${id}/`);
    },

    create(data: Omit<ExaminationSheet, 'id' | 'created_at' | 'updated_at'>) {
        return request.post<BaseResponse<ExaminationSheet>>('/examination-sheets/', data);
    },

    update(id: number, data: Partial<ExaminationSheet>) {
        return request.put<BaseResponse<ExaminationSheet>>(`/examination-sheets/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<ExaminationSheet>) {
        return request.patch<BaseResponse<ExaminationSheet>>(`/examination-sheets/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/examination-sheets/${id}/`);
    }
};

// --- Archives API ---
export const archiveService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Archive[]>>('/archives/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Archive>>(`/archives/${id}/`);
    },

    create(data: Omit<Archive, 'id'>) {
        return request.post<BaseResponse<Archive>>('/archives/', data);
    },

    update(id: number, data: Partial<Archive>) {
        return request.put<BaseResponse<Archive>>(`/archives/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Archive>) {
        return request.patch<BaseResponse<Archive>>(`/archives/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/archives/${id}/`);
    }
};

// --- Archive Case Relatives API ---
export const archiveCaseRelativeService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<ArchiveCaseRelative[]>>('/archive-case-relatives/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<ArchiveCaseRelative>>(`/archive-case-relatives/${id}/`);
    },

    create(data: Omit<ArchiveCaseRelative, 'id'>) {
        return request.post<BaseResponse<ArchiveCaseRelative>>('/archive-case-relatives/', data);
    },

    update(id: number, data: Partial<ArchiveCaseRelative>) {
        return request.put<BaseResponse<ArchiveCaseRelative>>(`/archive-case-relatives/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<ArchiveCaseRelative>) {
        return request.patch<BaseResponse<ArchiveCaseRelative>>(`/archive-case-relatives/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/archive-case-relatives/${id}/`);
    }
};

// --- Clinical Info API ---
export const clinicalInfoService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<ClinicalInfo[]>>('/clinical-info/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<ClinicalInfo>>(`/clinical-info/${id}/`);
    },

    create(data: Omit<ClinicalInfo, 'id'>) {
        return request.post<BaseResponse<ClinicalInfo>>('/clinical-info/', data);
    },

    update(id: number, data: Partial<ClinicalInfo>) {
        return request.put<BaseResponse<ClinicalInfo>>(`/clinical-info/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<ClinicalInfo>) {
        return request.patch<BaseResponse<ClinicalInfo>>(`/clinical-info/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/clinical-info/${id}/`);
    }
};

// --- Document Charts API ---
export const documentChartService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<DocumentChart[]>>('/document-charts/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<DocumentChart>>(`/document-charts/${id}/`);
    },

    create(data: Omit<DocumentChart, 'id'>) {
        return request.post<BaseResponse<DocumentChart>>('/document-charts/', data);
    },

    update(id: number, data: Partial<DocumentChart>) {
        return request.put<BaseResponse<DocumentChart>>(`/document-charts/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<DocumentChart>) {
        return request.patch<BaseResponse<DocumentChart>>(`/document-charts/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/document-charts/${id}/`);
    }
};

// --- Documents API ---
export const documentsService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Documents[]>>('/documents/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Documents>>(`/documents/${id}/`);
    },

    create(data: Omit<Documents, 'id'>) {
        return request.post<BaseResponse<Documents>>('/documents/', data);
    },

    update(id: number, data: Partial<Documents>) {
        return request.put<BaseResponse<Documents>>(`/documents/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Documents>) {
        return request.patch<BaseResponse<Documents>>(`/documents/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/documents/${id}/`);
    }
};

// --- Examination Images API ---
export const examinationImagesService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<ExaminationImages[]>>('/examination-images/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<ExaminationImages>>(`/examination-images/${id}/`);
    },

    create(data: Omit<ExaminationImages, 'id'>) {
        return request.post<BaseResponse<ExaminationImages>>('/examination-images/', data);
    },

    update(id: number, data: Partial<ExaminationImages>) {
        return request.put<BaseResponse<ExaminationImages>>(`/examination-images/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<ExaminationImages>) {
        return request.patch<BaseResponse<ExaminationImages>>(`/examination-images/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/examination-images/${id}/`);
    }
};

// --- Identity API ---
export const identityService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Identity[]>>('/identity/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Identity>>(`/identity/${id}/`);
    },

    create(data: Omit<Identity, 'id'>) {
        return request.post<BaseResponse<Identity>>('/identity/', data);
    },

    update(id: number, data: Partial<Identity>) {
        return request.put<BaseResponse<Identity>>(`/identity/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Identity>) {
        return request.patch<BaseResponse<Identity>>(`/identity/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/identity/${id}/`);
    }
};

// --- Images API ---
export const imageService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Image[]>>('/images/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Image>>(`/images/${id}/`);
    },

    create(data: Omit<Image, 'id'>) {
        return request.post<BaseResponse<Image>>('/images/', data);
    },

    update(id: number, data: Partial<Image>) {
        return request.put<BaseResponse<Image>>(`/images/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Image>) {
        return request.patch<BaseResponse<Image>>(`/images/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/images/${id}/`);
    }
};

// --- Shapes API ---
export const shapeService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Shape[]>>('/shapes/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Shape>>(`/shapes/${id}/`);
    },

    create(data: Omit<Shape, 'id'>) {
        return request.post<BaseResponse<Shape>>('/shapes/', data);
    },

    update(id: number, data: Partial<Shape>) {
        return request.put<BaseResponse<Shape>>(`/shapes/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Shape>) {
        return request.patch<BaseResponse<Shape>>(`/shapes/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/shapes/${id}/`);
    }
};

// --- Testing Sheets API ---
export const testingSheetService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<TestingSheet[]>>('/testing-sheets/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<TestingSheet>>(`/testing-sheets/${id}/`);
    },

    create(data: Omit<TestingSheet, 'id'>) {
        return request.post<BaseResponse<TestingSheet>>('/testing-sheets/', data);
    },

    update(id: number, data: Partial<TestingSheet>) {
        return request.put<BaseResponse<TestingSheet>>(`/testing-sheets/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<TestingSheet>) {
        return request.patch<BaseResponse<TestingSheet>>(`/testing-sheets/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/testing-sheets/${id}/`);
    }
};

// --- Texts API ---
export const textService = {
    getList(params?: QueryParams) {
        return request.get<BaseResponse<Text[]>>('/texts/', { params });
    },

    getById(id: number) {
        return request.get<BaseResponse<Text>>(`/texts/${id}/`);
    },

    create(data: Omit<Text, 'id'>) {
        return request.post<BaseResponse<Text>>('/texts/', data);
    },

    update(id: number, data: Partial<Text>) {
        return request.put<BaseResponse<Text>>(`/texts/${id}/`, data);
    },

    partialUpdate(id: number, data: Partial<Text>) {
        return request.patch<BaseResponse<Text>>(`/texts/${id}/`, data);
    },

    delete(id: number) {
        return request.delete(`/texts/${id}/`);
    }
};
