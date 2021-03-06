/**
 * SPOT API
 * API of SPOT Project
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { Quote } from './quote';
import { Reference } from './reference';


export interface QuoteReference { 
    quoteID: number;
    quote?: Quote;
    referenceID: number;
    reference?: Reference;
}

