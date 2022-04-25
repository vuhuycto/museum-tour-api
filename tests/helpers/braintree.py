import attr


@attr.s(auto_attribs=True)
class TransactionSaleMock:
    id: str


@attr.s(auto_attribs=True)
class SaleMock:
    is_success: bool
    transaction: TransactionSaleMock


@attr.s(auto_attribs=True)
class SuccessfulTransactionMock:
    def sale(self, *args):
        return SaleMock(is_success=True, transaction=TransactionSaleMock(id="a"))


@attr.s(auto_attribs=True)
class FailedTransactionMock:
    def sale(self, *args):
        return SaleMock(is_success=False, transaction=TransactionSaleMock(id="a"))


@attr.s(auto_attribs=True)
class SuccessfulBraintreeGatewayMock:
    transaction = SuccessfulTransactionMock()


@attr.s(auto_attribs=True)
class FailedBraintreeGatewayMock:
    transaction = FailedTransactionMock()


def mock_braintree_gateway(mocker, failure: bool = False):
    dep = "braintree.BraintreeGateway"

    if failure:
        mocker.patch(dep, return_value=FailedBraintreeGatewayMock())
        return

    mocker.patch(dep, return_value=SuccessfulBraintreeGatewayMock())
