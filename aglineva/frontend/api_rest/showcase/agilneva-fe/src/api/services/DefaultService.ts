/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Grade } from '../models/Grade';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Get API info
     * @returns any Successful Response
     * @throws ApiError
     */
    public static info(): CancelablePromise<{
        message?: string;
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/',
        });
    }

    /**
     * Get the showcase page
     * @returns string Successful Response
     * @throws ApiError
     */
    public static showcase(): CancelablePromise<string> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/showcase',
        });
    }

    /**
     * List restaurants
     * @returns number Successful Response
     * @throws ApiError
     */
    public static listRestaurants(): CancelablePromise<Record<string, Array<Record<string, number>>>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/restaurants',
        });
    }

    /**
     * Add a grade to a restaurant
     * @param requestBody
     * @returns number Successful Response
     * @throws ApiError
     */
    public static addGrade(
        requestBody: Grade,
    ): CancelablePromise<Record<string, Array<Record<string, number>>>> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/grade',
            body: requestBody,
            mediaType: 'application/json',
        });
    }

    /**
     * List mean grades for all restaurants
     * @returns number Successful Response
     * @throws ApiError
     */
    public static listMean(): CancelablePromise<Record<string, number>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/mean',
        });
    }

    /**
     * List restaurants sorted alphabetically
     * @returns number Successful Response
     * @throws ApiError
     */
    public static sortRestaurants(): CancelablePromise<Record<string, Array<Record<string, number>>>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/restaurants/sort_alpha',
        });
    }

    /**
     * List restaurants sorted by mean grade
     * @returns number Successful Response
     * @throws ApiError
     */
    public static sortRestaurantsMean(): CancelablePromise<Record<string, Array<Record<string, number>>>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/restaurants/sort_mean',
        });
    }

}
