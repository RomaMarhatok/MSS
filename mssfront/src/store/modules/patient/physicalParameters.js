import PhysicalService from "@/../services/PhysicalService"
const physicalService = new PhysicalService()
const state = {
    physicalParameters:[]
}
const getters = {
    getPhysicalParameters:(state)=>{
        return state.physicalParameters
    },
    getChartsDataSet:(state)=>{
        const labels = []
        const weightDataSet = {
            label:"Вес",
            data:[],
            fill:false,
            tension: 0.4,
        }
        const heightDataSet = {
            label:"Рост",
            data:[],
            fill:false,
            tension: 0.4,
        }
        const pressureDataSet = {
            label:"Давление",
            data:[],
            fill:false,
            tension: 0.4,
        }
        state.physicalParameters.forEach(physicalParameter=>{
            labels.push(physicalParameter.created_at)
            weightDataSet.data.push(physicalParameter.weight)
            heightDataSet.data.push(physicalParameter.height)
            pressureDataSet.data.push(physicalParameter.pressure)
        })
        
        return {
            labels: labels,
            datasets: [weightDataSet, heightDataSet, pressureDataSet],
        }
    }

}
const actions = {
    async fetchPhysicalParameters({commit},patientSlug){
        await physicalService.getPhysicalParametersForPatient(
                physicalParameters=>commit("setPhysicalParameters",physicalParameters),
                error=>console.log(error),
                patientSlug
            )
    }
}
const mutations = {
    setPhysicalParameters:(state,physicalParameters)=>{
        console.log("setPhysicalParameters",physicalParameters)
        state.physicalParameters = physicalParameters
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}