import pickle

import pytest

import openai_zero

EXCEPTION_TEST_CASES = [
    openai_zero.InvalidRequestError(
        "message",
        "param",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    openai_zero.error.AuthenticationError(),
    openai_zero.error.PermissionError(),
    openai_zero.error.RateLimitError(),
    openai_zero.error.ServiceUnavailableError(),
    openai_zero.error.SignatureVerificationError("message", "sig_header?"),
    openai_zero.error.APIConnectionError("message!", should_retry=True),
    openai_zero.error.TryAgain(),
    openai_zero.error.Timeout(),
    openai_zero.error.APIError(
        message="message",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    openai_zero.error.OpenAIError(),
]


class TestExceptions:
    @pytest.mark.parametrize("error", EXCEPTION_TEST_CASES)
    def test_exceptions_are_pickleable(self, error) -> None:
        assert error.__repr__() == pickle.loads(pickle.dumps(error)).__repr__()
