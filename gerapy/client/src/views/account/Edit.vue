<template>
  <div class="panel">
    <panel-title :title="$lang.titles.editAccount"></panel-title>
    <div v-loading="loadData" :element-loading-text="$lang.messages.loading" class="panel-body">
      <el-row>
        <el-col :span="10">
          <!--					子组件导入使用，并传参-->
          <substance :id="routeId" ref="substance">
            <template slot="submit">
              <!--					子组件只负责表单操作，不参与接口开发-->
              <el-button :loading="onSubmitLoading" size="small" type="primary" @click="onSubmitForm">
                <i class="fa fa-check"></i>
                {{ $lang.buttons.update }}
              </el-button>
            </template>
          </substance>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script type="text/javascript">
import PanelTitle from "../../components/PanelTitle";
import Substance from "./Substance";

export default {
  data() {
    return {
      onSubmitLoading: false,
      loadData: false,
      routeId: this.$route.params.id,  // 获取路由中携带的参数
    };
  },
  methods: {
    onSubmitForm() {
      // 调用子组件form实力，校验成功后进行接口请求
      this.$refs.substance.$refs.form.validate((valid) => {
        if (!valid) return false;
        this.onSubmitLoading = true;
        let formData = this.$refs.substance.formData;
        // 执行更新
        this.$http
          .post(
            this.formatString(this.$store.state.url.account.update, {
              id: this.routeId,
            }),
            formData
          )
          .then(() => {
            this.$message.success(
              this.$store.getters.$lang.messages.successSave
            );
            this.onSubmitLoading = false;
          })
          .catch(() => {
            this.onSubmitLoading = false;
          });
      });
    },
  },
  components: {
    PanelTitle,
    Substance,
  },
};
</script>

