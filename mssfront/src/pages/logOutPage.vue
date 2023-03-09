<script setup>
import LogOutService from '@/../services/LogOutService';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
sessionStorage.clear()
const store = useStore()
const router = useRouter()
const logOutService = new LogOutService()
logOutService.LogOut(store.state.user.slug)
sessionStorage.clear()
localStorage.clear()
router.push("/")
</script>