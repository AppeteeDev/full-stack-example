/**
 * Débats IDO API
 * API of Débats IDO Project
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { Protagonist } from '../model/protagonist';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class ProtagonistService {

    protected basePath = '/';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Retrieve a collection of Protagonist objects
     * This operation supports pagination
     * @param offset The number of items to skip before returning the results
     * @param limit The number of items to return
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public protagonistGet(offset?: number, limit?: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public protagonistGet(offset?: number, limit?: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public protagonistGet(offset?: number, limit?: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public protagonistGet(offset?: number, limit?: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {



        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (offset !== undefined && offset !== null) {
            queryParameters = queryParameters.set('offset', <any>offset);
        }
        if (limit !== undefined && limit !== null) {
            queryParameters = queryParameters.set('limit', <any>limit);
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<any>('get',`${this.basePath}/protagonist`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Create Protagonist
     * 
     * @param body 
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public protagonistPost(body: Protagonist, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public protagonistPost(body: Protagonist, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public protagonistPost(body: Protagonist, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public protagonistPost(body: Protagonist, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling protagonistPost.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('post',`${this.basePath}/protagonist`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Delete Protagonist object
     * Test
     * @param protagonistID The Id of a Protagonist
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public protagonistsProtagonistIDDelete(protagonistID: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public protagonistsProtagonistIDDelete(protagonistID: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public protagonistsProtagonistIDDelete(protagonistID: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public protagonistsProtagonistIDDelete(protagonistID: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (protagonistID === null || protagonistID === undefined) {
            throw new Error('Required parameter protagonistID was null or undefined when calling protagonistsProtagonistIDDelete.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<any>('delete',`${this.basePath}/protagonists/${encodeURIComponent(String(protagonistID))}/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve a Protagonist object
     * Test
     * @param protagonistID The Id of a Protagonist
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public protagonistsProtagonistIDGet(protagonistID: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public protagonistsProtagonistIDGet(protagonistID: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public protagonistsProtagonistIDGet(protagonistID: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public protagonistsProtagonistIDGet(protagonistID: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (protagonistID === null || protagonistID === undefined) {
            throw new Error('Required parameter protagonistID was null or undefined when calling protagonistsProtagonistIDGet.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<any>('get',`${this.basePath}/protagonists/${encodeURIComponent(String(protagonistID))}/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Update Protagonist object
     * Test
     * @param body 
     * @param protagonistID The Id of a Protagonist
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public protagonistsProtagonistIDPatch(body: Protagonist, protagonistID: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public protagonistsProtagonistIDPatch(body: Protagonist, protagonistID: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public protagonistsProtagonistIDPatch(body: Protagonist, protagonistID: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public protagonistsProtagonistIDPatch(body: Protagonist, protagonistID: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling protagonistsProtagonistIDPatch.');
        }

        if (protagonistID === null || protagonistID === undefined) {
            throw new Error('Required parameter protagonistID was null or undefined when calling protagonistsProtagonistIDPatch.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('patch',`${this.basePath}/protagonists/${encodeURIComponent(String(protagonistID))}/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
