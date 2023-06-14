/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type RestaurantListResponse = {
    nodes?: Array<{
        id?: string;
        projet?: string[] | null;
    }>;
}

export type RestaurantListRdesponse = {
    restaurants?: Record<string, Array<Record<string, number>>>;
};

export type RestaurantListResponse3 = {
    nodes?: Array<{
      id?: string;
      projet?: string[] | null;
    }>;
  };

