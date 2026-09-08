import { createServer } from "node:http";

const server = createServer((request, response) => {
  if (request.url === "/health") {
    response.writeHead(200, { "content-type": "application/json" });
    response.end(JSON.stringify({ status: "ok" }));
    return;
  }
  response.writeHead(404, { "content-type": "application/json" });
  response.end(JSON.stringify({ error: "not_found" }));
});

if (process.env.NODE_ENV !== "test") {
  server.listen(3000, "127.0.0.1", () => console.log("http://127.0.0.1:3000"));
}

export { server };
