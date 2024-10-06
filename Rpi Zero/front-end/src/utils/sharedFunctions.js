import logger from '@/utils/logger';
import store from '@/store/index';

export async function selectFunction (value) {
    try {
        switch (value) {
            case 'EMPTY': 
                nothing();
                break;
            default: 
                logger.error('ERROR selecting function: ');        
        }
    } catch (e) {
        logger.error('ERROR selecting function: ', e);
        await store.dispatch('displayGlobalToast', {globalToastText: 'ERROR: ' + e, globalToastType: 'DANGER'})
    }
}

const nothing = async () => {
    return;
}

const waterSatDensity = (temp) => {
    const rho_max = (6.112* 100 * Math.exp((17.62 * temp)/(243.12 + temp)))/(461.52 * (temp + 273.15))
    return rho_max
}
		

// https://github.com/thstielow/raspi-bme680-iaq/blob/main/bme680IAQ.py
// https://www.freeonlinecalc.com/air-quality-index-aqi-calculation-review-and-formulas.html
// https://aqicn.org/calculator/
export async function measure_AQI (temperature, pressure, humidity, gas_resistance, pm_2, pm_10) {
    try {
        // calculate BME680 sensor data AQ
        const ph_slope = 0.03
        const gas_ceil = 1
        const gas_recal_step = 0
        const gas_recal_period = 3600
        const burn_in_cycles = 300
        const rho_max = waterSatDensity(temperature)
        const hum_abs = humidity * 10 * rho_max
        const comp_gas = gas_resistance * Math.exp(ph_slope * hum_abs)
        const AQ = Math.min((comp_gas / gas_ceil)**2, 1) * 100
        // calculate PMS7003 sensor data AQ - PM 2.5
        let AQPM2;
        // 0-50
        if (pm_2>= 0 && pm_2<30){
            AQPM2 = ((50 - 0) / (30 - 0)) * (pm_2 - 0) + 0
        } 
        // 51-100
        else if (pm_2>= 30 && pm_2<60){
            AQPM2 = ((100 - 51) / (60 - 30)) * (pm_2 - 30) + 51
        } 
        // 101-200
        else if (pm_2>= 60 && pm_2<90){
            AQPM2 = ((200 - 101) / (90 - 60)) * (pm_2 - 60) + 101
        } 
        // 201-300
        else if (pm_2>= 90 && pm_2<120){
            AQPM2 = ((300 - 201) / (120 - 90)) * (pm_2 - 90) + 201
        } 
        // 301-400
        else if (pm_2>= 120 && pm_2<250){
            AQPM2 = ((400 - 301) / (250 - 120)) * (pm_2 - 120) + 301
        } 
        // 401-500
        else if (pm_2> 250 ){
            // does not matter what the value is, IAQ is really bad
            AQPM2 = 300
        } else {
            // big negative value to show error
            AQPM2 = -30000
        }
        // calculate PMS7003 sensor data AQ - PM 2.5
        let AQPM10;
        if (pm_10>= 0 && pm_10<12){
            AQPM10 = ((50 - 0) / (12 - 0)) * (pm_10 - 0) + 0
        } 
        // 51-100
        else if (pm_10>= 12 && pm_10<25){
            AQPM10 = ((100 - 51) / (25 - 12)) * (pm_10 - 12) + 51
        } 
        // 101-200
        else if (pm_10>= 25 && pm_10<50){
            AQPM10 = ((200 - 101) / (50 - 25)) * (pm_10 - 25) + 101
        } 
        // 201-300
        else if (pm_10>= 50 && pm_10<90){
            AQPM10 = ((300 - 201) / (90 - 50)) * (pm_10 - 50) + 201
        } 
        // 301-400
        else if (pm_10>= 90 && pm_10<180){
            AQPM10 = ((400 - 301) / (180 - 90)) * (pm_10 - 90) + 301
        } 
        // 401-500
        else if (pm_10> 180 ){
            // does not matter what the value is, IAQ is really bad
            AQPM10 = 300
        } else {
            // big negative value to show error
            AQPM10 = -30000
        }
        const AQI = (AQ + AQPM2 + AQPM10)/3
        return AQI
    } catch (e){
        logger.log('ERROR measuring AQI.. returning null: ', e)
        return null
    }

}

export async function qualitative_AQI (AQ) {
    try {
        let qual_value;
        if (AQ> 0 && AQ <= 50){
            qual_value = 'Good'
        } else if (AQ> 50 && AQ <= 100){
            qual_value = 'Moderate'
        } else if (AQ> 100 && AQ <= 150){
            qual_value = 'Unhealthy for sensitive groups'
        } else if (AQ> 150 && AQ <= 200){
            qual_value = 'Unhealthy'
        } else if (AQ> 200 && AQ <= 300){
            qual_value = 'Very unhealthy'
        } else if (AQ> 300){
            qual_value = 'Hazardous'
        } else {
            qual_value  = 'ERROR'
        } 
        return qual_value
    } catch (e){
        logger.log('ERROR qualifying AQI.. returning null: ', e)
        return null
    }
}

export default {selectFunction, measure_AQI, qualitative_AQI};