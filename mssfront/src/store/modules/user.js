
const state = {
    slug:"",
    role:"",
}

const getters = {
}

const actions = {
}

const mutations = {
    setSlug:( state, slug )=>(state.slug = slug),
    setRole:( state, role )=>(state.role = role)
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}