import strawberry


@strawberry.type(description="Book Schema")
class BookSchema:
    id: int
    name: str


@strawberry.input(description="Book Mutation Schema")
class BookMutationSchema:
    name: str
