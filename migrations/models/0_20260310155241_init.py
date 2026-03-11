from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "nickname" VARCHAR(50),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "token_blacklist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" TEXT NOT NULL,
    "expires_at" TIMESTAMPTZ NOT NULL,
    "logout_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmFtP2zAUx79KlSeQGIKOAtpbWsrogHaCsCEQitzETa06doidtRXqd5/t3G9dQcBaqW"
    "/puTjn/Ozm/JMXzaU2xGzfoBNI2hhYE4wY1741XjQCXCguaiL2GhrwvNQvDRwMsUrhMtYc"
    "5oKHjPvAkkuPAGZQmGzILB95HFEirCTAWBqpJQIRcVJTQNBzAE1OHcjH0BeOxydhRsSGM8"
    "jin97EHCGI7VztyJb3VnaTzz1l6xF+rgLl3YamRXHgkjTYm/MxJUk0Iqp8BxLoAw7l8twP"
    "ZPmyuqjhuKOw0jQkLDGTY8MRCDDPtLsiA4sSyU9Uw1SDjrzLl+bh0cnR6dfjo1MRoipJLC"
    "eLsL209zBREegb2kL5AQdhhMKYclMbWEZnwFkNuyShgE8UXcQXw1rGLzakANND8z4El+Ax"
    "uveGLNpl7BlLQ/+XftO50G92rvX7XeWZR56rQf97HE7F8Q6Pf79zNWgrwilROPOQD5kJeB"
    "nrmSDDkQur0eYzC3ztKHU/vtg82r3r7q2hX//MIT/Tja70NHO4Y+vO8W6eeLJI43fPuGjI"
    "n42HQb+riFHGHV/dMY0zHjRZEwg4NQmdmsDOth2bY1NuJzF1aMDfsJG5xM3cR82HwB4QPI"
    "8eaRuyr9HTd+m2Bgz65qvmRSbj30NjTfbvHeaGHLajSeXYkETKAM+pD5FDLuFcceyJigCx"
    "YAW3SGrcRcusH79FfAZia3q4fDBNBEj2aIj2RFOQqwY7+m1HP+tqCuJQyKMp8G0zR1N6aJ"
    "MWLEls2eU23aIFEOCo/mUXsuYs2AptFwOvV3SyIbbVcZum46ALEC6j64yBXyM24oT30XEf"
    "zs8FMxND4vCxhNZqLaEVizgRVZgysb5rhr68cPMAY1PqVxzAeorZnE0RxJ+AkiBroq5fgT"
    "Kb8yaU0Yn7byRbByuAbB3UcpSuPEZLiDDR7hsUaD5zK0HXQIKW1FS9MkhPQPJlReylevNm"
    "5ZPQjtY4v7yBGCjKtYKr/G1n/fa9TnotPlIw6dBH1rhKMkWepaIJpDFb1bRBqumP0LrR/2"
    "XVMZVJ2Q78BKT8a7wCYhS+mQAPD1YZ9CKqFqDyFUY9JRySijn/43bQr5nxaUoB5B0RDT7a"
    "yOJ7Dfmcf1pPrEsoyq6Xf5ktfoQtDGm5QLvqG8Znvo8v/gKKTyk4"
)
