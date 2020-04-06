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
 */
import { Protagonist } from './protagonist';
import { Quote } from './quote';

export interface QuoteAuthor { 
    quoteID: number;
    quote?: Quote;
    authorID: number;
    author?: Protagonist;
}