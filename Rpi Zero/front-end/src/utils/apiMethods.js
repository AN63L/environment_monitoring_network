import logger from './logger';
import store from '../store/index';
import axios from "axios";

const url = import.meta.env.VITE_API_PATH;
let parsed_quiet;

export async function get(path, quiet, queryParams) {
    try{
        if (quiet == undefined || quiet == false){
            store.dispatch('toggleLocalSpinner', true);
        }
        // globally manaqe quiet status - if not connected to API always quiet
        if (store.getters.storeToastData){
            parsed_quiet = true
        } else {
            parsed_quiet = quiet
        }
        // display loader
        let full_path;
        full_path = url.concat(path)
        let filters = '';
        if (queryParams != undefined){
            for (let i = 0; i < queryParams.length; i++){
                filters += '?' + queryParams[i].name + '=' + queryParams[i].value
            }
        }
        full_path = full_path.concat(filters)
        return await axios.get(full_path);
    } catch(e){
        logger.error('ERROR WITH GET: ', e)
        // hide loader and display error modal
        store.dispatch('toggleLocalSpinner', false);
        if (!parsed_quiet){
            store.dispatch('displayLocalModal', {
                modalType: 'INFO',
                modalMessage: e.toString(),
                modalTitle: 'Error with API call',
                modalCancelText: 'Close',
                modalSuccessText: null,
                modalConfirmFunction: 'EMPTY'
            });
        }
        return null
    } finally {
        // hide loader
        if (quiet == undefined || quiet == false){
            store.dispatch('toggleLocalSpinner', false);
        }
    }
}

export async function put(path, quiet, body) {
    try{
        if (quiet == undefined || quiet == false){
            store.dispatch('toggleLocalSpinner', true);
        }
        // globally manaqe quiet status - if not connected to API always quiet
        if (store.getters.storeToastData){
            parsed_quiet = true
        } else {
            parsed_quiet = quiet
        }
        // display loader
        let full_path;
        full_path = url.concat(path)
        return await axios.put(full_path, body);
    } catch(e){
        logger.error('ERROR WITH PUT: ', e)
        // hide loader and display error modal
        store.dispatch('toggleLocalSpinner', false);
        if (!parsed_quiet){
            store.dispatch('displayLocalModal', {
                modalType: 'INFO',
                modalMessage: e.toString(),
                modalTitle: 'Error with API call',
                modalCancelText: 'Close',
                modalSuccessText: null,
                modalConfirmFunction: 'EMPTY'
            });
        }
        return null
    } finally {
        // hide loader
        if (quiet == undefined || quiet == false){
            store.dispatch('toggleLocalSpinner', false);
        }
    }
}