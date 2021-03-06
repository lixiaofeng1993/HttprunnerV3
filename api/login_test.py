# NOTE: Generated By HttpRunner v3.1.11
# FROM: api\login.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLogin(HttpRunner):

    config = Config("登录接口").base_url("${ENV(base_url)}").export(*["token"])

    teststeps = [
        Step(
            RunRequest("登录接口 测试用例")
            .post("/users/login")
            .with_data({"username": "lixiaofeng", "password": 123456})
            .extract()
            .with_jmespath("body.result.access_token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.result.name", "lixiaofeng")
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
