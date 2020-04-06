/**
 * Débats IDO API
 * API of Débats IDO Project
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { Quote } from './quote';
import { Theme } from './theme';


export interface QuoteTheme { 
    themeID: number;
    theme?: Theme;
    quoteID: number;
    quote?: Quote;
}
