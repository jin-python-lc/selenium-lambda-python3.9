cat << EOF >> ~/.docker/config.json

{
    "proxies":
    {
        "default":
        {
            "httpProxy": "${HTTP_PROXY}",
            "httpsProxy": "${HTTPS_PROXY}",
            "noProxy" : "${NO_PROXY}"
        }
    }
}
EOF