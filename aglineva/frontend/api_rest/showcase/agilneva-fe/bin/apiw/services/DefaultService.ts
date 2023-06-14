/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { GradeRequest } from '../models/GradeRequest';
import type { MeanGradesResponse } from '../models/MeanGradesResponse';
import type {  RestaurantListResponse } from '../models/RestaurantListResponse';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Get all restaurants
     * @returns RestaurantListResponse Successful operation
     * @throws ApiError
     */
    public static listRestaurants(): CancelablePromise<RestaurantListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            
            url: '/restaurants',
        });
    }

    /**
     * Add a grade to a restaurant
     * @param requestBody
     * @returns RestaurantListResponse Successful operation
     * @throws ApiError
     */
    public static addGrade(
        requestBody: GradeRequest,
    ): CancelablePromise<RestaurantListResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/grade',
            body: requestBody,
            mediaType: 'application/json',
        });
    }

    /**
     * Get mean grades for all restaurants
     * @returns MeanGradesResponse Successful operation
     * @throws ApiError
     */
    public static listMean(): CancelablePromise<MeanGradesResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/mean',
        });
    }

    /**
     * Sort restaurants alphabetically
     * @returns RestaurantListResponse Successful operation
     * @throws ApiError
     */
    public static sortRestaurantsAlpha(): CancelablePromise<RestaurantListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/restaurants/sort_alpha',
        });
    }

    /**
     * Sort restaurants by mean grade
     * @returns RestaurantListResponse Successful operation
     * @throws ApiError
     */
    public static sortRestaurantsMean(): CancelablePromise<RestaurantListResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/restaurants/sort_mean',
        });
    }

}
